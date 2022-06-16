from django import forms
from core.models import NewUserTB

class update(forms.ModelForm):
    class Meta:
        model = NewUserTB
        fields = ('__all__')