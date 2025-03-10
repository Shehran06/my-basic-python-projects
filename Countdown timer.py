import time
def countdown():
 minutes=int(input("enter minutes"))
 secs=int(input("Enter seconds"))
 total_time= minutes*60+secs

 while total_time>0:
     minutes_left=total_time//60
     secs_left=total_time%60
     currenttime= f"{minutes_left:02}:{secs_left:02}"
     print(currenttime+"\n")
     time.sleep(1)#to create a time delay and count

     total_time-=1;
     print(total_time)

     if total_time==0:
         print("times up")

countdown()