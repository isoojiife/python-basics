weather = input("Is it sunny or rainy? ")
homework = input("Have you finished your homework? (yes/no) ")

if weather == "sunny":
    if homework == "yes":
        print("Go to the park.")
    else:
        print("Finish your homework first.")

if weather == "rainy":
    if homework == "yes":
        print("Play video games at home.")
    else:
        print("Finish your homework and then read a book.")