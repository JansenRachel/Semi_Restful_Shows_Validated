from django.db import models
from django.shortcuts import redirect, render, HttpResponse
from . models import Show


def index(request):
    return redirect('/shows')

def display_all_shows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, "all_shows.html", context)


def add_show_form(request):
    return render(request, "create_show.html")

def delete_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')

def update_show(request, show_id):
    
    edit = Show.objects.get(id=show_id)
    edit.title = request.POST['title']
    edit.network = request.POST['network']
    edit.release_date = request.POST['release_date']
    edit.desc= request.POST['desc']
    print("Show has updated in db")
    edit.save()
    return redirect(f"/show_details/{edit.id}")


def create_new_show(request):
    show = Show.objects.create (title = request.POST['title'], release_date = request.POST['release_date'], desc = request.POST['desc'], network = request.POST['network'])
    return redirect(f"/show_details/{show.id}")


def display_show_info(request, show_id):
    context = {
        'shows' : Show.objects.get(id = show_id)
    }
    return render(request, "display_show_info.html", context)

def edit_show(request, show_id):
    show_edited = Show.objects.get(id=show_id)
    context = {
        'shows' : show_edited
    }
    return render(request, "edit_show.html", context)

