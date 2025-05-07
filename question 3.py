import turtle

def draw_branch(t, branch_length, left_angle, right_angle, reduction_factor, depth):
    if depth == 0:
        return
    
    # Set color based on depth
    if depth == recursion_depth:
        t.pensize(10)  # Thick trunk
        t.color("brown")
    else:
        t.pensize(2)  # Thinner branches
        t.color("green")
    
    # Draw the branch
    t.forward(branch_length)
    
    # Left branch
    t.left(left_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1)
    
    # Right branch
    t.right(left_angle + right_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, reduction_factor, depth - 1)
    
    # Return to the original position
    t.left(right_angle)
    t.backward(branch_length)

def main():
    # Parameters (matching your example)
    left_angle = 20
    right_angle = 25
    starting_length = 100
    reduction_factor = 0.7
    global recursion_depth
    recursion_depth = 5

    # Set up turtle
    screen = turtle.Screen()
    screen.title("Recursive Tree")
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)  # Point upwards
    t.up()
    t.goto(0, -200)  # Start at the bottom center
    t.down()

    # Draw the tree
    draw_branch(t, starting_length, left_angle, right_angle, reduction_factor, recursion_depth)

    screen.mainloop()

if __name__ == "__main__":
    main()