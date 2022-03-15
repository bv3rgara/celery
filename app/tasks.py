from __future__ import absolute_import, unicode_literals

import time
import smtplib
import threading
from celery import shared_task

from django.shortcuts import render
from django.conf import settings as st
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@shared_task
def add(x, y):
    return x + y


@shared_task
def time_seconds(n):
    time.sleep(n)
    return True


@shared_task
def send_correo():
    mailServer = smtplib.SMTP(st.EMAIL_HOST, st.EMAIL_PORT)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(st.EMAIL_HOST_USER, st.EMAIL_HOST_PASSWORD)
    mensaje = MIMEMultipart()
    mensaje['From'] = st.EMAIL_HOST_USER
    mensaje['To'] = st.EMAIL_TO
    mensaje['Subject'] = 'Correo electronico de prueba'
    content = render_to_string(
        'template_email.html', {'user': 'Vergara Bruno'}
    )
    mensaje.attach(MIMEText(content, 'html'))
    mailServer.sendmail(
        st.EMAIL_HOST_USER,
        st.EMAIL_TO,
        mensaje.as_string()
    )
    print("Correo enviado correctamente desde send_correo")
    mailServer.close()
    # contenido = MIMEImage(file.read())
    # contenido.add_header(
    # 'Content-Disposition', 'attachment; filename = "Chuidiang-64.gif"'
    # )
    # mensaje.attach(contenido)


@shared_task
def send_email():
    content = render_to_string(
        'template_email.html', {'user': 'Vergara Bruno'}
    )
    send_mail(
        subject='Correo electronico de prueba',
        message='msm',
        from_email=st.EMAIL_HOST_USER,
        recipient_list=[st.EMAIL_TO],
        html_message=content,
    )
    print("Correo enviado correctamente desde send_email")
    # 
    # thread = threading.Thread(target=send_email, args=(user, ))
    # thread = threading.Thread(target=time_seconds, args=(15, ))
    # thead.start()
