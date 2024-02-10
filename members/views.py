from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Member
from django.db.models import Q




# Create your views here.

# def members(request):
#     template=loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

def members(request):
     mymembers=Member.objects.all().values()
     template=loader.get_template('all_members.html')
     context={
          "members":mymembers,
     }
     return HttpResponse(template.render(context,request))

def details(request,id):
     mymember=Member.objects.get(id=id)
     template=loader.get_template('details.html')
     context={'mymembers' : mymember}
     return HttpResponse(template.render(context,request))

def main(request):
     template=loader.get_template('main.html')
     return HttpResponse(template.render())

#def testing(request):
 # template = loader.get_template('template.html')
 # mymember = Member.objects.all().values()
 # context = {
   # 'mymember': mymember,   
  #}
 # return HttpResponse(template.render(context, request))

#def testing(request):
  #template = loader.get_template('template.html')
  #context = {
  # 'var1': 'John',
  #}
  #return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def testing(request):
  mydata = Member.objects.filter(id__lte=5).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))