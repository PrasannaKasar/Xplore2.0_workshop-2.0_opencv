

# Drawing_Shapes 

# TODO 1: Draw a straight horizontal line using a for loop

for x in range(70, 150): 
    canvas[230, x] = (200, 200, 200)


# TODO 2: Draw a filled circle using nested for loops

cx, cy = 190, 160  
r = 30   

for y in range(cy - r, cy + r + 1):
    for x in range(cx - r, cx + r + 1):
        if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
            canvas[y, x] = (0, 200, 255)