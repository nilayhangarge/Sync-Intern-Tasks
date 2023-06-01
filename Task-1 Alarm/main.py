# SYNC INTERN's TASK-1 "ALARM CLOCK"
import datetime
import time
from threading import *
from tkinter import *

import winsound

root = Tk()

root.geometry("450x250")  # page size


def threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to Wake up")

            winsound.PlaySound("Alarm.wav", winsound.SND_ASYNC)


# Adding Tasks Name, Author Name etc.
Label(root, text="SYNC INTERN's PYTHON TASK-1", font="Helvetica 15 bold", fg="blue").pack(pady=10)
Label(root, text="Task-1 Alarm Clock By Nilay Hangarge", font="Helvetica 15 bold", fg="green").pack(pady=10)
Label(root, text="⏬SET THE TIME HERE⏬", font="Helvetica 15 bold").pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('HRS', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
         '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('MIN', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
           '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
           '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52',
           '53', '54', '55', '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('SEC', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
           '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
           '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52',
           '53', '54', '55', '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="CLICK TO SET", font="Helvetica 15 bold", command=threading).pack(pady=15)

root.mainloop()  # Final Execution
