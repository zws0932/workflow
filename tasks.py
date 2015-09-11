import time
from celery import task

@task()
def add(x, y):
    return x + y

@task
def sendmail(mail):
    print "++++++++++++++++++++++++++++++++++++"
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')
    print "------------------------------------"
    return mail['to']




