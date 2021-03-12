from django import forms

from core.models import Item, auction_table, Category, AuctionItem, Bets


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'section']

class AuctionTableForm(forms.ModelForm):
    class Meta:
        model = auction_table
        fields = ['owner_name', 'item_name', 'category']

class AuctionItemForm(forms.ModelForm):
    class Meta:
        model = AuctionItem
        fields = ['owner', 'name', 'category']

class BettersForm(forms.ModelForm):
    class Meta:
        model = Bets
        fields = ['item', 'better', 'amount']