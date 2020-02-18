list = [8, 2, 9, 2, 1, 4, 6, 8, 9]
# digit = int(input("Enter Digit: "))
sqlist = [e**2 for e in list]  # List comprehension
print(list, "\n")
print(sqlist, "\n")

# Converting celcius to farenheit using list Comperihension
Celcius = [22, 1, 45, 24, 43, -1, 54, 6, 21]
F = [e*9/5+32 for e in Celcius]
print(Celcius, "\n")
print(F)
