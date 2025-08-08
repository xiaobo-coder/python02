import os
import platform
import sys

def isInuseWindow(port):
    if os.popen('netstat -an | findstr :' + str(port)).readlines():
        portIsUse = True
        print '%d is inuse' % port
    else:
        portIsUse = False
        print '%d is free' % port
    return portIsUse

def isInuseLinux(port):
    # lsof -i:{port}
    # not show pid to avoid complex
    if os.popen('netstat -na | grep :' + str(port)).readlines():
        portIsUse = True
        print '%d is inuse' % port
    else:
        portIsUse = False
        print '%d is free' % port
    return portIsUse

def isInuseAix(port):
    if os.popen('netstat -Aan | grep "\.' + str(port) + ' "').readlines():
        portIsUse = True
        print '%d is inuse' % port
    else:
        portIsUse = False
        print '%d is free' % port
    return portIsUse

def isInuseHp(port):
    if os.popen('netstat -an | grep "\.' + str(port) + ' "').readlines():
        portIsUse = True
        print '%d is inuse' % port
    else:
        portIsUse = False
        print '%d is free' % port
    return portIsUse

def isInuseSun(port):
    if os.popen('netstat -an | grep "\.' + str(port) + ' "').readlines():
        portIsUse = True
        print '%d is inuse' % port
    else:
        portIsUse = False
        print '%d is free' % port
    return portIsUse

def choosePlatform():
    machine = platform.platform().lower()
    if 'windows-' in machine:
        return isInuseWindow
    elif 'linux-' in machine:
        return isInuseLinux
    elif 'aix-' in machine:
        return isInuseAix
    elif 'hp-' in machine:
        return isInuseHp
    elif 'sunos-' in machine:
        return isInuseSun
    else:
        print 'Error, sorry, platform is unknown'
        exit(-1)

def checkNinePort(startPort):
    isInuseFun = choosePlatform()
    nineIsFree = True
    for i in range(1, 10):
        if (isInuseFun(startPort)):
            nineIsFree = False
            break
        else:
            startPort = startPort + 1
    return nineIsFree, startPort


def findPort(startPort):
    while True:
        flag, endPort = checkNinePort(startPort)
        if (flag == True):  # ninePort is ok
            break
        else:
            startPort = endPort + 1
    return startPort


def main(startPort):
    firstPort=findPort(startPort)
    print 'First port of nine free ports is ', firstPort

if __name__ == '__main__' :
    if len(sys.argv) > 1:
        print len(sys.argv)
        startPort = int(sys.argv[1])
    else:
        startPort = 500
    main(startPort)
