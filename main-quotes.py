import random
import datetime as dt
import pandas as pd
import smtplib

# ---------- Variables ----------#
my_email = "pythonmail@sloka.co.nz"
my_password = "Today@123"
to_email = "sandeep@thati.org"


# Find today's weekday

now = dt.datetime.now()

week_day = now.weekday()

# Send email if today's weekday is 5

if week_day == 5:
    # ------------ Read data from CSV ------ #

    with open("quotes.txt") as q_file:
        all_quotes = q_file.readlines()

    todays_quote = random.choice(all_quotes)

    print(todays_quote)

    # Send email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = to_email,
            msg = f"Subject: Today's Quote\n\n{todays_quote}"
        )

# End
