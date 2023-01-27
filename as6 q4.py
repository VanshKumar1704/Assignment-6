def Pangram(str1):

    start = ord('a')
    end = ord('z')
    #print(start)
    str1 = str1.lower()
    letters = list(map(str,''.join(str1.split())))
    #print(letters)
    for i in range(start, end + 1):
        if  chr(i) in letters: continue
        else: return False
    return True



if(Pangram(input())) : print('Pangram.')
else:print('not a Pangram.')
