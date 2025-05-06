import requests
from django.core.management.base import BaseCommand
from app1.models import CountryDetails 

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code != 200:
            self.stderr.write("Failed to fetch data")
            return

        countries = response.json()
        CountryDetails.objects.all().delete()

        for country in countries:
            try:
                CountryDetails.objects.update_or_create(
                    cca2=country.get("cca2", ""),
                    defaults={
                        "name": country.get("name", {}),
                        "tld": country.get("tld", []),
                        "ccn3": country.get("ccn3", None),
                        "cioc": country.get("cioc", None),
                        "independent": country.get("independent", False),
                        "status": country.get("status", ""),
                        "un_member": country.get("unMember", False),
                        "currencies": country.get("currencies", {}),
                        "idd": country.get("idd", {}),
                        "capital": country.get("capital", []),
                        "alt_spellings": country.get("altSpellings", []),
                        "region": country.get("region", ""),
                        "subregion": country.get("subregion", ""),
                        "languages": country.get("languages", {}),
                        "latlng": country.get("latlng", []),
                        "landlocked": country.get("landlocked", False),
                        "borders": country.get("borders", []),
                        "area": country.get("area", 0),
                        "demonyms": country.get("demonyms", {}),
                        "cca3": country.get("cca3", ""),
                        "translations": country.get("translations", {}),
                        "flag": country.get("flag", ""),
                        "maps": country.get("maps", {}),
                        "population": country.get("population", 0),
                        "gini": country.get("gini", {}),
                        "fifa": country.get("fifa", ""),
                        "car": country.get("car", {}),
                        "timezones": country.get("timezones", []),
                        "continents": country.get("continents", []),
                        "flags": country.get("flags", {}),
                        "coat_of_arms": country.get("coatOfArms", {}),
                        "start_of_week": country.get("startOfWeek", ""),
                        "capital_info": country.get("capitalInfo", {}),
                        "postal_code": country.get("postalCode", {}),
                    }
                )
                self.stdout.write(self.style.SUCCESS(f"Saved {country.get('cca2')}"))
            except Exception as e:
                self.stderr.write(f"Error saving {country.get('cca2', 'N/A')}: {str(e)}")
