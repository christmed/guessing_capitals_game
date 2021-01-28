import time
import random
import countries_capitals


def game_instructions():
    """Display game instructions."""

    instructions = 'Welcome to "Guess the Capital".\n'
    instructions += "You will have 90 seconds to guess as much world capitals " \
                    "as you can.\n"
    instructions += "\nYou will see a question like this:"

    question_example = "What is the capital of Westeros?\n"
    question_example += "a. King's Landing\n" \
                        "b. Winterfell\n" \
                        "c. Valyria\n" \
                        "d. Lannisport\n" \
                        "Option:\n"

    no_cheat = "Choose what you consider is the right option."
    no_cheat += "\nYou will have 3 seconds per question. "
    no_cheat += "Googling is NOT allowed!!!"

    print(instructions)
    print(question_example)
    print(no_cheat)


# Show instructions.
game_instructions()

# Store game data. Keys are countries and values are their capitals.
capitals = countries_capitals.capitals
random.shuffle(capitals)

start_time = time.time()
score = 0

while True:
    # Create a 90 second timer for the game.
    end_time = time.time()
    if end_time - start_time >= 5:
        break

    f_capitals = {}
    # Flatten capitals dictionary.
    for dict in capitals:
        cty_cap = {dict['country']: dict['city']}
        f_capitals.update(cty_cap)

    # Get a random country.
    countries = list(f_capitals.keys())
    rand_country = random.choice(countries)

    # Consider using a recursive function.
    already_asked = list()
    already_asked.append(rand_country)

    # Get right and wrong answers.
    correct_answer = f_capitals[rand_country]
    wrong_answers = list(f_capitals.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, 3)
    answer_options = wrong_answers + [correct_answer]
    random.shuffle(answer_options)
    print(answer_options)

print("Time's over!")
