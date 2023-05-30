import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.freesmtpservers.com', 25)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("smtp.freesmtpservers.com")
 
# message to be sent
message = "asdadfgsa"
 
# sending the mail
s.sendmail("smtp.freesmtpservers.com", "jaykumar.bano@gmail.com", message)
 
# terminating the session
s.quit()