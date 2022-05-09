from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def home(request):
    res = {
        'name': 'Name',
        'location': 'Location'
    }
    res_2 = {
        'response': 'Second',
        'after': 'Token'
    }
    if request.method == 'GET':
        return JsonResponse(res)
    if request.method == 'POST':
        return JsonResponse(res_2)
