from rest_framework import serializers # type: ignore
from .models import CountryDetails

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryDetails
        fields = '__all__'



