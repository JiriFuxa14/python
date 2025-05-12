def check_overspeeding(altitude, airspeed):
    if altitude < 10000:
        if airspeed > 250:
            return "ALERT: Overspeeding below 10,000 feet! Alarm triggered in cockpit and sent to ATC."
        else:
            return "Aircraft is within the speed limit below 10,000 feet."
    else:
        if airspeed > 660:
            return "WARNING: Aircraft is exceeding typical airspeed limits above 10,000 feet!"
        else:
            return "Aircraft is within the speed limit above 10,000 feet."

if __name__ == "__main__":
    altitude = int(input("Enter the aircraft's altitude in feet: "))
    airspeed = int(input("Enter the aircraft's airspeed in knots: "))
    result = check_overspeeding(altitude, airspeed)
    print(result)
