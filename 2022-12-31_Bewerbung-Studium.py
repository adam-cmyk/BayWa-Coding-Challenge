from random import * #um eine Zufallszahl generieren zu können
from getpass import getpass #Passwortmodul in Python --> Schriftfarbe wird nicht angezeigta
from time import sleep #um Zeiten zwischen einzelnen Schritten zu ermöglichen

f"bcolors.RESET_COLOR"

class bcolors:


    GREEN = '\033[92m' #grüne Farbe
    YELLOW = '\033[93m' #gelbe Farbe
    RED = '\033[91m' #rote Farbe
    RESET_COLOR = '\033[0m' #Farbe wird zurückgesetzt == Standartfarbe (hier weiß)
    BLUE = '\033[34m' #blaue Farbe


print("Willkommen zu einem kleinen lustigen Zahlenratenspiel für zwei Spieler :) \nViel Spaß :) ") 
print("Das Spiel funktioniert wie folgt: Es werden zufällige Zahlen (von 0 bis 250) vom Computer ausgesucht, dabei soll jeder Spieler versuchen, so genau wie möglich, an der ausgesuchten Zahl zu sein. \nACHTUNG: Erlaubt sind nur ganze natürliche Zahlen!") # kurze Info über das Spiel

player_number = 2
b = 0
dis1 = 1
dis2 = 1
points_player2 = 0
points_player1 = 0

while b == 0:
    rounds = int(input("Wie viele Runden soll gespielt werden?: ")) #Nachfrage, wie oft gespielt werden soll
    if rounds == 0:
        print("Fehler. Es wurde nicht für eine Runde gestartet") # Fehlermeldung falls keine Runden eingegeben wurden
        break
    if player_number == 2:
        player_1 = input("Name des 1. Spielers?: ") #Namenseingabe des 1. Spieler
        player_2 = input("Name des 2. Spielers?: ") #Namenseingabe des 2. Spieler
        if player_1 == player_2:
            print("Fehler. Beide Spieler haben denselben Namen. Bitte wiederholen und unterscheidliche Namen verwenden.")
            break
    else:
        print("Fehler. Es wurden zu viele Spieler bzw. keine zwei Spieler angefragt. \nBitte den Vorgang wiederholen")
        break
        
    
        
    i = 0
    while i < rounds:
        i += 1
        x = randint(0, 250) #Zufallszahl zwischen 0 und 250
        #x = int(randint(1, r))
    
        if player_number == 2:
            input_player1 = int(getpass("Zahl von %s : "%(player_1))) #verdeckte Zahleingabe der Spieler
            input_player2 = int(getpass("Zahl von %s : "%(player_2))) #verdeckte Zahleingabe der Spieler
        else:
            print("Es wurden keine Zahlen eingegeben. Bitte das Spiel wiederholen") #Fehlermeldung falls keine Zahlen eingegeben wurden
            break 
           
        if input_player1 > 250: 
            print("Fehler! Die eingegebene Zahl von", player_1, "ist über 250") #Fehlermeldung, falls die Zahl höher als 250 war
            break
        elif input_player2 > 250:
            print("Fehler! Die eingegebene Zahl von", player_2, "ist über 250") #Fehlermeldung, falls die Zahl höher als 250 war
            break
        
        sleep (1) #Pause zwischen
        print (f"Die gesuchte Zahl ist{bcolors.RED}", x) #Ausgabe der gesuchten Zahl
        sleep (1)
        
        dis1 = abs(input_player1 - x) # absolute Differenz zwischen gesuchter Zahl und eingegebener Zahl
        dis2 = abs(input_player2 - x) # absolute Differenz zwischen gesuchter Zahl und eingegebener Zahl
        
        
        if player_number == 2:
            print(f"{bcolors.RESET_COLOR}Zahl von %s:{bcolors.BLUE} "%(player_1), input_player1) #Ausgabe der zuvor eingegebnen Werte (line 45)
            sleep (1)
            print(f"{bcolors.RESET_COLOR}Zahl von %s:{bcolors.BLUE} "%(player_2), input_player2) #Ausgabe der zuvor eingegebnen Werte (line 46)
            sleep(1)
        else:
            print("Ein Fehler ist aufgetreten. Bitte noch einmal versuchen zu spielen.")


        if dis1 > dis2: # wenn Spieler 2 näher an der gesuchten Zahl ist
            print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player_2))
            points_player2 += 1
            if dis2 == x:
                print("Glückwunsch die richtige Zahl wurde getroffen. Du erhältst 2 Punkte")
                points_player2 += 1
        elif dis1 == dis2: # wenn beide Spieler dieselbe Zahl haben
            print(f"{bcolors.YELLOW}%s hat die gleiche Zahl wie %s {bcolors.RESET_COLOR}"%(player_1, player_2),". Somit erhält keiner der beiden Spieler einen Punkt.")
        else: # wenn Spieler 1 näher an der geuschten Zahl ist
            print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player_1))
            points_player1 += 1
            if dis1 == x:
                print("Glückwunsch die richtige Zahl wurde getroffen. Du erhälst 2 Punkte")
                points_player1 += 1
        print("Zwischenstand: ", player_1, ":", points_player1, " Punkt(e) ;", player_2, ":", points_player2, "Punkt(e)")
    break

