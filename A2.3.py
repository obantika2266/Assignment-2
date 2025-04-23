import turtle

def draw_branch(branch_length, depth, left_angle, right_angle, reduction_factor):
    if depth == 0 or branch_length < 1:
        return

    # Draw main branch
    turtle.pensize(max(1, depth))  # Thicker base
    turtle.forward(branch_length)

    # Left branch
    turtle.left(left_angle)
    turtle.color("green")
    draw_branch(branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)

    # Right branch
    turtle.right(left_angle + right_angle)
    draw_branch(branch_length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)

    # Reset position and heading
    turtle.left(right_angle)
    turtle.penup()
    turtle.backward(branch_length)
    turtle.pendown()

def main():
    # Get user inputs
    left_angle = float(input("Enter left branch angle (degrees): "))
    right_angle = float(input("Enter right branch angle (degrees): "))
    start_length = float(input("Enter starting branch length (pixels): "))
    depth = int(input("Enter recursion depth: "))
    reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))

    # Set up turtle
    turtle.title("Recursive Tree")
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.color("brown")

    # Start drawing
    draw_branch(start_length, depth, left_angle, right_angle, reduction_factor)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
