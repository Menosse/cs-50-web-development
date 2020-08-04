from django.shortcuts import render, redirect, reverse
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
import markdown2
from . import util
from django.template import RequestContext
from .models import NewEntryForm, EditForm
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


def randomEntry(request):
    rand_choice = choice(util.list_entries())
    try:
        return HttpResponseRedirect(reverse("title", kwargs={'title': rand_choice }))
    except:
        error404view(request, Exception)

def showEntry(request, title):
    try:
        return render(request, "encyclopedia/title.html",{
            "content": markdown2.markdown(util.get_entry(title)),
            "entry": title
        })
    except:
        error_message = 'Click here to add an arcticle for'
        # return HttpResponseRedirect(reverse(error404view,kwargs={"entry": title, "text": error_message}))
        return render(request, "encyclopedia/page404.html", {"entry": title, "text": error_message})

def editEntry(request, title):
    entryContent = util.get_entry(title)
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("title", kwargs={'title': title }))
        else:
            return render(request, "encyclopedia/editpage.html",{
                "form": form,
                "entry": title
            })
    return render(request, "encyclopedia/editpage.html",{
        "form": EditForm(initial={'content': entryContent}), "entry": title
        })

def search(request):
    try:
        search_param = request.GET.get('q','')
        if util.get_entry(search_param):
            return HttpResponseRedirect(reverse("title", kwargs={'title': search_param }))
        else:
            search_string = []
            for search_found_item in util.list_entries():
                if search_param.upper() in search_found_item.upper():
                    search_string.append(search_found_item)

            return render(request, "encyclopedia/search.html", {
            "entries": search_string
        })
    except:
        return render(request, "encyclopedia/page404.html", Exception)
    

def error404view(request, exception):
    return render(request, "encyclopedia/page404.html", {})