name = input("What's your name? ")

match name: 
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco" | "Sam" | "Rose":
        print("Slytherin")
    case _:
        print("Who?")


# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")