import random
# list of number 1-49
list_numbers = list(range(1, 50))
# shuffeling list
random.shuffle(list_numbers)
#taking six numbers from shuffled list
drawn_list = list_numbers[0:6]
#sorting list
drawn_list.sort()


final_user_list = []

# applying elements, verifying
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
result = 0
# checking duplicates
for number in final_user_list:
    if final_user_list.count(number) > 1:
        print(f"Number {number} duplicated")
        break
# checking number in range 1-49
    elif number not in range(1,50):
        print(f'Number {number} is not in range  1-49')
        break
    else:
        if drawn_list.count(number) == 1:
            result += 1
# checking elements in user list (must be 6 elements)
if  final_user_list == []:
        print("Your numbers are incorrect ")
elif len(final_user_list) != 6:
    print("< 6 elements")
    pass
# printing results
else:
    print(f'Your numbers {final_user_list}, \nDrawn numbers {drawn_list}\nYou guessed #{result}# of them !')


