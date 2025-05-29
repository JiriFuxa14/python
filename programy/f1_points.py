points = {
    "p1": 25, "p2": 24, "p3": 23, "p4": 22, "p5": 21, "p6": 20,
    "p7": 19, "p8": 18, "p9": 17, "p10": 16, "p11": 15, "p12": 14,
    "p13": 13, "p14": 12, "p15": 11, "p16": 10, "p17": 9, "p18": 8,
    "p19": 7, "p20": 6, "p21": 5, "p22": 4, "p23": 3, "p24": 2
}

driver_positions1 = input("Enter positions of your drivers (p1, p7): ").split(", ")
driver_positions2 = input("Enter positions of your opponent's drivers (p2, p8): ").split(", ")

# Check for duplicate positions
if len(driver_positions1) != 2 or len(driver_positions2) != 2:
    print("Error: Each player must input exactly two positions.")
elif set(driver_positions1) & set(driver_positions2):
    print("Error: Duplicate positions detected.")
else:
    # Calculate total points for each player
    total_points1 = sum(points.get(pos, 0) for pos in driver_positions1)
    total_points2 = sum(points.get(pos, 0) for pos in driver_positions2)

    # Determine the winner
    if total_points1 > total_points2:
        print("you won and get 4000 coins")
    elif total_points1 < total_points2:
        print("you lost and opponent gets 4000 coins")
    else:
        print("its a tie and gets determined by laptimes (who has the fastest lap)")
