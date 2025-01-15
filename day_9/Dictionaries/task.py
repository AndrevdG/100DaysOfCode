programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again"

empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit item in dictionary
programming_dictionary["Bug"] = "When a program is being prevented from running as expected"
print(programming_dictionary["Bug"])

for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")