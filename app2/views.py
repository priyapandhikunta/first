from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def priya(request):
    return HttpResponse(' priya hello')


def lakshmi(request):
    return HttpResponse('thinava')
