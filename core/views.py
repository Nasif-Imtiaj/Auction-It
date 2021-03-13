from django.utils import timezone
from django.views.generic import TemplateView, CreateView

from core.forms import ItemForm
from core.models import Item


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
            'home_nav': 'active'
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
