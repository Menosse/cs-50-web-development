from django import forms
from .models import Category, AuctionListing, Bid


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
    
    listing_pic = forms.FileField(label="Item Picture")

class PlaceBid(forms.Form):
    place_bid = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'min': "0", "placeholder" : "Bid"}))

class AddComment(forms.Form):
    Comment_title = forms.CharField(
        max_length=256,
        label='Title',
        widget=forms.TextInput(attrs={"class" : 'form-control'}))

    Comment_content = forms.CharField(
        max_length=256,
        label='Desciption',
        widget=forms.Textarea(attrs={"class" : 'form-control', "rows": "3"}))