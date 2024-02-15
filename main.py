import random

print("Welcome to password generator")
num_symbol=int(input("How many symbol do you want in your password : "))
num_char=int(input("How many character do you want in your password : "))
num_int=int(input("How many numbers do you want in your password : "))

list_num=["1","2","3","4","5","6","7","8","9","0"]
list_char=["a","b","c"]
english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
list_symbol=["*","%","/","&","+","!","-","_"]
chosen_list=[]

password=[]
sum_len=num_char+num_int+num_symbol

i=0
while i < sum_len:
    if num_char>0:
        if random.randint(0,1)==1:
            password.append(random.choice(list_char))
        else:
            password.append(random.choice(list_char).upper())
        num_char-=1
        i+=1
    if num_int>0:
        password.append(random.choice(list_num))
        num_int-=1
        i += 1
    if num_symbol>0:
        password.append(random.choice(list_symbol))
        num_symbol-=1
        i += 1

random.shuffle(password)
generated_password=""
for char in password:
    generated_password=generated_password+char

print("Your generated password is created...")
print("Your generated password is :",generated_password)




