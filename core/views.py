from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView
from django.db.models import Q
from core.forms import ItemForm
from core.models import Item, Category, AuctionItem


class UpdateActiveTimeMixin:
    def get(self, request, *args, **kwargs):
        if request.user:
            request.user.profile.last_active = timezone.now()
            request.user.profile.save()
        return super().get(request, *args, **kwargs)


class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categorys' : Category.objects.all(),
            'home_nav': 'active'
        })
        return context

class MembersListView(ListView):
    template_name = 'core/members.html'
    model = User
    context_object_name = 'members'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update({
            'members_nav': 'active'

        })
        return context


    paginate_by = 10


class AboutTemplateView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'about_nav': 'active'

        })
        return context





class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name = 'core/item_form.html'
    success_url = '/'


def is_valid_queryparam(param):
    return param != '' and param is not None

def BootstrapFilterView(request):
    qs = AuctionItem.objects.all()
    title_contains_query = request.GET.get('title_contains')
    owner_contains_query = request.GET.get('owner_contains')
    category = request.GET.get('category')
    published_Date = request.GET.get('published_Date')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(name__icontains=title_contains_query)

    if is_valid_queryparam(owner_contains_query):
        qs = qs.filter(owner__username__icontains=owner_contains_query)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(category=category)

    if is_valid_queryparam(published_Date):
        qs = qs.filter(date_posted__date=published_Date)





    context = {
        'queryset': qs,
        'categories': Category.objects.all(),
        'search_nav': 'active'
    }
    return render(request, 'core/search.html', context)