import random

random_number = random.randint(1,100)

print(random_number)

count = 1

while True:
    try:
        myNumber = int(input("insert any number between 1 and 100 : "))
        
        if myNumber < random_number:
            print("guess higher")
        elif myNumber > random_number:
            print("guess lower")
        else:
            print(f"congrats, you guessed right in {count} tries")
            break
        count = count+1
    except: 
        print("error occured, please input numbers only")