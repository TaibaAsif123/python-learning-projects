
"""
This program sets an alarm that checks the current time every second and plays a sound
file when the system time matches the user-specified alarm time
"""

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")



def main():
    alarm_time=input("Enter alarm time (HH:MM:SS)")
    set_alarm(alarm_time)
    sound_file="16-alarm.mp3"
    is_running=True
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if current_time==alarm_time:
            print("Wake up")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running=False

if __name__=="__main__":
    main()
