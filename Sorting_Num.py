
user_input = input("Enter numbers separated by spaces: ")


numbers = list(map(int, user_input.split()))


numbers.sort()


print("Sorted list in ascending order:", numbers)
