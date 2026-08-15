def format_name(name, lastname):
    capn = name.capitalize()
    capn2 = lastname.capitalize()
    return capn + " " + capn2

print(f"So your name is: {format_name(input("Enter your first name: ").lower(), input("Enter your last name: ").lower())}")