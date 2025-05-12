def car():
city_speed_limit = 50
highway_speed_limit = 130
car_speed = (int)(input("car speed:"))
if car_speed >= highway_speed_limit and car
if car_speed > city_speed_limit or car_speed > highway_speed_limit:
    print("Car is speeding")
else:
    print("Car is not speeding")
    
