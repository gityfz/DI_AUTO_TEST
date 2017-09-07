#!coding:utf-8
import re


def isString(s):
    try:
        s.lower() + s + ' '
    except:
        return False
    else:
        return True

def isAccount(s):
    reg = re.compile(r'^[0-9a-zA-z_]+$')
    if (reg.match(s)):
        return True
    else:
        return False

def isPassword(s):
    if(isString(s) and len(str(s))>5 and len(str(s))<19):
        return True
    else:
        return False


def isAId(taskId):
    try:
        if(int(taskId)>=0):
            return taskId.isdigit()
        else:
            return False
    except:
        return False


def isAIp(sourceIP):
    reg=re.compile(r'^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$')
    if(reg.match(sourceIP)):
        return True
    else:
        return False


def isAPort(sourcePort):
    try:
        if(int(sourcePort)>=0 and int(sourcePort)<=65535):
            return sourcePort.isdigit()
        else:
            return False
    except:
        return False

def ipToDecimal(ip):
    sum = 0
    if(ip==''):
        return ''
    else:
        ip=ip.split('.')
        for i, val in enumerate(ip):
            sum=sum+int((255 ** (3 - i)) * int(val))
        return sum