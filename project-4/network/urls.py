
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    #API URL
    path("posts/<str:postkind>", views.posts, name="posts"),
    path("following", views.following, name="following"),
    path("user", views.user, name="user"),
    path("follower", views.follower, name="follower"),
    path("likes", views.likes, name="likes"),
    path("compose", views.compose_post, name="compose"),
    path("single_post/<int:post_id>", views.single_post, name="single_post"),
    path("single_post/content/<int:post_id>", views.single_post_content, name="single_post_content"),
    path("single_post/check_like/<int:post_id>", views.check_like_post, name="like_post"),
    path("profile/<str:user>", views.profile, name="profile"),
]
