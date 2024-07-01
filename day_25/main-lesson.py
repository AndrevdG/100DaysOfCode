# with open("./weather_data.csv") as import_data:
#     data = import_data.readlines()
#     print(data)

# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temparatures = []
#     for row in data:
#         if row[1] != "temp":
#             temparatures.append(int(row[1]))
#     print(temparatures)

import pandas

# data = pandas.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp, 2))

# print(data["temp"].max())

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# temp_in_fahrenheit = monday.temp[0] * 9 / 5 + 32
# print(temp_in_fahrenheit)


# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")
