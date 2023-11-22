from django import forms
from django.utils import timezone
from .models import AgendamentoLivro
from django.core.exceptions import ValidationError

class AgendamentoLivroForm(forms.ModelForm):
    class Meta:
        model = AgendamentoLivro
        fields = ['data_agendamento']
        widgets = {
            'data_agendamento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_data_agendamento(self):
        data_agendamento = self.cleaned_data['data_agendamento']
        # Obtém a data atual
        data_atual = timezone.now().date() 
        # Calcula a data limite (dois dias a partir da data atual)
        data_limite = data_atual + timezone.timedelta(days=2)

        if data_agendamento > data_limite:
            raise ValidationError("A data de agendamento deve ser no maximo dois dias após a data atual.")
        if data_agendamento < data_atual:
            raise ValidationError('A data não pode ser menor que a data atual')
        if data_agendamento == data_atual:
            raise ValidationError('A data não pode ser igual a data atual')
        return data_agendamento