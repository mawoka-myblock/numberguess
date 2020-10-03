import random
import time

counter = 0

print("Hallo, willkommen zu meinem Spiel Number Guess! Willst du zufällige Zahlen benutzen? [J/n]:")
zufall = input()

while not zufall == "j" and not zufall == "n":
  print("Bitte gib j oder n ein:")
  zufall = input()

if zufall == "j":
  z = (random.randint  (0, 100))
elif zufall == "n":
  print("Die erste Zahl, bitte:")
  z1 = int(input())
#  while not z1.isnummeric():
#    print("Das war keine Zahl! Bitte Probiers nochmal:")
#    z1 = int(input())
  print("Die zweite Zahl, bitte:")
  z2 = int(input())
  
if z1 > z2:
  z = random.randint (z1, z2)
else:
  print("Da stimmt etwas nicht, mit deinen Nummern!")
  time.sleep(5)
  exit()

#Das eigentliche Spiel:

print("OK, ich habe mir eine Nummer überlegt, die du jetzt erraten darfst. Du sagst eine Nummer, und ich sage ob diese größer oder kleiner als meine Nummer ist.")
time.sleep(2)
print("Bitte fange jetzt an, zu raten:")
ui = int(input())
while not ui == z:
  if ui < z:
    print("Deine Zahl ist kleiner als meine Zahl!")
    ui = int(input())
    counter = counter + 1 
  elif ui > z:
    print("Deine Zahl ist größer als meine Zahl!")
    ui = int(input())
    counter = counter + 1

print("Du hast es geschafft! Du hast", counter, "Versuche gebraucht! Das hast du wirklich gut gemacht!")
print("Das Programm wird sich in 5 Sekunden schließen.")
time.sleep(5)
exit()

