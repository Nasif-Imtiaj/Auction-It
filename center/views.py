from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, CreateView , \
    UpdateView, DetailView, DeleteView, ListView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from core.forms import AuctionTableForm, AuctionItemForm, BettersForm, ImageForm, FollowerForm, ReviewForm
from core.models import auction_table, AuctionItem, Category, Bets, Images, Follower, Review
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
            'on_auction_nav': 'active',
            'photos': Images.objects.all()
        })
        return context

    ordering = ['-date_posted']
    paginate_by = 5


class AuctionTableDetailView(DetailView):
    template_name = 'center/detail_product.html'
    model = AuctionItem
    form_class= BettersForm
    initial = {'key': 'value'}
    form_class = BettersForm
    form_class2 = ImageForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'photos' : Images.objects.filter(item=self.object.id),
            'bets': Bets.objects.filter(item=self.object.id),
            'form': self.form_class(),
            'form2': self.form_class2()
        })
        print(context, "context")
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('center:detail_product',pk=self.kwargs.get('pk'))
        else:
            return render(request, self.template_name, {'form': form})

        form2 = self.form_class2(request.POST, request.FILES)
        if form2.is_valid():
            form2.instance.item = AuctionItem.objects.get(id=self.kwargs.get('pk'))
            form2.save()
            return redirect('center:detail_product',pk=self.kwargs.get('pk'))
        else:
            return render(request, self.template_name, {'form': form})




class AuctionTableCreateView(LoginRequiredMixin, CreateView):
    template_name = 'center/create_product.html'
    success_url = reverse_lazy('center:my_items')
    initial = {'key': 'value'}
    form_class = AuctionItemForm

    def get(self, request, *args, **kwargs):

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.instance.owner = self.request.user
            form.save()

            return HttpResponseRedirect(reverse('center:my_items'))

        return render(request, self.template_name, {'form': form})










class AuctionTableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = AuctionItemForm
    model = AuctionItem
    template_name = 'center/update_product.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user.username == item.owner:
            return True
        return False



class AuctionTableDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AuctionItem
    success_url = reverse_lazy('center:my_items')
    template_name = 'center/product_confirm_delete.html'
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.owner:
            return True
        return






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

    def form_valid(self, form):
        form.instance.better = self.request.user
        form.instance.item = AuctionItem.objects.get(id=self.kwargs.get('pk'))
        form.save();
        return redirect('center:detail_product',pk=self.kwargs.get('pk'))

class BettersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bets
    success_url = reverse_lazy('center:my_bets')
    template_name = 'center/delete_bet_confirm.html'
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.better:
            return True
        return



class AddPicCreateView(LoginRequiredMixin, CreateView):
    form_class = ImageForm
    template_name = 'center/add_pic.html'
    success_url = 'center/detail_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

        })
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.item =AuctionItem.objects.get(id=self.kwargs.get('pk'))
            form.save()
            return redirect('center:detail_product',pk=self.kwargs.get('pk'))
        else:
            return render(request, self.template_name, {'form': form})



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
    context_object_name = "v_user"
    form_class = ReviewForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_follower'] = self.object.following.filter(followed_by=self.request.user).exists()
        context.update({
        'broughts' : Bets.objects.filter(better=self.kwargs.get('pk'), is_accepted=True),
        'solds' : Bets.objects.filter(item__owner=self.kwargs.get('pk'), is_accepted=True),
        'reviews' : Review.objects.filter(reviewed_to = self.kwargs.get('pk') ),
        'followings' : Follower.objects.filter(followed_by = self.request.user ),
        'form2': self.form_class()

        })
        return context

class ReviewListView(ListView):
    template_name = 'center/user_profile.html'
    model = Review
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

        })
        return context

    paginate_by = 10



class AcceptDealDetailView(RedirectView):
    def dispatch(self, request, *args, **kwargs):
        self.accept_deal(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        return reverse('center:detail_product', kwargs={'pk': self.kwargs.get('pk')})

    def accept_deal(self, request, *args, **kwargs):
        bet = Bets.objects.get(id=self.kwargs.get('bi'))
        bet.is_accepted = True
        bet.accepted_time = timezone.now()
        bet.save()
        item = AuctionItem.objects.get(id=self.kwargs.get('pk'))
        item.is_sold = True
        item.save()

class FollowersCreateView(LoginRequiredMixin, CreateView):
    template_name = 'center/create_follower.html'
    success_url = reverse_lazy('center:my_items')
    initial = {'key': 'value'}
    form_class = FollowerForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.instance.following = User.objects.get(id=self.kwargs.get('pk'))
            form.instance.followed_by = self.request.user
            form.save()

            return HttpResponseRedirect(reverse('center:user_profile', kwargs={'pk': self.kwargs.get('pk')}))

        return render(request, self.template_name, {'form': form})

class FollowersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'center/delete_follower_confirm.html'
    model = Follower
    success_url = reverse_lazy('center:my_bets')

    def test_func(self):
        item = Follower.get_object()
        if self.request.user == self.request.user:
            return True
        return False





class FollowersListView(ListView):
    template_name = 'center/followers_list.html'
    model = Follower
    context_object_name = 'followers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'members_nav': 'active'

        })
        return context

    paginate_by = 10

class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'center/create_review.html'
    success_url = reverse_lazy('center:my_items')
    initial = {'key': 'value'}
    form_class = ReviewForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.instance.reviewed_to = User.objects.get(id=self.kwargs.get('pk'))
            form.instance.reviewed_by = self.request.user
            form.save()

            return HttpResponseRedirect(reverse('center:user_profile', kwargs={'pk': self.kwargs.get('pk')}))

        return render(request, self.template_name, {'form': form})

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'center/delete_review_confirm.html'
    model = Review
    def get_success_url(self, **kwargs):
        item = self.get_object()
        return reverse('center:user_profile',kwargs={'pk' : item.reviewed_to.id})

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.reviewed_by:
            return True
        return False

