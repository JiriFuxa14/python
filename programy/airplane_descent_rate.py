def calculate_descent_rate(current_altitude, target_altitude, distance_to_target):
    """
    Calculate the required descent rate in feet per minute.

    :param current_altitude: Current altitude in feet
    :param target_altitude: Target altitude in feet
    :param distance_to_target: Distance to target in nautical miles
    :return: Required descent rate in feet per minute
    """

    nautical_miles_to_feet = 6076.12
    minutes_per_hour = 60

    altitude_difference = current_altitude - target_altitude

   
    descent_rate = (altitude_difference / (distance_to_target * nautical_miles_to_feet)) * minutes_per_hour

    return descent_rate
    
current_altitude = float(input("Enter the current altitude in feet: "))
target_altitude = float(input("Enter the target altitude in feet: "))
distance_to_target = float(input("Enter the distance to target in nautical miles: "))

descent_rate = calculate_descent_rate(current_altitude, target_altitude, distance_to_target)
print(f"Required descent rate: {descent_rate:.2f} feet per minute")
