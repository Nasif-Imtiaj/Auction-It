from django.views.generic import TemplateView, CreateView , UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from core.forms import AuctionTableForm, AuctionItemForm, BettersForm
from core.models import auction_table, AuctionItem, Category, Bets
from django.contrib.auth.models import User
# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'center/home.html'

class OnAuctionListView(ListView):
    template_name = 'center/on_auction.html'
    model = AuctionItem
    context_object_name = 'items'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'on_auction_nav': 'active'

        })
        return context
    ordering = ['-date_posted']
    paginate_by = 5


class AuctionTableDetailView(DetailView):
    template_name = 'center/detail_product.html'
    model = AuctionItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

            'bets': Bets.objects.filter(item=self.object.id)
        })
        return context



class AuctionTableCreateView(LoginRequiredMixin, CreateView):
    form_class = AuctionItemForm
    template_name = 'center/create_product.html'
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'create_product_nav': 'active',
            'categorys': Category.objects.all()
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




class BettersCreateView(LoginRequiredMixin, CreateView):
    form_class = BettersForm
    template_name = 'center/betters.html'
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'create_product_nav': 'active',

        })
        return context




class UserItemsListView(ListView):
    template_name = 'center/my_items.html'
    model = AuctionItem
    context_object_name = 'items'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'on_auction_nav': 'active'

        })
        return context
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return AuctionItem.objects.filter(owner=self.request.user)

class UserBetsListView(ListView):
    template_name = 'center/my_bets.html'
    model = Bets
    context_object_name = 'bets'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

        'bets': Bets.objects.filter(better=self.request.user)

        })
        return context
    ordering = ['-betted_time']
    paginate_by = 5



class PofileDetailView(DetailView):
    template_name = 'center/user_profile.html'
    model = User
