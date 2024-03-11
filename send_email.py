import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "samyorangy1@gmail.com"
password = "rwovfcoibzpxungw"
receiver = "samyorangy1@gmail.com"
context = ssl.create_default_context()
message = """\
Subject: Test!
How are you?
I love you
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)