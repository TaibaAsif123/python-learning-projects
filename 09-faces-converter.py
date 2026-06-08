

"""
This program converts text-based emoticons :) and :( into their corresponding
emoji characters 🙂 and 🙁 based on user input
"""

def converter(msg):
    msg1=msg.replace(":)",'🙂')
    msg2=msg1.replace(":(",'🙁')
    return msg2

def main():
    msg=input("ENTER ANY EMOJI [:)/:(]")
    result=converter(msg)
    print(result)
main()