import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hrs, mins = divmod(mins, 60)
        days, hrs = divmod(hrs, 24)
        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hrs, mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Tik-tok! Time is up!")

t = int(input("Input time in seconds: "))

countdown(t)