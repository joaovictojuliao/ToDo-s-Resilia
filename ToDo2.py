populacao = int(input("Digite a população da cidade : "))
margemErro= float(input("Digite margem de erro esperada de (0 a 100%) "))

margemErro=margemErro/100
amostra = (6.6564*0.25)/(margemErro*margemErro)/(1+((6.6564*0.25)/((margemErro*margemErro)*populacao)))
amostraFinal=amostra//1

print("O tamanho da amostra é de : ", amostraFinal)
