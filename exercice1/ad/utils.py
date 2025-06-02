import requests

from .models import Ad


def get_ad_from_api(url):
    response = requests.get(url)
    response.raise_for_status()
    json_data = response.json()

    new_ad = Ad(
        url=url,
        dept_code=json_data["departmentCode"],
        zip_code=json_data["postalCode"],
        city=json_data["city"],
        annual_condominium_fees=json_data["annualCondominiumFees"],
    )
    return new_ad
