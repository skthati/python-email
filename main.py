import smtplib

my_email = "pythonmail@sloka.co.nz"
my_password = "Today@123"
to_email = "sandeep@thati.org"

with smtplib.SMTP("smtp.gmail.com") as email_connection:
    email_connection.starttls()
    email_connection.login(user=my_email, password=my_password)

    # message to be sent   
    # SUBJECT = "Hello from Python App"   
    # TEXT = "This email is from Python Mail."
    
    # message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    email_connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject: Test email \n\nThis is another way.")
    # email_connection.close()