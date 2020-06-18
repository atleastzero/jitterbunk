from django.views import generic

from .models import Bunk, UserProfile

class IndexView(generic.ListView):
    template_name = 'bunk/main_feed.html'
    context_object_name = 'bunk_list'

    def get_queryset(self):
        """Return all bunks."""
        return Bunk.objects.order_by('-time_sent')[:20]

class UserProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'bunk/user_feed.html'

    # def get_object(self, queryset=None):
    #     return self.kwargs['slug']

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        bunks_recieved = Bunk.objects.filter(to_user=self.get_object())
        bunks_sent = Bunk.objects.filter(from_user=self.get_object())
        context["bunks_with_user"] = (bunks_recieved | bunks_sent).order_by('-time_sent')[:20]
