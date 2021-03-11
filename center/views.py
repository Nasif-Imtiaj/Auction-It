from django.views.generic import TemplateView, CreateView , UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from core.forms import AuctionTableForm, AuctionItemForm
from core.models import auction_table, AuctionItem

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'center/home.html'

class OnAuctionTemplateView(TemplateView):
    template_name = 'center/on_auction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'on_auction_nav': 'active',
            'items': AuctionItem.objects.all()
        })
        return context

class AuctionTableDetailView(DetailView):
    template_name = 'center/detail_product.html'
    model = AuctionItem



class AuctionTableCreateView(LoginRequiredMixin, CreateView):
    form_class = AuctionItemForm
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

class AuctionTableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = AuctionItemForm
    model = auction_table
    template_name = 'center/update_product.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user.username == item.owner_name:
            return True
        return False

class AuctionTableDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = auction_table
    success_url = '/'
    template_name = 'center/product_confirm_delete.html'
    def test_func(self):
        item = self.get_object()
        if self.request.user.username == item.owner_name:
            return True
        return False
