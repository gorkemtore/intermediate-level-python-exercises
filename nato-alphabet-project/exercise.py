# multiplied_list = [i*2 for i in range(1,5)]
# print(multiplied_list)

# names = ["Görkem", "Zehra", "Sezen", "Berfin", "Asude", "Sena", "Betül", "Aslıhan", "Aybüke", "Zeynep"]
# new_names = [name.upper() for name in names if len(name) > 5]
# print(new_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number**2 for number in numbers]
# print(squared_numbers)

# Instructions
# You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.

# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

# Example Output
# [2, 8, 34]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers = [n for n in numbers if n % 2 == 0]
# print(even_numbers)

# with open("./nato-alphabet-project/file1.txt") as file1:
#     numbers_1 = [int(n[0]) for n in file1.readlines()]

# with open("./nato-alphabet-project/file2.txt") as file2:
#     numbers_2 = [int(n[0]) for n in file2.readlines()]

# common_numbers = [n for n in numbers_1 if n in numbers_2]
# print(f"Common numbers : {common_numbers}")

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# result = {word:len(word) for word in sentence.split()}
# print(result)



weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day:(temp*9/5)+32 for day, temp in weather_c.items()}


print(weather_f)


