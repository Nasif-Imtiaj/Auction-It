from django.contrib import admin

from core.models import Item
from core.models import auction_table, AuctionItem, Category, Bets, Images

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'section']

@admin.register(auction_table)
class auction_tableAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_name', 'item_name', 'category','timestamp']

@admin.register(AuctionItem)
class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'name', 'category','date_posted', 'is_sold']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp']

@admin.register(Bets)
class ItemAdmin(admin.ModelAdmin):
    pass
@admin.register(Images)
class ItemAdmin(admin.ModelAdmin):
    pass