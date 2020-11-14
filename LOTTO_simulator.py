import random
# list of number 1-49
list_numbers = list(range(1, 50))
# shuffeling list
random.shuffle(list_numbers)
#taking six numbers from shuffled list
drawn_list = list_numbers[0:6]
#sorting list
drawn_list.sort()


final_user_list= []

while True:
    try:
        separator = "','"
        user_list = (input(f"Guess SIX numbers 1-49, write numbers using {separator} to seperate them:"))
        split_user_list = user_list.split(',')
        split_user_list = [int(i) for i in split_user_list]
        [final_user_list.append(x) for x in split_user_list]

    except ValueError:
        print("One or more arguments is not integer")

    break

final_user_list.sort()
wynik = 0

for liczba in final_user_list:
    if final_user_list.count(liczba)>1:
        print(f"Number {liczba} duplicated")
        break
    elif liczba not in range(0,50):
        print(f'Number {liczba} is not in range  1-49')
        break
    else:
        if drawn_list.count(liczba)==1:
            wynik += 1

if  final_user_list == []:
        print("Nie wprowadziłeś poprawnie liczb")
elif len(final_user_list) != 6:
    print("< 6 elements")
    pass
else:
    print(f'Your numbers {final_user_list}, \nDrawn numbers {drawn_list}\nYou guessed #{wynik}# of them !')


