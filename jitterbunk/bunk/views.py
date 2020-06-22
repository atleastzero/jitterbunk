from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

from .models import Bunk, UserProfile
from .forms import BunkCreateForm

class IndexView(generic.ListView):
    template_name = 'bunk/main_feed.html'
    context_object_name = 'bunk_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["users"] = UserProfile.objects.all()
        return context

    def get_queryset(self):
        """Return all bunks."""
        return Bunk.objects.order_by('-time_sent')[:20]

# class UserProfileView(generic.DetailView):
#     model = UserProfile
#     template_name = 'bunk/user_feed.html'
#     context_object_name = 'user'

#     def get_context_data(self, **kwargs):
#         context = super(UserProfileView, self).get_context_data(**kwargs)
#         bunks_recieved = Bunk.objects.filter(to_user=self.get_object())
#         bunks_sent = Bunk.objects.filter(from_user=self.get_object())
#         context["bunks_with_user"] = (bunks_recieved | bunks_sent).order_by('-time_sent')[:20]
#         return context

# Danielle's Note
def user_profile_view(request, username):
    bunks_recieved = Bunk.objects.filter(to_user=self.get_object())
    bunks_sent = Bunk.objects.filter(from_user=self.get_object())
    context = {
        'bunk_with_user' = (bunks_recieved | bunks_sent).order_by('-time_sent')[:20]
    }
    return render(request, 'bunk/user_feed.html', context)
    
class CreateBunkView(generic.CreateView):
    model = Bunk
    fields = "__all__"

    def get_success_url(self):
        return reverse('bunk:index')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
    else:
        reverse('bunk:login')
