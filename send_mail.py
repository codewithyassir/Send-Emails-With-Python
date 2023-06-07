import smtplib
from email.message import EmailMessage


# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 465
sender_email = ''
email_password = ''
recipient_email = ''


msg = EmailMessage()
msg['Subject'] = "Wesh Wesh achabab"
msg['From'] = sender_email
msg['To'] = recipient_email

msg.add_alternative("""
	<!DOCTYPE html>
	<html>
		<body>
			<h2 style="color:black;">Hey,</h2>
			<p>Test Email Sending with Python.</p>
			<h5 style="color:black;">Merci.</h5>
		</body>
	</html>
	""", subtype='html')

with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender_email, email_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print(f"Email sent successfully to {recipient_email}")

##############################################################################################


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 465
sender_email = ''
email_password = ''
recipient_email = ''


msg = MIMEMultipart()
msg['Subject'] = "Wesh Wesh achabab"
msg['From'] = sender_email
msg['To'] = recipient_email

html = """
	<!DOCTYPE html>
	<html>
		<body>
			<h2 style="color:black;">Hey,</h2>
			<p>Test Email Sending with Python.</p>
			<h5 style="color:black;">Merci.</h5>
		</body>
	</html>"""

html_part = MIMEText(html, 'html')
msg.attach(html_part)


with open('cv.pdf', 'rb') as my_file:
	cv = my_file.read()

pdf = MIMEApplication(cv, maintype='application/pdf', subtype='octet-stream')
pdf.add_header('Content-Disposition','attachment', filename=my_file.name)
msg.attach(pdf)


with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender_email, email_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print(f"Email sent successfully to {recipient_email}")

##############################################################################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 465
sender_email = ''
email_password = ''
recipient_email = ''


msg = MIMEMultipart()
msg['Subject'] = "Wesh Wesh achabab"
msg['From'] = sender_email
msg['To'] = recipient_email


with open('template.html', 'r') as html_file:
	html = html_file.read()

html_part = MIMEText(html, 'html')
msg.attach(html_part)


with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender_email, email_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print(f"Email sent successfully to {recipient_email}")
