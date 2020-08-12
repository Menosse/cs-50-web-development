from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("register", views.register, name="register"),
    path("auction/<int:auction_id>", views.auctionListing, name="auction_listing"),
    path("auction/<int:auction_id>/bid", views.placeBid, name="place_bid"),
    path("auction/<int:auction_id>/close", views.closeListing, name="close_listing"),
    path("auction/<int:auction_id>/comment", views.addComment, name="add_comment"),
]
