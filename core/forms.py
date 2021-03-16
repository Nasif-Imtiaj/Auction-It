from django import forms
from django.utils.text import slugify

from core.models import Item, auction_table, Category, AuctionItem, Bets, Images


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
        fields = ['owner', 'name', 'category', 'location', 'color', 'model', 'description']

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('item','image',)


class BettersForm(forms.ModelForm):
    class Meta:
        model = Bets
        fields = ['amount']
