# Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["notkey"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[4]

# TypeError
# text = "abc"
# print(text + 5)

# FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} key does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed")
#     raise KeyError("Fake News!")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height higher than 3m is unlikely")

bmi = weight / height ** 2
print(f"bmi is {bmi}")
