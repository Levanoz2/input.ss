print('hello world')

promt = "Here you can enter"
promt += "a series of toppings>>>"

message = True

while message:
    message = input(promt)
    if message == "Quit":
        print("  I'll add " + message + " to your pizza.")
    else:
        break  

    promt = "How old are you?"
promt += "\nEnter 'quit' when you are finished >>>"

while True:
    age = input(promt)
    if age == "quit":
        break
    age = int(age)

    if age < 3:
        print("Your ticket cost is free")
    elif age < 13:
        print("Your ticket price is 11 $ ")
    else:
        print("Your ticket price is 13 $")


        sandwich_orders = ["big tasty","cheeseburger","mctoast", "bigmac"]
finished_sandwiches = [0,1,3]

while sandwich_orders:
    sandwich = sandwich_orders.pop(2)
    print("we are working on "+ sandwich + " at the moment")
    finished_sandwiches.append(sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("We have made " + sandwich + ", you can take it now")

sandwich_orders = ["dblcheezburger","bigtasty","cheeseburger","dblcheezburger","mctoast", "bigmac","doublecheezburger"]

finished_sandwiches = [0,1,3,2]

print("We are sorry, dblcheezburger sandwich ran out of")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("dblcheezburger")

print("\n")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Your order "+ sandwich + " will be prepared soon ! ")
    finished_sandwiches.append(sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("Your order " + sandwich + " is ready, take it")

name_promt = "Whats your name?>>>"
place_promt = "Where would you like to go?>>>"
next_promt = "\nWould you like to go with someone?(yes/no)>>>"

responses = {}

while True:
    name = input(name_promt)
    place = input(place_promt)
    
    
    responses[name] = place
    other_question = input(next_promt)
    if other_question == "yes":
        break
    
print(">>>results<<<")
for name,place in responses.items():
    print(name.title() + " would like to go in " + place.title() + ".")