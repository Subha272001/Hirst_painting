import turtle
import random

tim = turtle.Turtle()
my_screen = turtle.Screen()
turtle.colormode(255)
tim.speed("fastest")
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     randomcolor = (r, g, b)
#     return randomcolor
#

# def draw_spirograph(size_of_gap):
#     for _ in range(360//size_of_gap):
#         tim.circle(100)
#         tim.color(random_color())
#         current_heading = tim.heading()
#         tim.setheading(current_heading+size_of_gap)
#
#
# draw_spirograph(3)
# import colorgram
#
# colors = colorgram.extract('hirst_image.jpg', 30)
# print(colors)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

colors = [(207, 155, 102), (57, 107, 128), (162, 82, 43), (125, 79, 97), (122, 156, 171), (126, 175, 159), (195, 142, 39),
          (226, 198, 130), (188, 89, 109), (191, 131, 145), (14, 44, 57), (53, 38, 19), (51, 164, 128), (59, 121, 114),
          (218, 90, 70), (159, 22, 32), (41, 31, 33), (8, 30, 28), (81, 146, 165), (238, 167, 162), (156, 28, 21),
          (23, 80, 91), (233, 168, 173), (173, 206, 188), (106, 126, 157), (26, 87, 84)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 500
for dot_count in range(1,number_of_dots):
    tim.dot(10, random.choice(colors))
    tim.forward(20)

    if dot_count % 25 == 0:
        tim.setheading(90)
        tim.forward(20)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





my_screen.exitonclick()
