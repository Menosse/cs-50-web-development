from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Category, AuctionListing, Bid, Comment, WatchList
from .forms import AuctionListingForm, PlaceBid, AddComment

from datetime import datetime
from itertools import chain


def index(request):
    return render(request, "auctions/index.html",{
        "list": [item for item in AuctionListing.objects.all()],
    })


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
                    current_bid=float(form.cleaned_data["starting_bid"]),
                    bid_is_open = True,
                    auctionlisting_user=User.objects.get(pk=int(request.user.id)),
                    auctionlisting_category=Category.objects.get(pk=int(form.cleaned_data["auctionlisting_category"])))
                new_auction.save()
                new_bid = Bid(
                    value=float(form.cleaned_data["starting_bid"]),
                    starting=True,
                    bid_date=datetime.now(),
                    bid_auctionlisting = AuctionListing.objects.get(pk=new_auction.id),
                    bid_user=User.objects.get(pk=int(request.user.id))
                )
                new_bid.save()
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

def auctionListing(request, auction_id):
    auction_listing = AuctionListing.objects.get(pk=auction_id)
    bid_history = Bid.objects.filter(bid_auctionlisting=auction_id).all()
    comments = Comment.objects.filter(comment_auctionlisting=auction_id).all()
    if request.user == auction_listing.auctionlisting_winner and auction_listing.bid_is_open == False:
        auction_winner = "Contratulations! You won the auction!"
    else:
        auction_winner = None
    if request.user == auction_listing.auctionlisting_user and auction_listing.bid_is_open == True:
        listing_owner= auction_listing.auctionlisting_user
    else:
        listing_owner= None
    return render(request, "auctions/auction_listing.html",{
        "auction_listing": auction_listing,
        "bid_form": PlaceBid(),
        "bid_history": bid_history,
        "listing_owner": listing_owner,
        "auction_winner": auction_winner,
        "comment_form": AddComment,
        "comments": comments
        })

@login_required(redirect_field_name='', login_url='index')
def placeBid(request, auction_id):
    if request.method == "POST":
        auction_listing = AuctionListing.objects.get(pk=auction_id)
        bid_history = Bid.objects.filter(bid_auctionlisting=auction_id).all()
        comments = Comment.objects.filter(comment_auctionlisting=auction_id).all()
        user_bid = float(request.POST["place_bid"])
        if request.user  == auction_listing.auctionlisting_winner and auction_listing.bid_is_open == False:
            auction_winner = "Contratulations! You won the auction!"
        else:
            auction_winner = None
        if request.user == auction_listing.auctionlisting_user and auction_listing.bid_is_open == True:
            listing_owner= auction_listing.auctionlisting_user
        else:
            listing_owner= None
        if auction_listing.current_bid <= user_bid:
            auction_listing.current_bid = user_bid
            auction_listing.save()
            new_bid = Bid(
                value= user_bid,
                starting=False,
                bid_date=datetime.now(),
                bid_auctionlisting = auction_listing,
                bid_user=User.objects.get(pk=int(request.user.id))
            )
            new_bid.save()
        else:
            return render(request, "auctions/auction_listing.html",{
            "auction_listing": auction_listing,
            "bid_form": PlaceBid(),
            "bid_history": bid_history,
            "listing_owner": listing_owner,
            "auction_winner": auction_winner,
            "comment_form": AddComment,
            "comments": comments,
            "message": "The bid must be greater than the current price." 
            })
    return HttpResponseRedirect(reverse("auction_listing", args=(auction_listing.id,)))

@login_required(redirect_field_name='', login_url='index')
def closeListing(request, auction_id):
    if request.method == "POST":
        auction_listing = AuctionListing.objects.get(pk=auction_id)
        last_bid = Bid.objects.filter(bid_auctionlisting=auction_id).last()
        if auction_listing.bid_is_open == False:
            return HttpResponseRedirect(reverse("auction_listing", args=(auction_listing.id,)))
        else:
            auction_listing.bid_is_open = False
            auction_listing.winning_bid = last_bid.value
            auction_listing.auctionlisting_winner = last_bid.bid_user
            auction_listing.save()
    return HttpResponseRedirect(reverse("auction_listing", args=(auction_listing.id,)))

@login_required(redirect_field_name='', login_url='index')
def addComment(request, auction_id):
    if request.method == "POST":
        auction_listing = AuctionListing.objects.get(pk=auction_id)
        if auction_listing.bid_is_open == False:
            return HttpResponseRedirect(reverse("auction_listing", args=(auction_listing.id,)))
        else:
            new_comment = Comment(
                title=request.POST["Comment_title"],
                comment_content=request.POST["Comment_content"],
                comment_user=User.objects.get(pk=int(request.user.id)),
                comment_auctionlisting=AuctionListing.objects.get(pk=auction_id)
            )
            new_comment.save()
    return HttpResponseRedirect(reverse("auction_listing", args=(auction_listing.id,)))

@login_required(redirect_field_name='', login_url='index')
def watchlist(request):
    user_watchlist = WatchList.objects.get(watchlist_user=int(request.user.id))
    test = [item for item in user_watchlist.objects.all()]
    return render(request, "auctions/watchlist.html",{
        "watchlist": [1,2,3],
        "test": test
    })