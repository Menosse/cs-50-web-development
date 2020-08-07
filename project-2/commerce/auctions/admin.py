from django.contrib import admin

from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("code","description",)

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Category,CategoryAdmin)
admin.site.register(WatchList)