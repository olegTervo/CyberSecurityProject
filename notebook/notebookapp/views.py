from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Note
from notebookapp.db import *

def index(request):
	return HttpResponse("Wellcome")

@login_required
def listView(request):
	res = getlist2(request.user)

	return HttpResponse(res)

def homePageView(request):
	notes = []

	if request.user.is_authenticated:
		notes = Note.objects.filter(name__username = request.user.username)

	return render(request, 'pages/index.html', {'notes': notes})
