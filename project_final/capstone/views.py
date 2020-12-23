from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
 
def blog_view(request):
    projects = Project.objects.all()
    return render(request, 'blog.html', {'projects':projects})
 
def detail_view(request, id):
    project = get_object_or_404(Project, id=id)
    photos = ProjectImage.objects.filter(project=project)
    return render(request, 'detail.html', {
        'Project':project,
        'photos':photos
    })

def list_projects(request):
    projects = Project.objects.all()
    projects = [p.serialize() for p in projects]
    return JsonResponse({'projects':projects})

def project_api(request, id):
    project = Project.objects.get(id=id)
    return JsonResponse(project.serialize())

def project_images_api(request, id):
    project = Project.objects.get(id=id)
    photos = ProjectImage.objects.filter(project=project)
    photos = [img.serialize() for img in photos]
    return JsonResponse({
        'project':project.name,
        'project_id':project.id,
        'photos':photos
    })

def intro_api(request,id=1):
    intro = Intro.objects.get(id=id)
    return JsonResponse(
        intro.serialize()
    )
'''
def intro_api(request):
    intro = Intro.objects.all()
    intro = [i.serialize() for i in intro]
    return JsonResponse({
        "intro":intro
    })
'''

def bio_api(request,id=1):
    bio = Bio.objects.get(id=id)
    return JsonResponse(
        bio.serialize()
    )
#def bio_api(request):
    #bio = Bio.objects.all()
    #bio = [b.serialize() for b in bio]
    #return JsonResponse({
    #    'bio': bio
    #})
    

def contact_api(request, id=1):
    contact = Contact.objects.get(id=id)
    return JsonResponse(
        contact.serialize()
    )
'''
def contact_api(request, id=1):
    contact = Contact.objects.get(id=id)
    contact = [c.serialize() for c in contact]
    return JsonResponse({
        'contact':contact
    })
'''