'''
 print "Enter F"
 F=input()
 C=float(5)/9*(F-32)
 print F,'F=' ,C, 'C'

 import urllib2
 file = urllib2.urlopen('http://helloworldbook2.com/data/message.txt')
 message = file.read()
 print message

'''
'''
FN='Martin'
SN='Sun'
print FN,SN

print "���1ԪǮӲ�������ǣ�"
_1RMB=int(raw_input())
print "���5ëǮӲ�������ǣ�"
_05RMB=input()
print '1ëӲ�������أ�'
_01RMB=input()
print '��һ����',_1RMB*1+_05RMB*0.5+_01RMB*0.1,'Ԫ'

'''


import easygui  # EasyGUI has to be put under Python27 folder.

# easygui.msgbox('Hello There!') #This is the first FW for GUI.

user_response = easygui.msgbox('Hello there!')

print user_response



