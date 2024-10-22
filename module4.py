number_of_inputs = int(input("Enter N: "))
numbers = []

print("Enter " + str(number_of_inputs) + " numbers - ")

for i in range(number_of_inputs):
    numbers.append((int(input("Enter number: "))))

to_check = int(input("Enter the number to find:"))
found = -1
for i in range(number_of_inputs):
    if numbers[i] == to_check:
        found = i
print(found)
