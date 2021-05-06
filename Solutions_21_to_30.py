"""Number 21"""
# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. Please write a program to compute the distance
# from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program:

# Input:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# Output:
# 2
""" Solution N. 21"""
# robot_0, robot_i = [0,0], [0,0]  # Robot's starting and new position (x_1, y_1), (x_2, y_2)
# distance = 0
# while True:
#     movement = input("where do you want to go?: ").lower()
#     if not movement:
#         break
#     try:
#         if movement[0] == 'u':  # for steps up
#             robot_i[1] = robot_i[1] + float(movement.strip('up '))
#         elif movement[0] == 'd':  # for steps down
#             robot_i[1] = robot_i[1] - float(movement.strip('down '))
#         elif movement[0] == 'l':  # for left steps
#             robot_i[0] = robot_i[0] - float(movement.strip('left '))
#         elif movement[0] == 'r':  # for right steps
#             robot_i[0] = robot_i[0] + float(movement.strip('right '))
#     except ValueError:
#         print("Enter a valid direction")

#     a = (robot_i[0] - robot_0[1])**2
#     print(f"This is the value of a: {a}")
#     b = (robot_i[1] - robot_0[1]) ** 2
#     distance = round((a+b)**(0.5))
#     robot_0 = robot_i
#     print(f"This is the distance from the last known position: {distance}")
