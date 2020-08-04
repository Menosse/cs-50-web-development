from django.shortcuts import render, redirect, reverse
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
import markdown2
from . import util
from django.template import RequestContext
from .models import NewEntryForm
from random import choice

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newEntry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) == None :
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("index"))
            else:
                exists = 'This entry already exists.'
                return render(request, "encyclopedia/newentry.html",{
                    "form": form, "exists": exists, "title": title
                })
        else:
            return render(request, "encyclopedia/newentry.html",{
                "form": form
            })
    return render(request, "encyclopedia/newentry.html",{
        "form": NewEntryForm()
        })

def showEntry(request, title):
    try:
        return render(request, "encyclopedia/title.html",{
            "title": markdown2.markdown(util.get_entry(title)),
            "title1": title
        })
    except:
        a = 'Click here to add an arcticle for'
        return render(request, "encyclopedia/page404.html", {
            "title": title, "text": a
        })

def randomEntry(request):
    try:
        return render(request, "encyclopedia/title.html",{
            "title": markdown2.markdown(util.get_entry(choice(util.list_entries()))),
        })
    except:
        error404view(request, Exception)

def editEntry(request, title):
    return render(request,"encyclopedia/editpage.html",{
        "title": title
    })


def error404view(request, exception):
    return render(request, "encyclopedia/page404.html", {})