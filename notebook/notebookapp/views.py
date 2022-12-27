from django.shortcuts import render
from django.http import HttpResponse

from notebookapp.db import *

def index(request):
	return HttpResponse("Wellcome")

def listView(request):
	res = getlist2(request.user)

	return HttpResponse(res)
