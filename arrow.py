#I am gonna find you Arrow Man 

crime_scenes = {
    "The Glades": 3,
    "Starling City Bank": 5,
    "Queen Consolidated": 4,
    "Starling General Hospital": 6,
    "Starling City Port": 8,
    "CNRI law Office": 2      
}

#Now let's Map this out and by this I mean star city into a grid. 
locations = {
    "The Glades": (2, 8),
    "Starling City Bank": (6, 5),
    "Queen Consolidated": (5, 6),
    "Starling General Hospital": (8, 7),
    "Starling City Port": (1, 1),
    "CNRI law Office": (3, 7)     
}

#Now here's the deal we loop through our points in starling city and we see which one fits best. 
#Bacically the closer the distance from a suspectted base to a crime scene matches the arrival time... the better the guess. 

from math import sqrt

def distande(point1, point2):
    pass 

def find_best_base(locations, times):
    pass 

#I gotta think about it a bit. 