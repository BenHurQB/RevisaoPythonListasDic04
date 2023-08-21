#5) Faça um programa que, ao inserir um número qualquer, criará uma lista contendo todos os números primos entre 1 e o número digitado.

n = int(input('Informe o número: '))
lista = []
primo = [2]
if n > 0:
  for elemento in range(1,n+1):
    lista.append(elemento)
  
  #testar cada elemento da lista e verificar se é primo
  
  for elemento in range(2,len(lista)):
    n = lista[elemento]
    divisor = 2
    achei = False
    while divisor <= n:
      if n % divisor == 0 and divisor < n:
        achei = True
        break
      divisor += 1
    if  not achei:
       primo.append(n)
  print(primo)  
else:
  print('Não existe número primo para números negativos ou igual a zero')