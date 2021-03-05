from django.views.generic import TemplateView, CreateView

from core.forms import ItemForm
from core.models import Item


class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'home_nav': 'active',
            'items': Item.objects.all()
        })
        return context


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

