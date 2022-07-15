contador=1
nCandidatos=int(input('São quantos candidatos : '))
listaCandidatos=[]
 
while contador<=nCandidatos:
    listaNotas=[]
    print(f'\n---Digite as notas do {contador}º candidato abaixo---')
    entrevista=int(input('Digite a nota da ENTREVISTA : '))
    testeTeorico=int(input('Digite a nota do TESTE TEORICO : '))
    testePratico=int(input('Digite a nota do TESTE PRÁTICO : '))
    soft=int(input('Digite a nota da AVALIAÇÃO SOFT SKILLS : '))
 
    listaNotas.append(entrevista)
    listaNotas.append(testeTeorico)
    listaNotas.append(testePratico)
    listaNotas.append(soft)
 
    listaCandidatos.append(listaNotas)
    contador=contador+1
 
def buscaCandidato():
    buscaListaNotas=[]
    ultimaLista=[]
   
    buscaEntrevista=int(input('\nDigite a nota que BUSCA da ENTREVISTA : '))
    buscaTesteTeorico=int(input('Digite a nota que BUSCA do TESTE TEORICO : '))
    buscaTestePratico=int(input('Digite a nota que BUSCA do TESTE PRÁTICO : '))
    buscaSoft=int(input('Digite a nota que BUSCA da AVALIAÇÃO SOFT SKILLS : '))
 
    buscaListaNotas.append(buscaEntrevista)
    buscaListaNotas.append(buscaTesteTeorico)
    buscaListaNotas.append(buscaTestePratico)
    buscaListaNotas.append(buscaSoft)
 
 
    for candidato in listaCandidatos:    
        if candidato[0] >= buscaListaNotas[0]:            
            if candidato[1] >= buscaListaNotas[1]:                
                if candidato[2] >= buscaListaNotas[2]:                    
                    if candidato[3] >= buscaListaNotas[3]:                        
                        ultimaLista.append(candidato)
    print(ultimaLista)                   
 
    return
buscaCandidato()
