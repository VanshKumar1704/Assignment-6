def Perfect(num):
    if num <= 0:
        print('Enter a natural no.')
        return False

    divs = []
    for i in range(num ,0 ,-1):
        if num%i==0: divs.append(i)
    if num*2==sum(divs): return True
    else: return False

a = int(input('Enter a number: '))
if(Perfect(a)) :print('Perfect')
else: print('Not Perfect')
