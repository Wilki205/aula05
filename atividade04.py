i = 1
soma = 0
a = int(input("Qantidade de alunos: "))
while i <= a:
    n = float(input("Digite nota: "))
    soma += n
    i = i + 1
media = soma/a
print(media)