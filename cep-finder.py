import json,requests,os

if os.name == 'nt':
    limpa = 'cls'
else:
    limpa = 'clear'

option = 1

while option == 1:
    os.system(limpa)
    print("#" * 20)
    print("##   CEP Finder   ##")
    print("## @rafaelfilholm ##")
    print("#" * 20)

    cep_input = input("\nDigite um CEP(apenas os dígitos): \n> ")

    query = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep_input))

    endereco = json.loads(query.content)

    cep = endereco["cep"]
    logradouro  = endereco["logradouro"].upper()
    complemento = endereco["complemento"].upper()
    bairro = endereco["bairro"].upper()
    localidade = endereco["localidade"].upper()
    uf = endereco["uf"].upper()
    ibge = endereco["ibge"]

    print("==> Endereço Encontrado!!! <==")
    print("CEP: {}".format(cep))
    print("LOGRADOURO: {}".format(logradouro))
    print("COMPLEMENTO: {}".format(complemento))
    print("BAIRRO: {}".format(bairro))
    print("LOCALIDADE: {}".format(localidade))
    print("UNIDADE FEDERATIVA: {}".format(uf))
    print("CÓDIGO IBGE DA CIDADE: {}".format(ibge))

    print("\nDeseja Pesquisa outro CEP?")
    option = int(input("1. Sim, limpar e pesquisar novamente.\n2. Não, sair.\n> "))

print("Finalizado!")
print("By @rafaelfilholm")