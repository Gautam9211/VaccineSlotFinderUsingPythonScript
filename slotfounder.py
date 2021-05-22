import time, threading
StartTime=time.time()
def action():
   print('\naction ! -> time : {:.1f}s'.format(time.time()-StartTime))
   import  requests
   district_id= 702
   from datetime import date,datetime
   today = date.today()
   d1 = today.strftime("%d-%m-%Y")
   e=d1[0:2]
   j=int(e)+1
   d2=d1.replace(e,str(j)) 

   url1= f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_id}&date={d1}"
   url2=f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_id}&date={d2}"
   headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

   result1 = requests.get(url1, headers=headers)
   result2 = requests.get(url2, headers=headers)
   
   # Python program to read
   # json file 
   import json 
   # JSON string 
   #   deserializes into dict 
   # and returns dict.
   y1 = json.loads(result1.content.decode()) 
   y2 = json.loads(result2.content.decode()) 
   #print(f" data ::: {y}" )   
  
   
   from plyer import notification
   title = 'Hello Gautam!'
   from beepy import beep
   # integer as argument
   if(y1["sessions"]==[] or y2["sessions"]==[]):  
       print(f"There is no session on date ::{d1 if y1['sessions']==[] else d2}!")
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S")
   print("Current Time =", current_time)   
   a =y1["sessions"]!=[] 
   b =y2["sessions"]!=[]
   if( a or b):
      for x in range(len(y1["sessions"])):
         if((y1["sessions"][x]["min_age_limit"]==18) and (y1["sessions"][x]["available_capacity_dose1"]>0)):
           print(f"slots are available in center_id:: {y1['sessions'][x]['center_id']} and center name is :: {y1['sessions'][x]['name']} on date {y1['sessions'][x]['date']}")
           message= f'one slot is found in {y1["sessions"][x]["name"]} !'
           notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 5,
                    toast=False) 
           beep(sound=2)           
           import smtplib
           from email.message import EmailMessage
           msg = EmailMessage()
           msg.set_content(f"slots are available in center_id:: {y1['sessions'][x]['center_id']} and center name is :: {y1['sessions'][x]['name']} on date {y1['sessions'][x]['date']}")
           msg["subject"]="slot found!"
           msg["to"]= ["agarwal1991ng@gmail.com","shantanuagarwalsdimt@gmail.com"]
           user="agarwal1997ng@gmail.com"
           msg["from"]= user
           password = "mzbvabdnmcnvktpg"
           server=smtplib.SMTP("smtp.gmail.com",587)
           server.starttls()
           server.login(user,password)
           server.send_message(msg)
           server.quit()
           print("email are sent to respective emails")
         else:
           print(f"No slots are available  in {y1['sessions'][x]['name']} on date {y1['sessions'][x]['date']}.")  

           """
           from twilio.rest import Client
           from twilio.base.exceptions import TwilioRestException
           TWILIO_ACCOUNT_SID="AC161a9536f39e6c6dc7827b96080071c1"
           TWILIO_AUTH_TOKEN="b5b5d7dadf7e5669950b5107d7da6a8e"
           client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
           try:
              message = client.messages.create(
                     body=f"Hey Gautam Agarwal,we found the slot in {y1['sessions'][x]['name']} on date {y1['sessions'][x]['date']}",
                     from_='+14086634492',
                     to='+918650435741',
                 )
           except TwilioRestException as e:
              print(e)
              """
      for x in range(len(y2["sessions"])):        
         if((y2["sessions"][x]["min_age_limit"]==18) and (y2["sessions"][x]["available_capacity_dose1"]>0)):
              print(f"slot are available in center_id:: {y2['sessions'][x]['center_id']} and center name is ::  {y2['sessions'][x]['name']} on date {y2['sessions'][x]['date']}")
              message= f'one slot is found in {y2["sessions"][x]["name"]} !'
              notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 5,
                    toast=False) 
              beep(sound=2)
              import smtplib
              from email.message import EmailMessage
              msg = EmailMessage()
              msg.set_content(f"slots are available in center_id:: {y2['sessions'][x]['center_id']} and center name is :: {y2['sessions'][x]['name']} on date {y2['sessions'][x]['date']}")
              msg["subject"]="slot found!"
              msg["to"]= ["agarwal1991ng@gmail.com","shantanuagarwalsdimt@gmail.com"]
              user="agarwal1997ng@gmail.com"
              msg["from"]= user
              password = "mzbvabdnmcnvktpg"
              server=smtplib.SMTP("smtp.gmail.com",587)
              server.starttls()
              server.login(user,password)
              server.send_message(msg)
              server.quit()
              print("email sended to respective emails")
              
              """from twilio.rest import Client
              from twilio.base.exceptions import TwilioRestException
              TWILIO_ACCOUNT_SID="AC161a9536f39e6c6dc7827b96080071c1"
              TWILIO_AUTH_TOKEN="b5b5d7dadf7e5669950b5107d7da6a8e"
              client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
              try:
                message = client.messages.create(
                     body=f"Hey Gautam Agarwal,we found the slot in {y2['sessions'][x]['name']} on date {y2['sessions'][x]['date']}",
                     from_='+14086634492',
                     to='+918650435741',
                 )
              except TwilioRestException as e:
               print(e)
                  """
         else:
           print(f"No slots are available  in  {y2['sessions'][x]['name']} on date {y2['sessions'][x]['date']}.")           
   else:
           print(f"No slots are available.")


class setInterval :
    def __init__(self,interval,action) :
        self.interval=interval
        self.action=action
        self.stopEvent=threading.Event()
        thread=threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            self.action()

    def cancel(self) :
        self.stopEvent.set()

# start action every 86400s =1day
inter=setInterval(60,action)
print('just after setInterval -> time : {:.1f}s'.format(time.time()-StartTime))

# will stop interval in 120s
#t=threading.Timer(6,inter.cancel)
#t.start()