from django.forms import ModelForm, Select
from django.forms.widgets import TextInput
from .models import Boulder, Tick


class BoulderForm(ModelForm):
    class Meta:
        model = Boulder
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }


class ColorSelect(Select):
    option_template_name = 'select_option.html'


class TickForm(ModelForm):
    class Meta:
        model = Tick
        fields = '__all__'
        widgets = {
            'boulder': ColorSelect(),
        }