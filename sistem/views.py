from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import numpy as np
from libraries.perhitungan import Perhitungan
# Create your views here.

def index(request):

	return render(request, 'layout.html')
