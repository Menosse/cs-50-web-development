from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Intro)
admin.site.register(Bio)
#admin.site.register(Project)
admin.site.register(Contact)

class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage
 
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]
 
    class Meta:
       model = Project
 
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    pass