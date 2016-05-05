import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage

def email(text2):
	fromaddr = "rukocipa@gmail.com"
	fromname = "Rumah Cerdas Ruko Cipamokolan"
	penerima = ['hairudin.hasibuan@gmail.com','tetty.tjandrawati@gmail.com','faicanhas@gmail.com','Lina.indrawati@ymail.com']
	
	msg = MIMEMultipart()
	msg['From'] = fromname
	msg['To'] = ", ".join(penerima)
	msg['Subject'] = 'Pemberitahuan dari Ruko Cipamokolan'

	text1 = "Perintah berhasil dieksekusi. \nStatus : \n"
	#text2  = "nyala"
	pesan = MIMEText(text1 + text2)
	msg.attach(pesan)

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login(fromaddr, "rumaht0k0cipam0k0lan")
	server.sendmail(fromaddr, penerima, msg.as_string())
	server.quit()

#email("ayolah")
