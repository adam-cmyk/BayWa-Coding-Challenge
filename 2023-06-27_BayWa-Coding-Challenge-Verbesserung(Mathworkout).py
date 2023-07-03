from random import *
from getpass import getpass
from time import sleep

f"bcolors.RESET_COLOR"

class bcolors:


    GREEN = '\033[92m' #grüne Farbe
    YELLOW = '\033[93m' #gelbe Farbe
    RED = '\033[91m' #rote Farbe
    RESET_COLOR = '\033[0m' #Farbe wird zurückgesetzt == Standartfarbe (hier weiß)
    BLUE = '\033[34m' #blaue Farbe
    
print("Willkommen zu einem kleinen lustigen Zahlenratenspiel für zwei Spieler :) \nViel Spaß :) ") 
print("Das Spiel funktioniert wie folgt: Es werden zufällige Zahlen (von 0 bis 250) vom Computer ausgesucht, dabei soll jeder Spieler versuchen, so genau wie möglich, an der ausgesuchten Zahl zu sein. \nACHTUNG: Erlaubt sind nur ganze natürliche Zahlen!") # kurze Info über das Spiel

player1 = input("Name des ersten Spielers?: ")
player2 = input("Name des zweiten Spielers?: ")



def game_easy():
    x = randint(0, 250)
    try:
        input_player1 = int(getpass("Zahl von %s : "%(player1))) #verdeckte Zahleingabe der Spieler
        input_player2 = int(getpass("Zahl von %s : "%(player2))) #verdeckte Zahleingabe der Spieler
    except ValueError:
        print("Fehler. Keine gültige Zahleneingabe(n) !")
    
    if input_player1 > 250: 
        print("Fehler! Die eingegebene Zahl von", player1, "ist über 250") #Fehlermeldung, falls die Zahl höher als 250 war
    elif input_player2 > 250:
        print("Fehler! Die eingegebene Zahl von", player2, "ist über 250") #Fehlermeldung, falls die Zahl höher als 250 war
        False
    
    sleep (1) #Pause zwischen
    print (f"Die gesuchte Zahl ist{bcolors.RED}", x) #Ausgabe der gesuchten Zahl
    sleep (1)
    
    print(f"{bcolors.RESET_COLOR}Zahl von %s:{bcolors.BLUE} "%(player1), input_player1) #Ausgabe der zuvor eingegebnen Werte (line 45)
    sleep (1)
    print(f"{bcolors.RESET_COLOR}Zahl von %s:{bcolors.BLUE} "%(player2), input_player2) #Ausgabe der zuvor eingegebnen Werte (line 46)
    sleep(1)
    
    dis1 = x - input_player1
    dis2 = x - input_player2
    
    if dis1 > dis2:
        print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player1))
        if dis1 == x:
            print("Glückwunsch", player1, ", die richtige Zahl wurde getroffen.")
    elif input_player1 == input_player2: # wenn beide Spieler dieselbe Zahl haben
        print(f"{bcolors.YELLOW}%s hat die gleiche Zahl wie %s {bcolors.RESET_COLOR}"%(player1, player2))
    else: 
        print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player2))
        if dis2 == x:
            print("Glückwunsch", player2, ", die richtige Zahl wurde getroffen.")

def game_normal():
    try:
        rounds = int(input("Wie viele Runden wollt ihr spielen? "))
    except ValueError:
        print("Fehler. Keine gültige Zahleneingabe!")
    
    x = randint(0, 250)
    
    while rounds > 0:
        rounds -= 1
        try:
            input_player1 = int(getpass("Zahl von %s : "%(player1))) #verdeckte Zahleingabe der Spieler
            input_player2 = int(getpass("Zahl von %s : "%(player2))) #verdeckte Zahleingabe der Spieler
        except ValueError:
            print("Fehler. Keine gültigen Zahleneingabe(n) !")
        
        if input_player1 > 250: 
            print("Fehler! Die eingegebene Zahl von", player1, "ist über 250") #Fehlermeldung, falls die Zahl höher als 250 war
        elif input_player2 > 250:
            print("Fehler! Die eingegebene Zahl von", player2, "ist über 250") #Fehlermeldung, falls die Zahl höher als 250 war
            False
        
        sleep (1) #Pause zwischen
        print (f"Die gesuchte Zahl ist{bcolors.RED}", x) #Ausgabe der gesuchten Zahl
        sleep (1)
        
        print(f"{bcolors.RESET_COLOR}Zahl von %s:{bcolors.BLUE} "%(player1), input_player1) #Ausgabe der zuvor eingegebnen Werte (line 45)
        sleep (1)
        print(f"{bcolors.RESET_COLOR}Zahl von %s:{bcolors.BLUE} "%(player2), input_player2) #Ausgabe der zuvor eingegebnen Werte (line 46)
        sleep(1)
        
        dis1 = x - input_player1
        dis2 = x - input_player2
       
        if dis1 > dis2:
            print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player1))
            points_player1 += 1
            if dis1 == x:
                print("Glückwunsch", player1, "die richtige Zahl wurde getroffen.")
                points_player1 += 1
        elif input_player1 == input_player2: # wenn beide Spieler dieselbe Zahl haben
            print(f"{bcolors.YELLOW}%s hat die gleiche Zahl wie %s {bcolors.RESET_COLOR}"%(player1, player2))
            print("Somit bekommt keiner der bedien Spieler einen Punkt.")
        else: 
            print(f"{bcolors.GREEN}%s erhält einen Punkt{bcolors.RESET_COLOR}"%(player2))
            points_player2 += 1
            if dis2 == x:
                print("Glückwunsch", player2, "die richtige Zahl wurde getroffen.")
                points_player2 += 1
    print("Endstand:", player1, "hat", points_player1, "Punkte erzielt,", player2, "erzielte", points_player2, ". Herzlichen Glückwunsch")
    if points_player1 > points_player2:
        print("Herzlichen Glückwunsch!", player1, "du hast das Spiel gewonnen!")
    elif points_player2 > points_player1:
        print("Herzlichen Glückwunsch!", player2, "du hast das Spiel gewonnen!")
    else:
        print("Gleichstand. Dann müsst Ihr woll nochmal spielen :) ")

game_typ = int(input("Einfaches Spiel (nur eine Runde, keine Punktezählung) oder Erweitertes Spiel (mehrere Runden + Wiederholmöglichkeit, Punktezählung) \nEinfaches Spiel = 0 oder Erweitertes Spiel = 1?: "))

if game_typ == 1:
    game_normal()
elif game_typ == 0:
    game_easy()
else:
    False