from django import forms

class ContatoForm(forms.Form):
    nome = 'Nome'
    max_length = 100
    widget = forms.TextInput(attrs={'class': 'mt-1 block w-full p-2 bg-gray-700 border border-gray-600 rounded-md text-gray-100 focus:border-orange-500 focus:border-orange-500',
                                    'placeholder': 'seu.email@exemplo.com'})

    mensagem = forms.CharField(label='Mensagem', max_length=500, widget=forms.Textarea(attrs={'class': 'mt-1 block w-full p-2 bg-gray-700 border border-gray-600 rounded-md text-gray-100 focus:border-orange-500 focus:border-orange-500',
                                    'placeholder': 'Digite sua mensagem aqui...'}))