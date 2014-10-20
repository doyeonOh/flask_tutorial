from flask.ext.mail import Message
from app import mail
from flask import render_template, current_app
from config import ADMINS
from threading import Thread
from flask import current_app
# from .decorators import async

# @async
# def send_async_email(app, msg):


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    with current_app.app_context():
        mail.send(msg)
    # send_async_email(current_app, msg)

def follower_notification(followed, follower):
    send_email("[microblog] %s is now following you!" % follower.nickname,
               ADMINS[0],
               [followed.email],
               render_template('followers_email.txt',
                               user=followed, follower=follower),
               render_template('followers_email.html',
                               user=followed, follower=follower))

