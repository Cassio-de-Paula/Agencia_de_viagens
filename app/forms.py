from typing import Any
from django import forms
from app.migrations.models.passageiro import Passageiro
from app.migrations.models.voo import Voo


class PassageiroForm(forms.ModelForm):
    class Meta:
        model = Passageiro
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(PassageiroForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs.update({"class": "form-control"})

class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = '__all__'
        widgets = {
            'partida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'chegada': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super(VooForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs.update({"class": "form-control"})


class AddPassageiroForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ['passageiro']
    
    def __init__(self, *args, **kwargs):
        super(AddPassageiroForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs.update({"class": "form-control"})

