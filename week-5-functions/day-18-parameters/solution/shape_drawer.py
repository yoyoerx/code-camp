# Day 18 — SOLUTION: Shape Drawer

def draw_line(symbol, length):
    print(symbol * length)

def draw_box(symbol, height, width):
    for row in range(height):
        print(symbol * width)

# Try them out:
draw_line("=", 20)
print()
draw_box("#", 3, 8)
print()
draw_box("@", 5, 5)
print()
draw_line("=", 20)
