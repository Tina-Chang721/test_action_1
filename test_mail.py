import smtplib, ssl #帶入套件smtplib 自動寄e-mail套件 ssl 安全加密套件
from email.mime.text import MIMEText #表示在層層資料夾裡面找到MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender ='qnys159875@gmail.com'
receiver = ['csmu05@gmail.com','qnys159875@gmail.com']
passwd = "kimd zxdg mrri ylke"
for i in receiver:
    msg = MIMEMultipart()  #類似input msg為變數可以變更
    msg["From"] = sender #用自己的email address 寄件者
    msg["To"] = i #收件者
    msg["Subject"] = Header("Test send email","utf-8").encode() #要記得用utf-8 用.encode轉換成0101

    body = "This is send by python\n" #\n表示換行
    body2 = "how are you?"

    msg_text=MIMEText("This is send by python")
    msg.attach(msg_text)
    c = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server: #google規定需要,465 表示port港口的意思
        server.login(sender,passwd)
        server.sendmail(sender,i,msg.as_string())
    print("success send mail")


