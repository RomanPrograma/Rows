
string = input('enter str:  ')
alpha_count=0
number_count=0
for i in string:
    if i.isalpha():
        alpha_count +=1
    elif i.isdigit():
        number_count +=1
    else:
        print('bl')
print(alpha_count)
print(number_count)