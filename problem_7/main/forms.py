from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import Name

class NameForm(BSModalForm):
    class Meta:
        model = Name
        fields = ['name', 'work', 'salary']