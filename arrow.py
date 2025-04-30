from math import sqrt

# CRIME SCENES with PERFECTLY MATCHED ARRIVAL TIMES
crime_scenes = {
    "The Glades": 4.47,      
    "Starling City Bank": 2.24, 
    "Queen Consolidated": 1.0,  
    "Starling General Hospital": 5.0, 
    "Starling City Port": 4.24, 
    "CNRI Law Office": 2.24    
}

locations = {
    "The Glades": (2, 8),
    "Starling City Bank": (6, 5),
    "Queen Consolidated": (5, 4),  # Very close to Verdant (4,4)
    "Starling General Hospital": (8, 7),
    "Starling City Port": (1, 1),
    "CNRI Law Office": (3, 5),
    "Verdant (Arrowcave)": (4, 4)  # The REAL BASE(The Night Club))
}

def distance(point1, point2):
    """Euclidean distance between two points."""
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def find_best_base(locations, crime_scenes):
    """Find the (x,y) point that minimizes error between distance & arrival time."""
    best_location = None
    best_score = float('inf')
    
    # Test every possible grid point (0-9 in x and y)
    for x in range(10):
        for y in range(10):
            total_error = 0
            
            # Compare against all crime scenes
            for scene_name, time in crime_scenes.items():
                scene_coords = locations[scene_name]
                dist = distance((x, y), scene_coords)
                error = abs(dist - time)
                total_error += error
            
            # Update best guess if this location fits better
            if total_error < best_score:
                best_score = total_error
                best_location = (x, y)
    
    return best_location, best_score

# Find the best base location
best_coords, score = find_best_base(locations, crime_scenes)

# Check if it matches Verdant's location
verdant_location = locations["Verdant (Arrowcave)"]
print(f" Calculated best base: {best_coords} (Error score: {score})")
print(f" Actual Arrowcave location: {verdant_location}")
print(" Algorithm correct?: ", best_coords == verdant_location)