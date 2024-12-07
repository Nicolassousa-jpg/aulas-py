#LUCROS DA  EMPRESA

faturamento = 1000 #tipo: int

custo = 750.5 #se o numero for quebrado, usar PONTO ao inves de VIRGULA. isso fara dela uma variavel do tipo: float

novas_vendas = 100
faturamento = faturamento + novas_vendas


imposto = faturamento * 0.1

lucro = faturamento - custo - imposto

margem_de_lucro = lucro/faturamento

print("O faturamento do mes foi de:",faturamento, "R$")
print("O custo do mes foi de:",custo, "R$")
print("o lucro foi de:",round(lucro, 2), "R$")
print("A margem de lucro foi de:",round(margem_de_lucro, 2),)
print("tivemos um total de:",imposto, "em impostos")

# Mod -> % = resto da divisão, ou seja, 10/3 = 9, porem o numero restante da divisão é 1.

#exemplo pratico
tempo_contrato = 170 #fica dificil de fazer essa conta de cabeça e converter para meses ou anos, 

tempo_anos = tempo_contrato/12

print("tempo em anos",tempo_anos)
print("arredondando fica")
#o tempo disso dara em 14.1666666666666 anos, mas, quanto isso dara em meses? por isso do -> % <- 
#para complementar esse codigo e deixa-lo de melhor entendimento ao usuario iremos adicionar "int" antes de "tempo_anos". Isso ira pegar o numero inteiro desse resultado
# então vai ficar assim:
print("tempo em anos",int(tempo_anos))

#vamos ver isso em meses

tempo_meses = 170 % 12
print("tempo em meses",tempo_meses)
print("ou seja" ,int(tempo_anos),"anos e",tempo_meses, "meses")

# :)