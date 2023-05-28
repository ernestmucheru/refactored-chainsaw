from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.

#Home
def home(request):
    all_tours = Tour.objects.all().order_by('-created_at')
    context = {
        'tours': all_tours
    }
    return render( request, 'home.html', context)

#Add Tour
def add_tour(request):
    if request.method == "POST":
        if request.POST.get('tour') \
            and request.POST.get('photos') \
            and request.POST.get('description') \
            and request.POST.get('blog') \
            or request.POST.get('price'):
            tour = Tour()
            tour.tour = request.POST.get('tour')
            tour.photos = request.POST.get('photos')
            tour.description = request.POST.get('description')
            tour.blog = request.POST.get('blog')
            tour.price = request.POST.get('price')
            tour.save()
            return HttpResponseRedirect('/')
    else:
        return render( request, 'add.html')

#View Tour Individually
def tour(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    if tour != None:
        context = {
            'tour': tour
        }
        return render(request, "edit.html" , context ) 

#Edit Tour
def edit_tour(request):
    if request.method == "POST":
        tour = Tour.objects.get(id = request.POST.get('id'))
        if tour != None:
            tour.tour = request.POST.get('tour')
            tour.photos = request.POST.get('photos')
            tour.description = request.POST.get('description')
            tour.blog = request.POST.get('blog')
            tour.price = request.POST.get('price')
            tour.save()
            return HttpResponseRedirect('/')

#Delete Tour
def delete_tour(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    tour.delete()
    return HttpResponseRedirect('/')