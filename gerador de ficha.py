import random
input('aperte qualquer tecla para gerar um personagem')
classe = ('assasino','Mago','Guerreiro Arcano',)
pontos = 80
calcular = 0

while True:
    print(f'classe {random.choices(classe)}')
    
    calcular = random.randint(1, 19)
    mod = (calcular - 10)//2
    total = pontos - calcular
    print(f'for: {calcular} ({mod:.0f})')
    calcular = random.randint(1,19)
    mod = (calcular - 10) //2
    total = pontos - calcular
    print(f'des: {calcular} ({mod:.0f})')
    calcular = random.randint(1,19)    
    mod = (calcular - 10)//2
    total = pontos - calcular
    print(f'res: {calcular} ({mod:.0f})')
    calcular = random.randint(1,19)
    mod = (calcular - 10)//2
    total = pontos-calcular
    print(f'int: {calcular} ({mod:.0f})')
    calcular = random.randint(1,19)
    mod = (calcular-10)//2
    total = pontos-calcular
    print(f'car: {calcular} ({mod:.0f})')
    calcular = random.randint(1, 19)
    mod = (calcular-10)//2
    total = pontos-calcular
    print(f'sab: {calcular} ({mod:.0f})')
    calcular = random.randint(1,19)
    mod = (calcular-10)//2
    total = pontos-calcular
    print(f'vig: {calcular} ({mod:.0f})')
    
    x = input('quer sair [s/n]').upper
    if x in 'S':
        break
    else:
        print('')