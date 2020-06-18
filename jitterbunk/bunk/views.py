from django.views import generic

from .models import Bunk

class IndexView(generic.ListView):
    template_name = 'bunk/index.html'
    context_object_name = 'bunk_list'

    def get_queryset(self):
        """Return all bunks."""
        return Bunk.objects.order_by('-time_sent')[:20]
