import random
while True:
    q = int(input('quantos dados?'))
    x = int(input('de quantos lados?'))
    for c in range(1,q+1):
        print('='*19)
        print(' '*8,random.randrange(x+1))
        print('=' * 19)
