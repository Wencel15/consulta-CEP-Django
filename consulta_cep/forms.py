from django import forms

# Define uma classe CepForm que herda de forms.Form, que é um formulario baseado na classe form
class CepForm(forms.Form):
    cep = forms.CharField(label='CEP', max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Digite o CEP'}))
    
    # forms.CharField indica que cep é um campo de texto simples 
    # Label 'CEP' define o rotulo do campo exibido no html
    # max_length=11 tamanho do campo considerando caracteres especiais xx.xxx-xxx
    # widget=forms.TextInput(attrs={'placeholder': 'Digite o CEP'} define o input no html com o testo impresso dentro do campo com placeholder