from django.urls import path

from .views import AdListCreate, fetch_and_insert, quantiles

urlpatterns = [
    path("ads/", AdListCreate.as_view(), name="ad-list-create"),
    path("fetch_and_insert/", fetch_and_insert, name="fetch_and_insert"),
    path("quantiles/", quantiles, name="quantiles"),
]
