
"""
This program converts a time input (e.g., "7:30") to a decimal value and determines
if it falls within breakfast (7-8), lunch (12-13), or dinner (18-19) time ranges
"""

def main():

    time = input("What time is it? ")

    result = convert(time)


    if 7 <= result <= 8:
        print("Breakfast Time")
    elif 12 <= result <= 13:
        print("Lunch Time")
    elif 18 <= result <= 19:
        print("Dinner Time")
def convert(time):

    hours, minutes = time.split(':')

    hours = float(hours)
    minutes = float(minutes) / 60

    return hours + minutes

if __name__ == "__main__":
    main()