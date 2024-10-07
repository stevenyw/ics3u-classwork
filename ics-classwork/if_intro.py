# The if statements will change the code underneath it by applying the changes from the code on top of it. If its false, it'll skip the if statement.
# So the code doesn't mistake it for just printing it out by itself, and it'll only print it out if the if statement says the code is true.
# The += means num + 1, or take the number and add it by 1, and the -= means to take the number and minus it by one.

robot_location = 25
ball_location = 30
goal_location = 10
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False
