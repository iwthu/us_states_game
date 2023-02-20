import turtle, pandas, text_module

states_data = pandas.read_csv("./game/50_states.csv")
wow = states_data["state"]
wow = wow.to_list()

s = turtle.Screen()
s.setup(700, 500)
s.bgpic("./game/blank_states_img.gif")

when_right = text_module.TextOnScreen()

score = 0
game_on = True
guessed_data = []
while game_on:
    guess = str(s.textinput(f"Score: {score}/50", "Write down the name of the states that you know! Type 'Exit' to exit the game."))
    if guess.title() in wow and guess not in guessed_data:
        guess_data = states_data[states_data.state == guess]
        guess_state_name = guess_data["state"].to_list()
        guess_states_cord_data = (int(guess_data.x), int(guess_data.y))
        when_right.write_down_guess(guess_state_name[0], guess_states_cord_data)
        guessed_data.append(guess)
        score += 1
    elif guess.title() in guessed_data:
        easter_egg = s.textinput("Nah", "You already wrote that! >:C").title()
        if easter_egg == "Fuck you" or easter_egg == "F u" or easter_egg == "Fuck u":
            s.bgpic("./game/stop.gif")
            s.setup(650, 450)
            s.textinput("Stop right there! Criminal scum!", "You violated the law. Pay the court a fine or serve your "
                                                            "sentence. Your stolen goods are now forfeit.")
            game_on = False
    elif guess is None:
        continue
    if score == 50:
        s.textinput("WOW!", "You won! Do you proud of yourself?")
        s.textinput("lol", "I dont care actually :^)")
        game_on = False
    if guess.title() == "Exit":
        not_guessed = [state for state in wow if state not in guessed_data]
        data_new = pandas.DataFrame(not_guessed)
        save = s.textinput("Hey!", "I'll create a file with stated that you didn't guess. If that is okay type 'y'.")
        if save.title() == 'y':
            data_new.to_csv("learn_this.csv")
            game_on = False
        else:
            game_on = False
        break