sleep(1)

print("Herzlichen Glückwunsch. Ihr habt das Spiel beendet.")
if dis1 > dis2:
    print(f"{bcolors.YELLOW}%s hat das Spiel gewonnen." %(player_2))
elif dis2 == dis1:
    print(f"{bcolors.YELLOW} Gleichstand. Ihr beiden seid zusammen Gewinner!")
else:
    print(f"{bcolors.YELLOW}%s hat das Spiel gewonnen." %(player_1))
      
retry = int(input(f"{bcolors.RESET_COLOR} Möchtet ihr nochmal spielen (0 = ja, 1 = nein)? "))
if retry == 0:
    x = randint(0, 250)
    counter_repeat = int(input("Wie oft wollt ihr das Spiel wiederholen?: "))
    while counter_repeat > 0:
        counter_repeat -= 1
        if player_number == 2:
            input_player1 = int(getpass("Zahl von %s : "%(player_1))) #verdeckte Zahleingabe der Spieler
            input_player2 = int(getpass("Zahl von %s : "%(player_2))) #verdeckte Zahleingabe der Spieler
        else:
            print("Es wurden keine Zahlen eingegeben. Bitte das Spiel wiederholen") #Fehlermeldung falls keine Zahlen eingegeben wurden
            break 
                
        if input_player1 > 250: 
            print("Fehler! Die eingegebene Zahl ist über 250") #Fehlermeldung, falls die Zahl höher als 250 war
            break
        elif input_player2 > 250:
            print("Fehler! Die eingegebene Zahl ist über 250") #Fehlermeldung, falls die Zahl höher als 250 war
            break
                
        sleep (1) #Pause zwischen
        print (f"Die gesuchte Zahl ist{bcolors.RED}", x) #Ausgabe der gesuchten Zahl
        sleep (1)
                    
        dis1 = abs(input_player1 - x) # absolute Differenz zwischen gesuchter Zahl und eingegebener Zahl
        dis2 = abs(input_player2 - x) # absolute Differenz zwischen gesuchter Zahl und eingegebener Zahl
                    
                    
        if player_number == 2:
            print(f"{bcolors.RESET_COLOR}Zahl von %s:{bcolors.BLUE} "%(player_1), input_player1) #Ausgabe der zuvor eingegebnen Werte (hier line 98)
            sleep (1)
            print(f"{bcolors.RESET_COLOR}Zahl von %s:{bcolors.BLUE} "%(player_2), input_player2) #Ausgabe der zuvor eingegebnen Werte (hier line 99)
            sleep(1)
        else:
            print("Ein Fehler ist aufgetreten. Bitte noch einmal versuchen zu spielen.")
                    
                        
        if dis1 > dis2: # wenn Spieler 1 näher an der gesuchten Zahl ist
            print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player_2))
        elif dis1 == dis2: # wenn beide Spieler dieselbe Zahl haben
            print(f"{bcolors.YELLOW}%s hat die gleiche Zahl wie %s somit erhält keiner einen Punkt{bcolors.RESET_COLOR}"%(player_1, player_2))
        else: # wenn Spieler 2 näher an der geuschten Zahl ist
            print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player_1))            
elif retry == 1:
    print("Schade, dass ihr schon aufhören wollt. Bis bald.")
else:
    print("Fehler, ihr habt etwas anderes eingetippt, als 0 oder 1")
