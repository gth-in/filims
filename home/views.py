from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from.models import filims,details

def base(request):
    myfil=filims.objects.all().values()
    template=loader.get_template("base.html")
    context={
        "myfil": myfil,
             }
    return HttpResponse(template.render(context,request))
# Create your views here.
def detailed (request,id):
    det= details.objects.get(id=id)
    context={
        5:det
    }
    template=loader.get_template("detail.html")
    return HttpResponse(template.render(context,request))
def upload(request):
    if request.method=="POST":
        name=request.POST.get('name')
        genre=request.POST.get('genre')
        rating=request.POST.get('rating')
        image=request.POST.get('file')
        about=request.POST.get('about')
        director=request.POST.get('director')
        mod=filims(name=name,genre=genre,rating=rating,image=image)
        mod2=details(about=about,director=director)
        mod.save()
        mod2.save()
        print(mod)
        return redirect('/')
    template=loader.get_template("upload.html")
    return HttpResponse(template.render({}, request))
