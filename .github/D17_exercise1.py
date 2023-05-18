print('\n------------task 1----------------\n')

usr_inp = None

while usr_inp is None or not usr_inp.isdigit(): 
    try: 
        usr_inp = input('please enter a number: ' )

    except ValueError:
        print('error- please enter a number')
    
usr_inp = int(usr_inp)

for i in range(1, 11):
    result = usr_inp * i
    print(f"{usr_inp} x {i} = {result}")


print('\n------------task 2----------------\n')

for num in range(1,10):
    print(str(num)  * num)

print('\n------------task 3----------------\n')

usr_inp = None
result = []

word = input('please enter a String: ' )

for i in range(len(word)-1,-1,-1):
    result.append(word[i])
    

print("".join(result))

print('\n------------task 4----------------\n')


result = ""

sentence  = input('please enter a String: ' )

for i in range(len(sentence)):
    if sentence[i] == 'o':
        result += 'O'
    else:
        result += sentence[i]
    
print(result)

print('\n------------task 5----------------\n')

num_dig = 0
num_char = 0
num_other = 0

usr_str = input('Please enter a string of letters and digits: ')

for i in range(len(usr_str)):
    if usr_str[i].isalpha() and not usr_str[i].isdigit():
        num_char += 1
    
    elif usr_str[i].isdigit():
        num_dig += 1
    else:
        num_other +=1
        

print('number of digits: ', num_dig)
print('number of letters: ', num_char)
print('number of other chars: ', num_other)


