from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Boulder


class BoulderForm(ModelForm):
    class Meta:
        model = Boulder
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }
