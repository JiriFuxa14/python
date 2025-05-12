










def ping_cj():
    while True:
        user_input = input("Should he stream the rest of the season? ").strip().lower()
        if user_input == "yes":
            print("Continuing to ask...")
        else:
            print("they said no")
            return "Stream decision made"
ping_cj()