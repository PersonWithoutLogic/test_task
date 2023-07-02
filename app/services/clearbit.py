import requests
from typing import Optional

def enrich_person(email: str, api_key: str) -> dict:
    url = f"https://person.clearbit.com/v2/combined/find?email={email}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {
            "full_name":


def enrich_person(email: str, api_key: str) -> dict:
    url = f"https://person.clearbit.com/v2/combined/find?email={email}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {
            "full_name": data.get("person", {}).get("name", {}).get("fullName"),
            "location": data.get("person", {}).get("location", {}).get("name"),
            "company": data.get("company", {}).get("name"),
            "title": data.get("person", {}).get("employment", {}).get("title"),
        }
    else:
        return {}
