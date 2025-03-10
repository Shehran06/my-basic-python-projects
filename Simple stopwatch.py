import  time

global stopmin, stopsec
stopmin=int(input("Enter minutes"))
stopsec=int(input("Enter secs"))

global minutes, seconds

global stop_timer


def start():
    seconds = 0
    minutes = 0

    while seconds>=0:
        seconds+=1
        time.sleep(1)
        current_time = f"{minutes:02}:{seconds:02}"
        print(current_time)
        if seconds>=60:
            minutes+=1
            seconds=0

        if seconds==stopsec and minutes==stopmin:
            print("time up")
            break

def stop():
    global stop_timer
    stop_timer = True  # Set stop_timer to True to stop the timer

start()
stop()
