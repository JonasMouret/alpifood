from django.http import JsonResponse
from alpifoodapp.models import Restaurant
from alpifoodapp.serializers import RestaurantSerializers
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.models import AccessToken

def customers_get_restaurant(request):
    restaurants = RestaurantSerializers(
        Restaurant.objects.all().order_by("-id"),
        many = True
    ).data

    return JsonResponse ({"restaurants": restaurants})