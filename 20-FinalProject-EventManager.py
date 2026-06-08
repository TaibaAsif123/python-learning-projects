
"""
This program tracks user login/logout events across multiple machines and generates
a report showing which users are currently logged into each machine
"""

# Helper function to extract the date from an event
def get_event_date(event):
    return event.date

def current_users(events):
    # Sort events based on date
    events.sort(key=get_event_date)
    
    # Dictionary to track logged-in users on each machine
    machines = {}
    
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()  # Use a set to store users

        # Add or remove users based on login/logout event
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)

    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))
        else:
            print("{}: No users currently logged in".format(machine))

# Example usage
class Event:
    def __init__(self, date, machine, user, event_type):
        self.date = date
        self.machine = machine
        self.user = user
        self.type = event_type

events = [
    Event("2023-09-25 08:00", "Machine1", "UserA", "login"),
    Event("2023-09-25 08:05", "Machine1", "UserB", "login"),
    Event("2023-09-25 08:15", "Machine2", "UserC", "login"),
    Event("2023-09-25 08:20", "Machine1", "UserA", "logout"),
    Event("2023-09-25 08:30", "Machine2", "UserC", "logout"),
]

# Call the functions to generate the report
machines = current_users(events)
generate_report(machines)
