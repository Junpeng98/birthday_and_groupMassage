#  以节日祝福消息群发为场景，支持多个节日的的消息群发，消息内容与节日相关。
#  实现定时发送，以纪念日，生日为场景，消息内容与纪念日相关。
#    实现对应消息的简单自动回复。
#    节日包括 元旦 除夕 端午等除清明节外的传统节日
#    生日（纪念日） 暂定为使用者输入 昵称 和日期实现
#    2016213155 丁峻鹏

import itchat
import time

from itchat.content import *
from datetime import datetime
from sched import scheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from pip._vendor.distlib.compat import raw_input
message_festival = '来临之际，祝大家节日快乐！'
message_birthday = ',祝你生日快乐！'
global b_name

def send_yuandan():
    
    myfriends = itchat.get_friends()
    count = 0
    
    for myfriends in myfriends:
        print(myfriends)
        if myfriends['RemarkName']:
            print(myfriends['RemarkName'])
            print(myfriends["UserName"])
            message='元旦'+message_festival
            itchat.send(message,toUserName=myfriends["UserName"])

            time.sleep(0.5)
            count += 1
            #print('发送成功')
def send_chuxi():
    
    myfriends = itchat.get_friends()
    count = 0
    
    for myfriends in myfriends:
        print(myfriends)
        if myfriends['RemarkName']:
            print(myfriends['RemarkName'])
            print(myfriends["UserName"])
            message='除夕夜'+message_festival
            itchat.send(message,toUserName=myfriends["UserName"])

            time.sleep(0.5)
            count += 1
            #print('发送成功')

            
def send_duanwu():
    
    myfriends = itchat.get_friends()
    count = 0
    
    for myfriends in myfriends:
        print(myfriends)
        if myfriends['RemarkName']:
            print(myfriends['RemarkName'])
            print(myfriends["UserName"])
            message='端午节'+message_festival
            itchat.send(message,toUserName=myfriends["UserName"])

            time.sleep(0.5)
            count += 1
            #print('发送成功')
def send_zhongqiu():
    
    myfriends = itchat.get_friends()
    count = 0
    
    for myfriends in myfriends:
        print(myfriends)
        if myfriends['RemarkName']:
            print(myfriends['RemarkName'])
            print(myfriends["UserName"])
            message='中秋节'+message_festival
            itchat.send(message,toUserName=myfriends["UserName"])

            time.sleep(0.5)
            count += 1
            #print('发送成功')

def ask_birthday(scheduler): 
    global b_name
    b_name = raw_input("想要向哪位好友发送生日祝福:")   
    
    month=raw_input("他/她的生日是几月:")
    day=raw_input("他/她的生日是几日:")
      
    year=2019
    now_time = datetime.now()
    now_hour=now_time.strftime('%H')
    
    now_sec=now_time.strftime('%M')
    now_sec=int(now_sec)+2
    scheduler.add_job(send_birthday,'date', run_date= datetime(year,int(month),int(day),int(now_hour),now_sec))    
 
                                                                     
def send_birthday():
    global b_name
    message=b_name+message_birthday
   
    myfriends=itchat.search_friends(name=b_name)
 
    itchat.send(message,toUserName=myfriends[0]["UserName"])

        

def main():
    itchat.auto_login(True)
    scheduler=BlockingScheduler()
    ask_birthday(scheduler)
    scheduler.add_job(send_yuandan,'date',run_date= datetime(2020,1,1))
    scheduler.add_job(send_chuxi,'date',run_date= datetime(2020,1,24))
    scheduler.add_job(send_duanwu,'date',run_date=  datetime(2020,6,25))
    scheduler.add_job(send_zhongqiu,'date',run_date=  datetime(2020,10,1))
    scheduler.start()


    

 
if __name__ == '__main__':
    
    main()    
    