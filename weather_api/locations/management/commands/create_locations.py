import os
import csv
import enum
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from locations.models import Country, State, City


class LocationType(enum.Enum):
    COUNTRY = 1
    STATE = 2
    CITY = 3


class Command(BaseCommand):
    help = 'Create countries, states and cities'

    def __handle_country(self, country_data):
        name = country_data[0].strip()
        try:
            country = Country.objects.get(name=name)
            self.stdout.write(self.style.WARNING(f"Country {name} already exists, ID: {country.id}"))
        except Country.DoesNotExist:
            Country.objects.create(name=name)
            self.stdout.write(self.style.SUCCESS(f"Country {name} created"))

    def __handle_state(self, state_data):
        name = state_data[0].strip()
        country_name = state_data[1].strip()
        try:
            country = Country.objects.get(name=country_name)
            state = State.objects.get(name=name, country=country)
            self.stdout.write(self.style.WARNING(f"State {name} already exists: ID: {state.id}"))
        except Country.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Country {country_name} does not exist"))
        except State.DoesNotExist:
            State.objects.create(name=name, country=country)
            self.stdout.write(self.style.SUCCESS(f"State {name} created"))

    def __handle_city(self, city_data):
        name = city_data[0].strip()
        latitude = city_data[1].strip()
        longitude = city_data[2].strip()
        state_name = city_data[3].strip()
        country_name = city_data[4].strip()
        try:
            country = Country.objects.get(name=country_name)
            state = State.objects.get(name=state_name, country=country)
            city = City.objects.get(name=name, state=state)
            self.stdout.write(self.style.WARNING(f"City {name} already exists: ID: {city.id}"))
        except Country.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Country {country_name} does not exist"))
        except State.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"State {state_name} does not exist"))
        except City.DoesNotExist:
            City.objects.create(name=name, state=state, latitude=latitude, longitude=longitude)
            self.stdout.write(self.style.SUCCESS(f"City {name} created"))

    def __handle_file(self, path, location: LocationType):
        with open(path, 'r') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                if location == LocationType.COUNTRY:
                    self.__handle_country(row)
                elif location == LocationType.STATE:
                    self.__handle_state(row)
                elif location == LocationType.CITY:
                    self.__handle_city(row)

    def handle(self, *args, **options):
        countries_path = os.path.join(settings.BASE_DIR, 'locations/management/commands/countries.csv')
        states_path = os.path.join(settings.BASE_DIR, 'locations/management/commands/states.csv')
        cities_path = os.path.join(settings.BASE_DIR, 'locations/management/commands/cities.csv')
        self.stdout.write(self.style.WARNING(f"--------------------- COUNTRIES ---------------------"))
        self.__handle_file(countries_path, LocationType.COUNTRY)
        self.stdout.write(self.style.WARNING(f"--------------------- STATES ---------------------"))
        self.__handle_file(states_path, LocationType.STATE)
        self.stdout.write(self.style.WARNING(f"--------------------- CITIES ---------------------"))
        self.__handle_file(cities_path, LocationType.CITY)
