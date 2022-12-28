from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Note
from notebookapp.db import *

def homePageView(request):
	notes = []

	if request.user.is_authenticated:
		notes = Note.objects.filter(name__username = request.user.username)

	return render(request, 'pages/index.html', {'notes': notes})

@login_required
def addView(request):
	new_note = request.POST.get('note')
	print(new_note)
	user = User.objects.get(username=request.user.username)
	newNote = Note.objects.create(name = user, body = new_note)
	newNote.save()

	return redirect('/notebookapp/')
