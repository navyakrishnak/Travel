from django.shortcuts import render
from . models import products
# Create your views here.
def stat(request):
    obj=products.objects.all()
    return render(request,"index.html",{'result':obj})