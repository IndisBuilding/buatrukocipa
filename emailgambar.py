import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def email():
	fromaddr = "rukocipa@gmail.com"
	fromname = "Rumah Cerdas Ruko Cipamokolan"
	penerima = ['faicanhas@gmail.com','Lina.indrawati@ymail.com','tetty.tjandrawati@gmail.com','hairudin.hasibuan@gmail.com']
	#penerima = ['okyzaprabowo@gmail.com','wahyuputrarama@gmail.com','ceceraraa@gmail.com','faicanhas@gmail.com']
	msg = MIMEMultipart()
	msg['From'] = fromname	
	msg['Subject'] = 'Pemberitahuan dari Ruko Cipamokolan'
	msg['To'] = ", ".join(penerima)

	text = MIMEText("Situasi terkini")
	msg.attach(text)
	#for file in pngfiles:
	fp = open('image1.jpg','rb')
	img = MIMEImage(fp.read())
	fp.close
	img.add_header('Content-Disposition', 'attachment', filename='depan_pagar.jpg')
	msg.attach(img)

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(fromaddr, "rumaht0k0cipam0k0lan")
	server.sendmail(fromaddr, penerima, msg.as_string())
	server.quit()
	
