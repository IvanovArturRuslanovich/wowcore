from django.contrib import admin
from core.models import Item

from core.models import AuctionItemPrice, AuctionItemOrder

admin.site.register(Item)
admin.site.register(AuctionItemPrice)
admin.site.register(AuctionItemOrder)
