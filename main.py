import turtle
import pandas
screen = turtle.Screen()
screen.title("India States/UT Game")
img = "india_states1.gif"
screen.addshape(img)
turtle.shape(img)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

SCORE = 0
data = pandas.read_csv("35_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 35:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/35 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        SCORE = int((len(guessed_states) / 35) * 100)
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            # t.goto(int(state_data.x), int(state_data.y))
            t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))

            t.write(answer_state)
            # t.write(state_data.state.item())

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(41, 151)
t.write(f"YOU GOT {SCORE}%")
for states in all_states:
    if states not in guessed_states:
        state_data = data[data.state == states]
        # t.goto(int(state_data.x), int(state_data.y))
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(states)

screen.exitonclick()
