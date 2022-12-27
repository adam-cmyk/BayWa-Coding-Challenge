from random import * #um eine Zufallszahl generieren zu können
from getpass import getpass #Passwortmodul in Python --> Schriftfarbe wird nicht angezeigt
from re import S #reguläre Ausdrücke
from time import sleep #um Zeiten zwischen einzelnen Schritten zu ermöglichen

f"bcolors.RESET_COLOR"

class bcolors:


    GREEN = '\033[92m' #grüne Farbe
    YELLOW = '\033[93m' #gelbe Farbe
    RED = '\033[91m' #rote Farbe
    RESET_COLOR = '\033[0m' #Farbe wird zurückgesetzt == Standartfarbe (hier weiß)
    BLUE = '\033[34m' #blaue Farbe


print("Willkommen zu einem kleinen lustigen Zahlenratenspiel für zwei Spieler :) \nViel Spaß :) ") 

player_number = 2
 
b = 0
while b == 0:
    if player_number == 2:
        player_1 = input("Name des 1. Spielers?: ") #Namenseingabe des 1. Spieler
        player_2 = input("Name des 2. Spielers?: ") #Namenseingabe des 2. Spieler
    else:
        print("Fehler. Es wurden zu viele Spieler bzw. keine zwei Spieler angefragt. \nBitte den Vorgang wiederholen")
        break
        
    rounds = int(input("Wie viele Runden soll gespielt werden?: ")) #Nachfrage, wie oft gespielt werden soll
    if rounds == 0:
        print("Fehler. Es wurde nicht für eine Runde gestartet") # Fehlermeldung falls keine Runden eingegeben wurden
        break

    print("Das Spiel geht wie folgt: Es werden zufällige Zahlen (von 0 bis 500) vom Computer ausgesucht, dabei soll jeder Spieler versuchen, so genau wie möglich, an der ausgesuchten Zahl zu sein. ACHTUNG: Erlaubt sind nur natürliche Zahlen!") # kurze Info über das Spiel
        
    i = 0
    while i < rounds: #wenn i größer als die Rundenzahl ist
        i += 1 # i wird pro Runde größer
        r = randint(0, 500) #Zufallszahl zwischen 0 und 500
        x = int(randint(1, r))
    
        if player_number == 2:
            input_player1 = int(getpass("Zahl von %s : "%(player_1))) #verdeckte Zahleingabe der Spieler
            input_player2 = int(getpass("Zahl von %s : "%(player_2))) #verdeckte Zahleingabe der Spieler
        else:
            print("Es wurden keine Zahlen eingegeben. Bitte das Spiel wiederholen") #Fehlermeldung falls keine Zahlen eingegeben wurden
            break 
           
        if input_player1 > 500: 
            print("Fehler! Die eingegebene Zahl ist über 500") #Fehlermeldung, falls die Zahl höher als 500 war
            break
        elif input_player2 > 500:
            print("Fehler! Die eingegebene Zahl ist über 500") #Fehlermeldung, falls die Zahl höher als 500 war
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
        
            
        if dis1 > dis2: # wenn Spieler 1 näher an der gescuhten Zahl ist
            print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player_2))
        elif dis1 == dis2: # wenn beide Spieler dieselbe Zahl haben
            print(f"{bcolors.YELLOW}%s hat die gleiche Zahl wie %s somit erhält keiner einen Punkt{bcolors.RESET_COLOR}"%(player_1, player_2))
        else: # wenn Spieler 2 näher an der geuschten Zahl ist
            print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player_1))

    break # nach Abschluss der Schleife endet das Programm

