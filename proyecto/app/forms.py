from django import forms
from .models import Categoria,SubCategoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['descripcion']
        labels={'descripcion':'Descripción'}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    

class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model=SubCategoria
        fields=['categoria','descripcion']
        labels={
            'categoria':'Categorías',
            'descripcion':'Descripción'
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
