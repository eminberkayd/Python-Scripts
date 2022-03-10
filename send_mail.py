"""
A basic Python script for sending mail
-Gmail servers limit the number of mail to sent by 500 in a day. 
Even if you try to send more than 500 mail in a day with infinity loop, it won't.
Also, this may lead to some bad circumstances such as tagging your mail
adress as spam and you might not use your mail adress 2-3 days.
So, be careful while using this.
"""

import smtplib
content = "The content" #Your mail content

mail = smtplib.SMTP("smtp.gmail.com",587) #check the documentation of smtplib for other mail sources
mail.ehlo() # to tell the gmail server we will use its server 
mail.starttls() # for encyrption 

mail.login("example@gmail.com","psw") #write your own mail adress and its password

for i in range(3): # you can increase this loop freely, but gmail will limit the number of mails with 500 in a day.

    mail.sendmail("source_mail","destination_mail", content)
