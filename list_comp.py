# The classes a student is registered for
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

# Make a list of only the ITEC classes
only_itec = [ c for c in classes_registered if c.startswith('ITEC')]
#only_itec = [ c.lower() for c in classes_registered if c.startswith('ITEC')] if you want all class names in lower case
print(only_itec)

# Record temperatures every day. Record -1 if not possible to take measurement.

high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

# make a list of only numbers that represent a valid temperature measurement
only_real_measurements = [ temp for temp in high_temps if temp != -1]
print(only_real_measurements)

temp_celsius = [(temp_f - 32) * 5 / 9 for temp_f in only_real_measurements ]
print(temp_celsius)

average = sum(temp_celsius) / len(temp_celsius)
# print('The average is ' + str(average))
print(f'The average is {average:.2f}C')

# list comprehension syntax (making a list from another list)
strings = ['pizza', 'Beyonce', 'cat']
lengths = [len(string) for string in strings]
print(lengths)


# other longer option
strings2 = ['pizza', 'Beyonce', 'cat']
lengths2 =[]

for string in strings2:
    length = len(string)
    lengths2.append(length)

print(lengths2)

numbers = [2, 4, 6]
plus_one = [ n+1 for n in numbers ]
print(plus_one)

# Python doesn't have contains() methods, use the in operator to see if a string contains a substring, or a list contains an item

listy = [0, 3, 4, 0, 22, 1]
non_zero = [n for n in listy if n != 0]
print(non_zero)


#Uppercase all food items, but only if it's pizza
foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [food.upper() for food in foods if 'pizza' in food]
print(pizzas)

new_numbers = [0, 10, 4, 0, 32]
numbers_doubled_no_zeros = [ n * 2 for n in new_numbers if n!=0 ]
print(numbers_doubled_no_zeros)