# with open("./day-25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("./day-25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)

#import pandas

#data = pandas.read_csv(filepath_or_buffer="./day-25/weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# #print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean()) #gives to us avarage 

# print(data["temp"].max())
#print(data[data["day"] =="Monday"])
#print(data[data.day == "Monday"])

#print(data[data.temp == data["temp"].max()])

import pandas

data = pandas.read_csv(filepath_or_buffer="./day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count" : [black_squirrels_count, red_squirrels_count, grey_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./day-25/squirrel_count.csv")