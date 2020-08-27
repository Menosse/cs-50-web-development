import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post, Like, Following, Follower

def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def posts(request):
    posts = Post.objects.all()
    posts = posts.order_by("-timestamp").all()
    return JsonResponse([post.serialize() for post in posts], safe=False)

@login_required
def following(request):
    following_list = Following.objects.get(following=request.user)
    return JsonResponse([following_list.serialize()], safe=False)

@login_required
def follower(request):
    follower_list = Follower.objects.get(follower=request.user)
    return JsonResponse([follower_list.serialize()], safe=False)

@login_required
def likes(request):
    likes_list = Like.objects.filter(user=request.user)
    return JsonResponse([like.serialize() for like in likes_list], safe=False)

@csrf_exempt
@login_required
def compose_post(request):
    # Composing a new post must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    try:
        # Create post
        data = json.loads(request.body)
        post = Post(
            user=request.user,
            body=data.get("post_body"),
            num_likes=0
        )
        post.save()
        return JsonResponse({"message": "Post made successfully."}, status=201)
    except IntegrityError as e:
        print(e)
        return JsonResponse({"message": f"internal error {e}."}, status=500)
    


