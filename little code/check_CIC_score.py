import urllib.request
import urllib.parse
import urllib.error
import time
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# get initial sore
url = 'http://www.cic.gc.ca/english/express-entry/rounds.asp'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
tags = soup('td')

number = tags[0].text  # may contain footnote info
score = tags[1].text

print('number of invitation:', number)
print('Score:', score)

print("listening to " + url)

while True:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    tags = soup('td')

    number_new = tags[0].text
    score_new = tags[1].text

    if (number_new != number or score_new != score):
        number = number_new
        score = score_new

        # send email
        user_id = 'auto@gmail.com'
        passward = 'xxxx'

        client_addr = 'your_email@gmail.com'

        msg = MIMEMultipart()
        msg['From'] = 'auto@gmail.com'
        msg['To'] = client_addr
        msg['Subject'] = "CIC EE sore update!"

        body = 'Number of invitation:%s \nScore:%s' % (number, score)
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user_id, passward)

        server.sendmail('auto@gmail.com', client_addr, msg.as_string())
        server.quit()

    else:
        print('no update', time.strftime("%c"))
        pass

    time.sleep(4*60*60)
