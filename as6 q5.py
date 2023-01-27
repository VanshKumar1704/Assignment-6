def order(str1):
    if '-' not in str1 or ' ' in str1:
        print('Enter a valid value.')
        return
    str1 = str1.split('-')
    str1.sort()
    print('-'.join(map(str,str1)))

order(input('Enter string: '))
