from django.shortcuts import render
from .models import FaktorResiko
from utils.helper import context_response
from django.http import HttpResponse, JsonResponse

# Create your views here.

def detail(request):
	id_faktor_resiko = request.POST.get('id')
	faktor = FaktorResiko.objects.get(pk=id_faktor_resiko)

	context = {
		'faktor' : faktor.faktor
	}
	context = context_response(True, context)

	return JsonResponse(context, safe=False)