from django import forms

from .models import Bunk

class BunkCreateForm(forms.ModelForm):
    class Meta:
        model = Bunk
        fields = "__all__"
