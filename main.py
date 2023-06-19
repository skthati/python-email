import smtplib

my_email = "pythonmail@sloka.co.nz"
my_password = "Today@123"
to_email = "nsd1026@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as email_connection:
    email_connection.starttls()
    email_connection.login(user=my_email, password=my_password)

    # message to be sent   
    # SUBJECT = "Hello from Python App"   
    # TEXT = "This email is from Python Mail."
    
    # message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    email_connection.sendmail(
        from_addr=my_email, 
        to_addrs=to_email, 
        msg="Subject: Dear Darling Swetha 1\n\nI love you."
    )
    # email_connection.close()
