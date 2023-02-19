from django.views import generic
from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Shelter,Dog
from django.urls import reverse_lazy

# Create your views here.
#def shelter_list(request):
#    shelters = Shelter.objects.all()
#    context = { 'shelters': shelters }
#    return render(request, 'shelter_list.html', context)

class ShelterListView(generic.ListView):
    template_name = 'shelter_list.html'
    context_object_name = 'shelters'

    def get_queryset(self):
        return Shelter.objects.all()


def index(request):
    return HttpResponse('fdkmfdo')


def shelter_detail(request, pk):
    shelter = get_object_or_404(Shelter, pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)

class DogDetailView(generic.DetailView):
    model = Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'

class DogCreateView(generic.CreateView):
    model = Dog
    template_name = 'dog_form.html'
    fields = ['name', 'description', 'shelter']

class DogUpdateView(generic.CreateView):
    model = Dog
    template_name = 'dog_form.html'
    fields = ['name', 'description', 'shelter']

