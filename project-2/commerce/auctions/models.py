from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class User(AbstractUser):
    pass

class Category(models.Model):
    code = models.CharField(max_length=3)
    description = models.CharField(max_length=64)

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    starting_bid = models.FloatField()
    current_bid = models.FloatField()
    bid_is_open = models.BooleanField()
    listing_pic = models.ImageField(null=True, blank=True)
    auctionlisting_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="auctionlisting_user")
    auctionlisting_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, related_name="auctionlisting_category")
    winning_bid = models.FloatField(blank=True, null=True)
    auctionlisting_winner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True, related_name="auctionlisting_winning_user")

class Comment(models.Model):
    title = models.CharField(max_length=64)
    comment_content = models.CharField(max_length=256)
    comment_date = models.DateTimeField(blank=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="comment_user")
    comment_auctionlisting = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, blank=False,  related_name="comment_auctionlisting")

class Bid(models.Model):
    value = models.FloatField()
    starting = models.BooleanField()
    bid_date = models.DateTimeField(max_length=64)
    bid_auctionlisting = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, blank=False,  related_name="bid_auctionlisting")
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="bid_user")

class SingleWatchList(models.Model):
    watchlist_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, related_name="watchlist_user")
    watchlist_item = models.ManyToManyField(AuctionListing,null=True, blank=True, related_name="watchlist_item")