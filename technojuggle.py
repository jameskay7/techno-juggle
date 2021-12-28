from playsound import playsound
import random 

aeroDynamic = 'Aerodynamic.mp3'
superHeroes = 'SuperHeroes.mp3'
dltmgyd = 'DLTMGYD.mp3'
one_minute_to_midnight = 'One minute to midnight.mp3'
okPal = 'OK Pal.mp3'
touchIt = 'Touch It.mp3'
phantom = 'Phantom 2.mp3'
dance = 'D.A.N.C.E..mp3'
teenpregnancy = 'Teen Pregnancy.mp3'
#a list of all the songs to shuffle from 
songs = [aeroDynamic, superHeroes, dltmgyd, one_minute_to_midnight, okPal, touchIt, phantom, dance, teenpregnancy]

song_shuffled = False

#actual program 
print('Hello! What is your name?')
myInput = input()
print('Hello ' + myInput + ' Welcome to technojuggle, here is a tracklist of the songs available. ')
print('1. Aerodynamic - Daft Punk' "\n" "2. Superheroes - Daft Punk" "\n" '3. Justice - D.A.N.C.E' "\n" '4. Justice - One Minute to Midnight' "\n" '5. M83 - Ok Pal' "\n" '6. FatBoy Slim - Don\'t let the man get you down (Justice Remix)' "\n" '7. Daft Punk - Touch It/Technologic' "\n" '8. Justice - Phantom Pt.2 ')
choice = input("Would you like to shuffle your music? Type yes or no ")

randomSelect = random.choice(songs)
def shuffling(choice):
    for _ in songs:
        if choice == "yes":
            playsound(randomSelect)

shuffling(choice)
     
while not song_shuffled:
    songSelect = input("What song would you like to hear? ")
    if choice == "no":
        for song in songs:
            if songSelect == song in songs:
             playsound(song)
             break