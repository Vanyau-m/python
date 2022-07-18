# Создаем генератор паролей
import smtplib
import random

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#Задаем символы для пароля
alph = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%&*()_1234567890'
number = int( input('Какое количество паролей необходимо? '))
lenght = int( input('Какая нужна длина пароля? '))

#Сама генерация пароля + запись его в файл
for x in range( number ):
    password = ''
    for i in range (lenght):
        password+=random.choice(alph)
    print('Мой пароль - ' + password)
    name_file = input("Введи имя твоего файла:  ")
    text_file = open("C:\\Users\\IVAN\\PycharmProjects1\\gen_password\\" + name_file+ ".txt", "a")
    text_file.write('\n' + password)
    text_file.close()

#Данные для отправки с почты gmail
address_from = ""                  # Откуда отправляем
address_to = ""                    # Кому отправляем
e_password = input("Введите пароль от почты для отправки: ")      # Пароль от почты (Сделать вводимым значением )

path = "C:\\Users\\IVAN\\PycharmProjects1\\gen_password\\" + name_file+ ".txt"

message = MIMEMultipart()
message['From']    = address_from
message ['To']     = address_to
message['Subject'] = 'Сообщение Python'
body = input("Введите текст сообщения перед отправкой: ")

attach = MIMEApplication(open(path, 'rb').read())
attach.add_header('Content-Disposition', 'attachment', filename=str(name_file)+'.txt')

message.attach(MIMEText(body,'plain'))
message.attach(attach)

server = smtplib.SMTP('smt.gmail.com', 587)
server.starttls()
server.login(address_from, e_password)
server.send_message(message)
server.quit()

