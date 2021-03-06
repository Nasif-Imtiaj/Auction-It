from django.views.generic import TemplateView

from core.forms import ItemForm
from core.models import Item

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'center/home.html'

class OnAuctionTemplateView(TemplateView):
    template_name = 'center/on_auction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'on_auction_nav': 'active',
            'items': Item.objects.all()
        })
        return context