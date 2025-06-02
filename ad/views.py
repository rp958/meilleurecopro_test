import numpy
import requests
from django.shortcuts import redirect, render
from rest_framework import generics

from .forms import QuantilesForm, UrlForm
from .models import Ad
from .serializers import AdSerializer
from .utils import get_ad_from_api


class AdListCreate(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


def fetch_and_insert(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            ad_id = url.split("/")[-1]
            api_url = f"https://www.bienici.com/realEstateAd.json?id={ad_id}"
            try:
                get_ad_from_api(api_url).save()
                return redirect("ad-list-create")
            except requests.RequestException as e:
                form.add_error(None, f"Error fetching data: {e}")
    else:
        form = UrlForm()

    return render(request, "fetch_and_insert.html", {"form": form})


def quantiles(request):
    form = QuantilesForm(request.GET or None)
    ads = Ad.objects.all().order_by("annual_condominium_fees")

    if request.method == "GET" and form.is_valid():
        dept_code = form.cleaned_data.get("dept_code")
        city = form.cleaned_data.get("city")
        zip_code = form.cleaned_data.get("zip_code")

        if city != "":
            city = city.strip().lower()
        else:
            city = None
        if dept_code:
            ads = ads.filter(dept_code=dept_code)
        if city:
            ads = ads.filter(city__icontains=city)
        if zip_code is not None:
            ads = ads.filter(zip_code=zip_code)
    ads = ads.filter(annual_condominium_fees__isnull=False)

    if ads.count():
        all_annual_condo_fees = [
            condo_fee["annual_condominium_fees"]
            for condo_fee in ads.values("annual_condominium_fees")
        ]
        avg = round(sum(all_annual_condo_fees) / len(all_annual_condo_fees), 2)
        ten_quant = numpy.quantile(all_annual_condo_fees, 0.1)
        ninety_quant = numpy.quantile(all_annual_condo_fees, 0.9)
    else:
        avg = 0
        ten_quant = 0
        ninety_quant = 0
    return render(
        request,
        "quantiles.html",
        {
            "form": form,
            "ads": ads,
            "avg": avg,
            "ten_quant": ten_quant,
            "ninety_quant": ninety_quant,
        },
    )
