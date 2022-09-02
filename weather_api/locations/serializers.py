from rest_framework import serializers
from locations.models import Country, State, City


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializerRead(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = State
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CitySerializerRead(serializers.ModelSerializer):
    state = StateSerializerRead()

    class Meta:
        model = City
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
