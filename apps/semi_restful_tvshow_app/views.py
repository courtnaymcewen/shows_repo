from django.shortcuts import render, redirect
from .models import *

def all_shows(request):
    a_shows = Show.objects.all()
    context = {
        'a_shows' : a_shows
    }
    return render(request, "semi_restful_tvshow_app/all_shows.html", context)

def new_show(request):#shows the form
    print ('new_tvshow')
    return render(request, "semi_restful_tvshow_app/new_show.html")

def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show' : show
    }
    return render(request, "semi_restful_tvshow_app/edit_show.html", context)

def show_detail(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show' : show
    }
    return render(request, "semi_restful_tvshow_app/show_detail.html", context)

def create_show(request): #processing behind the scenes adds info to database
    print ('new_tvshow')
    print (f'request:{request}')
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    show = Show.objects.last()
    show.save()
    return redirect(f'/show/{show.id}')

def update_show(request, show_id): #processing behind the scenes adds info to database
    show = Show.objects.get(id=show_id)
    print ("*************************************", request.POST)
    # print (f'{request.POST["title"]}')
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.description = request.POST['description']
    show.release_date = request.POST['release_date']
    show.save()
    context = {
        'show' : show
    }
    return redirect(f'/show/{show.id}')

def destroy_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect(f'/show') 
# sample
# def index(request):
#     context = {
#         "all_books": Book.objects.all(),
#         "all_authors": Author.objects.all(),
#     }
#     return render(request, "book_authors_app/index.html", context)