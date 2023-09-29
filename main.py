from turtle import Screen, Turtle

my_scr = Screen()
my_scr.screensize(600, 600, "black")
my_scr.title("SNAKE GAME")
my_scr.tracer(0)
snake = []
delta = 0
fd = 1
game_is_on = True

for i in range(3):
    tim = Turtle("square")
    snake.append(tim)
    tim.pen(pendown=False, pencolor="white", fillcolor="white")
    tim.setpos(x=0 - delta, y=0)
    delta += 20

my_scr.update()

while game_is_on:
    # while (300, 300) > snake[0].pos() > (-300, -300):
    for body_item in snake:
        body_item.forward(fd)
        my_scr.update()
        if (-300, -300) > snake[0].pos() > (300, 0):
            # game_is_on = False
            fd = -fd


# print(snake[1].pos())
# print(snake[1].pos()<(0,0))


my_scr.exitonclick()
