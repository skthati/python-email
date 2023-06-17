import datetime as dt
import pandas as pd
import random

data = pd.read_csv("birthday wisher/birthdays.txt")


now = dt.datetime.now()

day = now.day
month = now.month

month_day = (month, day)

data_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if month_day in data_dict:
    file_path = f"temp{random.randint(1, 3)}.txt"

    with open("birthday wisher/templates/"+file_path) as file_content:
        file_data = file_content.read()
        file_data = file_data.replace("[name]", data_dict[month_day]["name"])
        print(file_data)


# for i in data_dict:
#     if i == month_day:
#         print(data_dict[i]["email"])

# day_lst = data['day']

# for i in day_lst:
#     if i == day:
#         print(data[data.day == i])