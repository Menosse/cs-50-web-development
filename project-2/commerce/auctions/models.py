from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class User(AbstractUser):
    pass

class Category(models.Model):
    code = models.CharField(max_length=3)
    description = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.description}"

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    starting_bid = models.FloatField()
    auctionlisting_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="auctionlisting_user")
    auctionlisting_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, related_name="auctionlisting_category")
    def __str__(self):
        return f"{self.title} {self.description} {self.starting_bid}"


class Comment(models.Model):
    title = models.CharField(max_length=64)
    comment_content = models.CharField(max_length=256)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="comment_user")
    comment_auctionlisting = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, blank=False,  related_name="comment_auctionlisting")
    def __str__(self):
        return f"{self.title} {self.comment_content}"

class Bid(models.Model):
    value = models.FloatField()
    starting = models.BooleanField(max_length=64)
    bid_date = models.DateTimeField(max_length=64,)
    bid_auctionlisting = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, blank=False,  related_name="bid_auctionlisting")
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name="bid_user")
    def __str__(self):
        return f"{self.value} {self.starting} {self.bid_date}"

class WatchList(models.Model):   
   watchlist_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, related_name="watchlist_user")
   watchlist_item = models.ManyToManyField(AuctionListing, blank=True, related_name="watchlist_item")
   def __str__(self):
       return f"{self.watchlist_user} {self.watchlist_item}"

class AuctionListingForm(forms.Form):
    title = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control','autofocus':'autofocus'}))

    description = forms.CharField(
        max_length=256,
        widget=forms.Textarea(
        attrs={'class': 'form-control', "rows": "3"}))

    starting_bid = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', "min" : "0"}))

    auctionlisting_category = forms.ChoiceField(
        label='Category',
        choices=Category.objects.all().values_list("id", "description"),
        widget=forms.Select(attrs={'class': 'form-control'})
        )
