from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import sys

@csrf_exempt
def index(request):
        return HttpResponse("This is a test page!")