import random
# list of number 1-49
list_numbers = list(range(0, 50))
# shuffeling list
random.shuffle(list_numbers)
#taking six numbers from shuffled list
drawn_list = list_numbers[0:6]
#sorting list
drawn_list.sort()

separator = "','"
user_list = [input(f"Guess SIX numbers 1-49, write numbers using {separator} to seperate them:")]
