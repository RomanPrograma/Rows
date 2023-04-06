string = input('enter string:  ')
src_symbol = input(' enter the symbol you are looking for:  ')
count = 0
for c in string:
    if c == src_symbol:
        count +=1
print(count)
