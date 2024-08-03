def Alarm_time(user_current_time, user_wait_hours):
    # Calculate the alarm time
    Alarm_hours = (user_current_time + user_wait_hours) % 24
    return Alarm_hours

def main():
    try:
        # User must state their current time
        user_current_time = int(input("The current time: "))
        if user_current_time < 0 or user_current_time > 23:
            raise ValueError("The time range is between 0 and 23.")
        
        # How many hours to wait for the alarm?
        user_wait_hours = int(input("Specify the number of hours to wait for the alarm: "))
        if user_wait_hours < 0:
            raise ValueError("The program only accept non-negative integer.")

        # When will the alarm go off
        user_alarm_time = Alarm_time(user_current_time, user_wait_hours)
        
        # Display result
        print(f"it will be {user_alarm_time}:00 when the alarm goes off.")
    except ValueError as e:
        print(f"Invalid input: {e}")
main()
