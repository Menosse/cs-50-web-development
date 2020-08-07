from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Category, AuctionListing, AuctionListingForm


def index(request):
    return render(request, "auctions/index.html")


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(redirect_field_name='', login_url='index')
def create_listing(request):
    if request.method == "POST":
        form = AuctionListingForm(request.POST)
        if form.is_valid():
            try:
                new_auction = AuctionListing(
                    title=form.cleaned_data["title"],
                    description=form.cleaned_data["description"],
                    starting_bid=float(form.cleaned_data["starting_bid"]),
                    auctionlisting_user=User.objects.get(pk=int(request.user.id)),
                    auctionlisting_category=Category.objects.get(pk=int(form.cleaned_data["auctionlisting_category"])))
                new_auction.save()
            except IntegrityError:
                return HttpResponseRedirect(reverse("index"))
        return render(request, "auctions/create_listing.html",{
            "message": "New Auction created!",
            "form": AuctionListingForm(),
            })
    else:
        return render(request, "auctions/create_listing.html",{
            "form": AuctionListingForm(),
        })