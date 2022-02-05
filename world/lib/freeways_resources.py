from django.http import JsonResponse
from models.passenger_car_restrictions_model import PassengerCarRestrictions

class FreewayResource:

    @staticmethod
    def get_all_freeways(req) -> JsonResponse:
        pass