from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_view, name='blog'),
    path('project/<int:id>', views.project_api, name='project'),
    path('intro', views.intro_api, name='intro'),
    path('bio', views.bio_api, name='bio'),
    path('contact', views.contact_api, name='contact'),
    path('projectphotos/<int:id>', views.project_images_api, name='projectphotos'),
    path('<int:id>/', views.detail_view, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)