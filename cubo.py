#Algoritimo para achar a raíz cúbica perfeita
x=int(input('Insira um número inteiro: '))
ans = 0
while ans**3 < abs(x):
    ans=ans+1
if ans**3 != abs(x):
    print (x, 'não é um cubo perfeito.')
else:
    if x<0:
        ans=-ans
    print ('A raíz cúbica de ' + str(x) + ' é ' + str(ans)+'.')
