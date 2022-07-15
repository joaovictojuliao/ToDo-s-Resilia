contadorAnalista=0
contadorCientista=0
dicionarioAnalista = {'analista de dados': ['python', 'powerbi', 'sql', 'boa comunicação']} 
dicionarioCientista = {'cientista de dados': ['python', 'banco de dados', 'machine learning', 'resolução de problemas', 'estatística']}
pessoas=dict()
listaPessoas=list()
listaAprovados=[]

print('\n----------Seja bem-vindo ao BuscaVagas----------')
numeroCandidatos=int(input('Digite a quantidade de candidatos: '))

for c in range(0, numeroCandidatos):
    pessoas['Nome: ']=str(input(f'Digite o nome do {c+1}º candidato: '))
    pessoas['Vaga: ']=str(input('Qual a vaga desejada: ')).lower()
    pessoas['Resumo: ']=str(input('Digite o resumo: ')).lower()
    listaPessoas.append(pessoas.copy())

    if pessoas['Vaga: '] in dicionarioAnalista:
        contadorAnalista+=1
        for i in dicionarioAnalista.values():
            for a in i:
                if a in pessoas['Resumo: ']:
                   listaAprovados.append(pessoas.copy()) 
            
    elif pessoas['Vaga: '] in dicionarioCientista:
        contadorCientista+=1
        for i in dicionarioCientista.values():
            for a in i:
                if a in pessoas['Resumo: ']:
                    listaAprovados.append(pessoas.copy())
print('\n--------------------LISTA DE TODOS OS CANDIDATOS--------------------')
for e in listaPessoas: 
    print(e)
print('\n--------------------PESSOAS INTERESSADAS EM CADA VAGA--------------------')
print(f'Numero de pessoas que se interessam na vaga de Analista de dados: {contadorAnalista}')
print(f'Numero de pessoas que se interessam na vaga de Cientista de dados: {contadorCientista}')
print('\n---------------PESSOAS QUE NO RESUMO TEM AS PALAVRAS CHAVES---------------')
for a in listaAprovados: 
    print(a)
