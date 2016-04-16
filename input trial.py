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

print "你的1元钱硬币数量是："
_1RMB=int(raw_input())
print "你的5毛钱硬币数量是："
_05RMB=input()
print '1毛硬币数量呢？'
_01RMB=input()
print '你一共有',_1RMB*1+_05RMB*0.5+_01RMB*0.1,'元'

'''


import easygui  # EasyGUI has to be put under Python27 folder.

# easygui.msgbox('Hello There!') #This is the first FW for GUI.

user_response = easygui.msgbox('Hello there!')

print user_response



