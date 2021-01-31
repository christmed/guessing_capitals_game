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


def countdown():
    """"Simulates a countdown."""

    print('Are you ready?')
    time.sleep(1)
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    print('Here we go!\n')


def dict_options(answer_opts):
    """"Create a dict of answers for the current question.

    :param answer_opts: right and wrong answers.
    :type answer_opts: list
    :returns: a dictionary with the options and its answers.
    :rtype: dict
    """
    d_options = {}
    for i in range(4):
        dict_option = {'abcd'[i]: answer_opts[i]}
        d_options.update(dict_option)
    return d_options


def check_answer(d_options, selected_opt, correct_ans):
    """Checks whether answer is right or wrong.

    :param d_options: dict of possible answers.
    :type d_options: dict
    :param selected_opt: user answer
    :type selected_opt: str
    :param correct_ans: correct answer of question.
    :type correct_ans: str
    :returns: True, False or None depending of the answer
        0 - incorrect
        1- correct
        None - Invalid option
    :rtype boolean or none"""

    if selected_opt in d_options.keys():
        selected_answer = d_options[selected_opt]
    else:
        print("There isn't such option. Try again.")
        return None

    if selected_answer == correct_ans:
        return True
    else:
        return False


# Show instructions.
game_instructions()
countdown()

# Store game data. Keys are countries and values are their capitals.
capitals = countries_capitals.capitals
random.shuffle(capitals)

f_capitals = {}
# Flatten capitals dictionary.
for d in capitals:
    cty_cap = {d['country']: d['city']}
    f_capitals.update(cty_cap)

# Create list of asked countries to avoid duplicates.
already_asked = list()

# Create a 90 second timer for the game.
start_time = time.time()
end_time = time.time()
timer = end_time - start_time
score = 0
question_count = 0
while timer < 90:
    # Get a random country.
    countries = list(f_capitals.keys())
    rand_country = random.choice(countries)
    if rand_country in already_asked:
        continue

    # Consider using a recursive function.
    already_asked.append(rand_country)

    # Get right and wrong answers.
    correct_answer = f_capitals[rand_country]
    wrong_answers = list(f_capitals.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, 3)
    answer_options = wrong_answers + [correct_answer]
    random.shuffle(answer_options)

    # Create list of correct answers to compare with user choices.
    correct_answers = list()
    correct_answers.append(correct_answer)

    # Displays the question and its possible answers.
    print(f'What is the capital of {rand_country}?')
    d_options = dict_options(answer_options)
    for k, v in d_options.items():
        print(k, v)
    print('')
    option = input('Option: ')
    print('')

print("Time's over!")
