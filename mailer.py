# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from django.template import loader
from amms.settings import EMAIL_HOST_USER   #项目配置邮件地址，请参考发送普通邮件部分

import time


def send_html_mail(subject, content, recipient_list):
    html_content = loader.render_to_string(
                        'mail_template.html',               #需要渲染的html模板
                        {
                            'name':content['name'],
                            'date':time.strftime("%Y-%m-%d %X",time.localtime()),    #参数
                            'info':content['info']
                        }
                   )
    msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, recipient_list)
    msg.content_subtype = "html" # Main content is now text/html
    msg.send()

#send_html_mail(subject, html_content, [收件人列表])
