# task 1
#using while loop to print out numbers from -5 to 5, without 0.


print('\n------------task 1 ----------------\n')
str_result = ""
num = -5
while num in range(-5,6): # loop through the range 
    if num == 0:# skip the 0
        num +=1
    
    
    str_result += str(num)+ " " # build the string
    num += 1
    
print(str_result)
# task 2
# iterates over given string and converts 
# the lower letters to capital letters and vice versa
print('\n------------task 2 Upper and lower letters----------------\n')

text = input('enter text: ')
i = 0

result_str = ""
while i < len(text): # converting the lower and upper case letters
    if text[i].isupper():
        
        result_str += text[i].lower()
    else:
        
        result_str += text[i].upper()
    i += 1
print(result_str)

# task 3
# using while loop, to calculate the average of n 
# integer numbers (input from the user). Input 0 (zero)
#  finishes entering numbers and prints out calculations

print('\n------------task 3 average of numbers----------------\n')
num_lst = []
num_to_avg = int(input('''Input few integers to calculate 
their average! \n Input 0 to exit!!! '''))

# as long as num_to_avg equal to 0 it will prompting for number
while num_to_avg != 0: 
    num_lst.append(num_to_avg)
    num_to_avg = int(input('Type a integer : '))

# compute the average and print it
print('the average is: ' , sum(num_lst)/len(num_lst)) 


# Task 4
#using while loop, to find indexes of 
# prompted character in the given text.

print('\n------------task 4 find a character----------------\n')

text = '''She came to me one morning
One lonely Sunday morning
Her long hair flowing in the mid-winter wind
I know not how she found me
For in darkness I was walking
And destruction lay around me from a fight I could not win'''

i = 0
char = input('What should be found? ')

while i < len(text):
    if text[i] == char:  # looping through the indices 
        print(f'Character {char} found at index {i}')  # printing the relevant indices
    i += 1
    


# Task 5
# using while loop, read (prompt) three numbers 
# (a,b,c) and check how many numbers between 
# a and b are divisible by c.
# Input 0 (zero) as a third number (divisor)
# finishes program and prints out the results.


print('\n------------task 5 find divisible numbers----------------\n')

temp_result = 0
start = int(input('enter start number: '))
end = int(input('enter end number: '))

divisor = int(input('enter divisor: '))

i=0
# multiplying the divisor with integers until end num has been reached
# (more efficient than looping through each number and dividing it to test) 
while  (temp_result + divisor) < end:
    temp_result = divisor * i
    print(f'{temp_result} is divisible by {divisor}')
    i += 1
    # printing the number of numbers
print(f'there is a total of {i} numbers')

