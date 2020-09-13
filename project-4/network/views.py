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
def posts(request, postkind):

    if postkind == "all":
        posts = Post.objects.all()
    elif postkind == "following":
        following = Following.objects.get(following=request.user)
        following_list = [user for user in following.following_list.all()]
        posts = Post.objects.filter(user__in=following_list)
    else:
        return JsonResponse({"error": "Invalid path."}, status=400)
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

@csrf_exempt
@login_required
def single_post(request, post_id):
    
    # FIND REQUESTED POST
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
    
    # GET - SHOW SINGLE POST BASED ON POST ID
    if request.method == "GET":
        return JsonResponse(post.serialize())

    # PUT - ADD LIKE TO SINGLE POST BASED ON POST ID
    elif request.method == "PUT":
        #data = json.loads(request.body)
        #if data.get("num_likes") is not None:
        
        #increase post likes
        post.num_likes += 1
        post.liked_by_user.add(request.user)
        post.save()

        #register like
        like = Like(
            user = request.user,
            post = post,
            currently_like = True,
        )
        like.save()
        return HttpResponse(status=204)
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)

def check_like_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
    if request.user in post.liked_by_user.all():
        return JsonResponse({"post_liked_by_user": True})
        #return True
    else:
        return JsonResponse({"post_liked_by_user": False})
        #return False