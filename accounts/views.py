from django.views.generic import TemplateView


from core.forms import AuctionTableForm
from core.models import auction_table

class StatusTemplateView(TemplateView):
    template_name = 'accounts/status.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

            'items': auction_table.objects.all()
        })
        return context

class ProfileTemplateView(TemplateView):
    template_name = 'accounts/profile.html'