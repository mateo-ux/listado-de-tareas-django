from django import forms
from .models import Tarea

class CrearTareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre','descripcion','estado']
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs = {'class': 'form-control'}),
            'estado': forms.RadioSelect(choices=[
                ('Pendiente.', 'Pendiente.'),
                ('En curso', 'En curso'),
                ('Terminada.', 'Terminada.'),
        ]),
        }
        verbose_name_plural = 'ModelNames'
        
        
class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)

