from django.views.generic import TemplateView, CreateView , UpdateView, DetailView


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

class AuctionTableDetailView(DetailView):
    template_name = 'center/detail_product.html'
    model = auction_table



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

    def form_invalid(self, form):
        print("Here")
        return super().form_invalid(form)

class AuctionTableUpdateView(UpdateView):
    form_class = AuctionTableForm
    model = auction_table
    template_name = 'center/update_product.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()

