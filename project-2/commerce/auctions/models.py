from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.timezone import now


class User(AbstractUser):
    pass

class Comment(models.Model):
    title = models.CharField(max_length=64)
    comment_content = models.CharField(max_length=256)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="comment_user")
    def __str__(self):
        return f"{self.title} {self.comment_content}"

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    starting_bid = models.FloatField()
    auctionlisting_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="auctionlisting_user")
    def __str__(self):
        return f"{self.title} {self.description} {self.starting_bid}"

class Bid(models.Model):
    value = models.FloatField()
    starting = models.BooleanField()
    date = models.CharField(max_length=64)
    bid_auctionlisting = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, blank=True,  related_name="bid_auctionlisting")
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="bid_user")
    def __str__(self):
        return f"{self.value} {self.starting} {self.date}"

class Category(models.Model):
    code = models.CharField(max_length=3)
    description = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.description} {self.code}"

class WatchList(models.Model):
    watchlist_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="watchlist_user")
    watchlist_item = models.ManyToManyField(AuctionListing, blank=True, related_name="watchlist_item")

    def __str__(self):
        return f"{self.watchlist_user} {self.watchlist_item}"