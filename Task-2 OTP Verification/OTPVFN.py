import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # TLS security
server.login('nilayhangarge@gmail.com', 'csexiggdvougflmi')
otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
msg = 'Hello User, Your OTP is ' + str(otp)
sender = ''
receiver = ''
server.sendmail('nilayhangarge@gmail.com', 'nilaynhangarge@acpce.ac.in', msg)
a = input("Enter Your OTP >> ")
if a == otp:
    print("Congratulations, Your OTP is Successfully Verified.")
else:
    print("Please check your OTP again & fill it properly.")

server.quit()
