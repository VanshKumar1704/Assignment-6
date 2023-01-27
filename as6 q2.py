def Palin(phr):
    l1 = list(''.join(phr.split()))
    if l1 == list(reversed(l1)):  # can use [::-1] as well, however reversed faster
        return True
    else:
        return False


input = input('Enter a Phrase: ')
if Palin(input):
    print("Tis a palindrome. ")

else:
    print('Tis not.')
