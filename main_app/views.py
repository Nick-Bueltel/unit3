from django.shortcuts import render, redirect
from .models import Item
from django.views.generic.edit import DeleteView
from django import forms
from .forms import ItemForm
from django.views.decorators.http import require_POST
# Create your views here.


def create(request):
    newform = ItemForm(request.POST)
    context = {'form': newform}
    if newform.is_valid():
        addedform = newform.save()
        

    return render(request, 'create.html', context,)

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html',{'items': items})
  
class DeleteItem(DeleteView):
    model = Item
    success_url = '/'
    
    