def calling():
    user_input = input("should i call them?")
    if user_input == "yes": 
        print("calling them now")
    else:
        print("not calling them")  
    return calling
calling()
