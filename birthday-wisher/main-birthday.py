
"""
Aim:
    Check if someone has birthday today and send email.

Args:
    data : pull the data from birthdays.txt
    now: present date and time
    day: extract just day value from "now" variable


Returns:
    Sends email via gmail smtp
"""


import datetime as dt
import pandas as pd
import random
import smtplib

# -----Import data from txt file.
data = pd.read_csv("birthday-wisher/birthdays.txt")

# Grab today's date and time.
now = dt.datetime.now()
day = now.day
month = now.month
month_day = (month, day)

# ------ Email variables -----#

my_email = "pythonmail@sloka.co.nz"
my_password = "Today@123"
to_email = "sloka.thati@gmail.com"

# Convert data to dictionary

data_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if month_day in data_dict:
    # file_path = f"temp{random.randint(1, 3)}.txt"
    file_path = "temp4.txt"

    with open("birthday-wisher/templates/"+file_path) as file_content:
        file_data = file_content.read()
        file_data = file_data.replace("[name]", data_dict[month_day]["name"])
        print(file_data)

    with smtplib.SMTP("smtp.gmail.com") as birthday_email:
        birthday_email.starttls()
        birthday_email.login(user=my_email, password=my_password)
        birthday_email.sendmail(
            from_addr = my_email,
            to_addrs = to_email, 
            msg=f"Subject: I love you {data_dict[month_day]['name']}!!\n\n{file_data}"
        )

# for i in data_dict:
#     if i == month_day:
#         print(data_dict[i]["email"])

# day_lst = data['day']

# for i in day_lst:
#     if i == day:
#         print(data[data.day == i])
