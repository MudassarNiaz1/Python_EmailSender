import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


myEmail = "write your email address"
recipient_email = "write the email address to whom you send"  
smtp_server = 'smtp.gmail.com'
smtp_port = 587


msg = MIMEMultipart()
msg['From'] = myEmail
msg['To'] = recipient_email  
msg['Subject'] = 'write the message you wnat to send!'


body = 'This email was sent from Python with an attachment'
msg.attach(MIMEText(body, 'plain'))


file_path = ''  
file_name = ''  


with open(file_path, 'rb') as file:
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(file.read())
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', f'attachment; filename={file_name}')
    msg.attach(part)


try:
    
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  

    
    server.login(myEmail, "password generated from google app passwords.. if not create first.")

    
    server.sendmail(myEmail, recipient_email, msg.as_string())  
    print("Email Sent Successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()



















































# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders


# myEmail = "mrbeanamz@gmail.com"
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587


# msg = MIMEMultipart()
# msg['From'] = myEmail
# msg['To'] = myEmail
# msg['Subject'] = 'The subject of the email...'


# body = 'This email was sent from Python with an attachment'
# msg.attach(MIMEText(body, 'plain'))


# file_path = 'path_to_your_file_here'  
# file_name = 'your_attachment_filename'  


# with open(file_path, 'rb') as file:
    
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload(file.read())
#     encoders.encode_base64(part)  
#     part.add_header('Content-Disposition', f'attachment; filename={file_name}')
#     msg.attach(part)


# try:

#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()  

    
#     server.login(myEmail, "zbfcovevigovxhia")

#     # Send the email with the attachment
#     server.sendmail(myEmail, myEmail, msg.as_string())  
#     print("Email Sent Successfully!")
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     server.quit()




























# # msg = MIMEText('This email was sent from Python')
# # msg['Subject'] = 'The subject of the email...'
# # msg["From"] = myEmail
# # msg["To"] = myEmail

# # server = smtplib.SMTP(smpt_server, smtp_port)
# # server.starttls()
# # server.login(myEmail, "zbfcovevigovxhia")

# # server.send_message(msg)
# # print("Email Sent Successfully!")
# # server.quit()