from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Note

def homePageView(request):
	notes = []

	if request.user.is_authenticated:
		return redirect('/notebookapp/list/' + str(request.user.id))

	return render(request, 'pages/index.html', {'notes': notes})

@login_required
#@csrf_protect
@csrf_exempt
def addView(request):
	new_note = request.POST.get('note')
	print(new_note)
	user = User.objects.get(username=request.user.username)
	newNote = Note.objects.create(name = user, body = new_note)
	newNote.save()

	return redirect('/notebookapp/list/' + str(user.id))

@login_required
def listView(request, user_id = ""):
    notes = []

    #username = request.user.username
    #
    #if request.user.is_authenticated:
        #notes = Note.objects.filter(name__username = username)

    if user_id != "":
        for note in Note.objects.raw("SELECT id, body FROM notebookapp_note WHERE name_id = " + user_id):
            notes.append(note)

    return render(request, 'pages/index.html', {'notes': notes})
