from numpy import random
n = random.randint(0,100)

print("Number is between 0 - 100. Now the game is yours to play!")
choice = -1
cnt = 0
while choice != n:
  choice = int(input("Enter your choice "))

  if choice == n:
    print("GOAT")
    break

  elif choice < n:
    print("Oofff...the number is greater than your choice!")

  else:
    print("Ehhh the number is smaller than your choice!")
  cnt += 1

print(f"Game Over in {cnt} turns")