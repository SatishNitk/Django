from django.shortcuts import render,redirect, get_object_or_404
from notepad.models import *
from notepad.forms import *

def create_view(request):
	form = NoteModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect('/')
	context = {
	 'form':form
	}	

	return render(request,"notepad/create.html",context)

def list_view(request):
	notes = Note.objects.all()
	context = {
	'object_list' : notes
	}
	return render(request,"notepad/list.html",context)

def delete_view(request, note_id):
	item_to_delete = Note.objects.filter(pk=note_id)
	if item_to_delete.exists():
		if request.user == item_to_delete[0].user: # check for user is the owner for this note to delete
			item_to_delete[0].delete()
	return redirect("/notes/list")


def update_view(request, note_id):
	unique_note = get_object_or_404(Note,id=note_id)
	form = NoteModelForm(request.POST or None, request.FILES or None, instance=unique_note)  # due to instance form will be pre populated with data
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect('/')
	context = {
	 'form':form
	}	

	return render(request,"notepad/create.html",context)


