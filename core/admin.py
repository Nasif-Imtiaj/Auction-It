from django.contrib import admin

from core.models import Item
from core.models import auction_table, AuctionItem, Category

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'section']

@admin.register(auction_table)
class auction_tableAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_name', 'item_name', 'category','timestamp']

@admin.register(AuctionItem)
class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'name', 'category','date_posted']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp']