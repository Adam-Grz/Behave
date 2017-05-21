import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "smarq@o2.pl"
toaddr = "adamg@cakesolutions.net"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Testing sending emails with Python"
 
body = "It worked!!"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "testresults"
attachment = open("testresults", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP_SSL('poczta.o2.pl', 465)
#server.starttls()
server.login(fromaddr, "XXXXX")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print "Email sent!"
