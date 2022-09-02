from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from locations.serializers import CountrySerializer, StateSerializer, StateSerializerRead, CitySerializer, CitySerializerRead
from locations.models import Country, State, City


class CountryViewSet(viewsets.ModelViewSet):

    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return StateSerializerRead
        return self.serializer_class


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CitySerializerRead
        return self.serializer_class

    @action(detail=False, methods=['get'])
    def weather(self, request):
        all_cities = City.objects.all()
        data = []
        for city in all_cities:
            data.append({
                "name": city.name,
                "state": city.state.name,
                "country": city.state.country.name
                # TODO: add weather data
            })
        return Response(data)

    @action(detail=True, methods=['get'])
    def forecast(self, request,  pk=None):
        city = City.objects.get(id=pk)
        data = {
            "name": city.name,
            "state": city.state.name,
            "country": city.state.country.name
            # TODO: add forecast data
        }
        return Response(data)
