from django.shortcuts import render
from .forms import CepForm
import requests

def consulta_cep(request):
    resultado = None # inicia a variavel com o armazenamento dos dados consultados
    erro = None # inicia a variavel com o armazenamento dos erros

    if request.method == 'POST': # Verifica a requisição
        form = CepForm(request.POST) # Cria uma instancia do formulario CepForm com os dados recebidos via POST 
        if form.is_valid(): # Verifica a validade das informações conforme parametros do Django
            cep = form.cleaned_data['cep'] # Obtem o valor do campo CEP
            cep = cep.replace(".", "").replace("-", "").replace(" ", "") # Replace de caracteres indesejados

            if len(cep) == 8: # Antes da requisição, verifica se o campo tem 8 caracteres.
                link = f'https://viacep.com.br/ws/{cep}/json/' # Monta a URL para a API do ViaCEP, substituindo {cep} pelo CEP fornecido
                requisicao = requests.get(link) # Requisição montada conforme API
                if requisicao.status_code == 200: # Se a requisição reotornar status 200 
                    dic_requisicao = requisicao.json() # Converte a resposta em JSON
                    if 'erro' not in dic_requisicao: # Verificação de erro no retorno da API do VIACEP
                        resultado = {
                            'cep': dic_requisicao['cep'],
                            'rua': dic_requisicao['logradouro'],
                            'bairro': dic_requisicao['bairro'],
                            'cidade': dic_requisicao['localidade'],
                            'uf': dic_requisicao['uf'],
                        } # Se não ha erro, extrai as informações do JSON
                    else:
                        erro = "CEP não encontrado" # Caso o CEP foi invalido 
                else:
                    erro = "Erro na requisição ao ViaCEP" # Caso o retorno foi diferente de 200
            else:
                erro = "CEP inválido" # Caso o CEP for digitado com menos de 8 caracteres
    else:
        form = CepForm()

    return render(request, 'consulta_cep/consulta.html', {'form': form, 'resultado': resultado, 'erro': erro}) # Renderiza o HTML com o formulario, resultado e erros