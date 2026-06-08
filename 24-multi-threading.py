
"""
This program demonstrates multithreading by executing three household chores
(walk dog, take out trash, get mail) simultaneously using threading.Thread,
then waits for all to complete before printing "All chores complete"
"""

#multi tasking
#executing functions at the same time
#threading.Thread(target=my_function)
import threading
import time
def walk_dog():
    time.sleep(8)
    print("You finished walking the dog")
def take_out_trash():
    time.sleep(2)
    print("You take out the trash")
def get_mail():
    time.sleep(4)
    print("you get the mail")

chore1=threading.Thread(target=walk_dog)
chore1.start()

chore2=threading.Thread(target=take_out_trash)
chore2.start()

chore3=threading.Thread(target=get_mail)
chore3.start()
#we are executing these three functions at the same time
#it will print based on waht is finished first
#wait for chores to finish
chore1.join()
chore2.join()
chore3.join()

print("All chores complete")

#chore2=threading.Thread(target=take_out_trash,args=("scooby",)) 
#it is a tuple