from rest_framework import serializers

from alpifoodapp.models import Restaurant

class RestaurantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "phone", "address", "logo")
