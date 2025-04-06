# PROBLEM STATEMENT:

# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


# SOLUTION👇
import tkinter as tk    #graphics library for buttons, drawings etc

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase(event):
    # Erase the squares when the eraser touches them
    x, y = event.x, event.y  # Get mouse position
    overlapping = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)  # Find objects under eraser
    
    for obj in overlapping:
        canvas.itemconfig(obj, fill="white")  # Change the square color to white (erase effect)

# main window
root = tk.Tk()
root.title("Grid Eraser")

# canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Draw the grid of blue squares
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        cell = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

# Bind mouse movement with left click to the erase function
canvas.bind("<B1-Motion>", erase)


root.mainloop()
