n = 30
for i in range(n):
    v= ''.join(map(lambda x:str(x%10), range(1,i+2)))
    print(f'{(v+v[-2::-1]): ^{n*2-1}}')
    