import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.widgets import Button

# ==== DARK MODE SETUP ====
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 8), facecolor='#0d1117')
ax.set_facecolor('#0d1117')

# Crime scene data (same as before)
locations = {
    "The Glades": (2, 8),
    "Starling City Bank": (6, 5),
    "Queen Consolidated": (5, 4),
    "Starling General Hospital": (8, 7),
    "Starling City Port": (1, 1),
    "CNRI Law Office": (3, 5),
    "Verdant (Arrowcave)": (4, 4)
}

crime_scenes = {
    "The Glades": 4.47,      
    "Starling City Bank": 2.24, 
    "Queen Consolidated": 1.0,  
    "Starling General Hospital": 5.0, 
    "Starling City Port": 4.24, 
    "CNRI Law Office": 2.24    
}

# ==== PLOT SETUP ====
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("FIND THE ARROW'S LAIR", fontsize=16, color='#58a6ff', fontweight='bold')
ax.grid(color='#30363d', linestyle='--')

# Plot crime scenes
for name, coords in locations.items():
    if name != "Verdant (Arrowcave)":
        ax.scatter(*coords, color='#ff7b72', s=150, edgecolors='white', zorder=4)
        ax.text(coords[0]+0.1, coords[1]+0.1, name, color='white', fontsize=9, zorder=5)
    else:
        verdant = ax.scatter(*coords, color='#58a6ff', s=200, marker='X', label='Actual Verdant', zorder=3)

# ==== ANIMATION ====
best_xy = (0, 0)
best_error = float('inf')

# Heatmap background (error visualization)
x_grid, y_grid = np.meshgrid(np.linspace(0, 10, 50), np.linspace(0, 10, 50))
error_grid = np.zeros_like(x_grid)

def update_heatmap():
    """Update the error heatmap (darker = worse fit)."""
    for i in range(len(x_grid)):
        for j in range(len(y_grid)):
            total_error = 0
            for scene, time in crime_scenes.items():
                dist = np.linalg.norm(np.array(locations[scene]) - np.array([x_grid[i,j], y_grid[i,j]]))
                total_error += abs(dist - time)
            error_grid[i,j] = total_error
    return ax.imshow(error_grid, extent=(0,10,0,10), origin='lower', 
                     cmap='inferno', alpha=0.3, vmin=0, vmax=50)

heatmap = update_heatmap()

# Animation function
def update(frame):
    global best_xy, best_error
    x, y = frame // 10, frame % 10
    
    # Calculate error for this (x,y)
    total_error = 0
    for scene, time in crime_scenes.items():
        dist = np.linalg.norm(np.array(locations[scene]) - np.array([x, y]))
        total_error += abs(dist - time)
    
    # Update best guess
    if total_error < best_error:
        best_error = total_error
        best_xy = (x, y)
        best_point.set_offsets([x, y])
    
    # Update current search point
    current_point.set_offsets([x, y])
    return current_point, best_point, heatmap

# Plot elements
current_point = ax.scatter([], [], color='#f78166', s=100, label='Current Test', zorder=4)
best_point = ax.scatter([], [], color='#3fb950', s=300, marker='*', label='Best Guess', zorder=5)

# ==== BUTTON ====
button_ax = plt.axes([0.4, 0.05, 0.2, 0.075])
button = Button(button_ax, 'START SEARCH', color='#238636', hovercolor='#2ea043')
button.label.set_color('white')

def start(event):
    anim = FuncAnimation(fig, update, frames=100, interval=100, blit=True)
    plt.draw()

button.on_clicked(start)

# Legend and final touches
ax.legend(loc='upper right', facecolor='#0d1117')
plt.tight_layout()
plt.show()