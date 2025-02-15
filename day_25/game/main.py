# from sre_parse import State
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
tort = turtle.Turtle()
tort.hideturtle()
tort.penup()
question_title = "Guess the state"

data = pandas.read_csv("./game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []
score = 0

answer_state = ""
while score < 50 and answer_state is not None:
    answer_state = screen.textinput(question_title, "What's another states name?")
    if answer_state is not None and answer_state.title() in all_states:
        state = data[data.state == answer_state.title()]
        tort.goto(state.x.iloc[0], state.y.iloc[0])
        tort.write(state.state.iloc[0])
        guessed_states.append(state.state.iloc[0])
        score += 1
        question_title = f"{score}/50 States Correct"

if score != 50:
    missed_states = [state for state in all_states if state not in guessed_states]
    pandas.DataFrame(missed_states).to_csv("./states_to_learn.csv", index=False, header=False)
