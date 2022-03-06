# Practical Problem 4
# User have to enter different integer numbers or case sensitive strings and the program should display if the string
# is palindrome or not and in case of integers, the nearest next palindrome number have to be shown
user_list = []

list_size = int(input("Specify the number in integer only you want to take to find the next palindrome: "))
for i in range(list_size):
    user_list.append(input("Enter any integer or case-sensitive string: "))

print("\n")
for item in user_list:
    if item.isalpha():
        if item == item[::-1]:
            print(f"Your palindrome for {item} is {item}.")
        else:
            print(f"{item} is not a palindrome.")
    elif item.isnumeric():
        item_pal = int(item)
        while 1:
            if str(item_pal) == str(item_pal)[::-1]:
                print(f"The next palindrome for {item} is {item_pal}.")
                break
            else:
                item_pal += 1
                continue
