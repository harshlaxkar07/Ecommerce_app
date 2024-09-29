from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views import View



def home(request):
    return render(request,'app/home.html')

def index(request):
    return render(request,'app/index.html')



class categoryView(View):
    def get(self,request,val):
        return render(request,'app/category.html', locals())



