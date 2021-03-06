from django.views.generic import TemplateView, CreateView

from core.forms import ItemForm
from core.models import Item
from core.forms import AuctionTableForm
from core.models import auction_table

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'center/home.html'

class OnAuctionTemplateView(TemplateView):
    template_name = 'center/on_auction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'on_auction_nav': 'active',
            'items': auction_table.objects.all()
        })
        return context

class AuctionTableCreateView(CreateView):
    form_class = AuctionTableForm
    template_name = 'center/create_product.html'
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'create_product_nav': 'active',
        })
        return context