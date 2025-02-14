def calculate_speed(distance, time):
    if time <= 0:
        return "Time must be greater than zero"
    speed = distance / time
    return speed

#example
distance = float(input("Enter the distance in km: "))
time = float(input("Enter the time in hours: "))
required_speed = calculate_speed(distance, time)
print(f"To cover {distance} km in {time} hours, you need to go at {required_speed} km/h.")