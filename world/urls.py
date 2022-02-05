from django.urls import path
from django.http import JsonResponse

def get_freeways(req):

    return JsonResponse({
        "freeways": []
    })

urlpatterns = [
    path('freeways', get_freeways)
]