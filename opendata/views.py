from django.shortcuts import render
import requests
from .NYC_API import API_ENDPOINT


# Create your views here.
def get_nyc_api_data() -> list:
    """
    this function for data getting for nys open api
    here we will fetch all json data and will return list
    :return: [{data 1}, {data 2} ..., {data n}]
    """
    api_response = requests.get(API_ENDPOINT)
    jon_data = api_response.json()
    data = []
    for building_data in jon_data:
        building_info = {}
        # zip_code
        if 'zip_code' in building_data:
            building_info["zip_code"] = building_data["zip_code"]
        else:
            building_info["zip_code"] = '-'  # haven't zip code

        # address
        if 'street_name' in building_data:
            street_name = building_data["street_name"]
        else:
            street_name = '-'  # haven't street name
        if 'zoning' in building_data:
            zoning = building_data["zoning"]
        else:
            zoning = '-'  # haven't info about zoning data
        if 'housenum_lo' in building_data:
            housenum_lo = building_data["housenum_lo"]
        else:
            housenum_lo = '-'  # haven't info about zoning data
        # gross_sqft
        if 'gross_sqft' in building_data:
            building_info["gross_sqft"] = building_data["gross_sqft"]
        else:
            building_info["gross_sqft"] = '-'
        # year building
        if 'yrbuilt' in building_data:
            building_info["yrbuilt"] = building_data["yrbuilt"]
        else:
            building_info["yrbuilt"] = '-'
        # pytaxclass building
        if 'pytaxclass' in building_data:
            building_info["pytaxclass"] = building_data["pytaxclass"]
        else:
            building_info["pytaxclass"] = '-'
        # owner building
        if 'owner' in building_data:
            building_info["owner"] = building_data["owner"]
        else:
            building_info["owner"] = '-'

        building_info["address"] = f"{housenum_lo}, {street_name}, {zoning}"
        data.append(building_info)
    return data
