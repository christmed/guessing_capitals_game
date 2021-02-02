import time
import random
import countries_capitals


def game_instructions():
    """Display game instructions."""

    greeting = f'\nWelcome to "Guess the Capital". Let\'s test your Geography knowledge!'
    instructions = "You will have 90 seconds to guess as much capitals of the world " \
                   "as you can.\n"
    instructions += "You will see a question like this:\n"

    question_example = "What is the capital of Westeros?\n"
    question_example += "a. King's Landing\n" \
                        "b. Winterfell\n" \
                        "c. Valyria\n" \
                        "d. Lannisport\n" \
                        "Option:\n"

    no_cheat = "Choose what you consider is the right option.\n"
    no_cheat += "Press 'Enter' on your keyboard after you choose the option.\n"
    no_cheat += "Googling is NOT allowed!!!"

    print(greeting)
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


def prompt_question(country, correct_ans):
    """Prompts questions and gets user answer.

    :param country: Subject of the question.
    :type country: str
    :param correct_ans: right answer of question.
    :type correct_ans: str
    :returns: option status (right or wrong).
    :rtype boolean
    """
    while True:
        print(f'What is the capital of {country}?')
        d_options = dict_options(answer_options)
        for k, v in d_options.items():
            print(k, v)
        option = input('\nOption: ')
        option_status = check_answer(d_options, option, correct_ans)
        if option_status is None:
            print("There isn't such option. Try again.")
            continue
        return option_status


def dict_options(answer_opts):
    """"Create a dict of answers for the current question.

    :param answer_opts: right and wrong answers.
    :type answer_opts: list
    :returns: a dictionary with the options and its answers.
    :rtype dict
    """
    d_options = {}
    for i in range(4):
        dict_option = {'abcd'[i]: answer_opts[i]}
        d_options.update(dict_option)
    return d_options


def check_answer(d_options, selected_opt, correct_ans):
    """Checks whether answer is right or wrong.

    :param d_options: possible answers.
    :type d_options: dict
    :param selected_opt: user answer.
    :type selected_opt: str
    :param correct_ans: correct answer of question.
    :type correct_ans: str
    :returns: True, False or None depending on the answer
        0 - incorrect
        1- correct
        None - Invalid option
    :rtype boolean or none
    """
    if selected_opt in d_options.keys():
        selected_answer = d_options[selected_opt]
    else:
        return None

    if selected_answer == correct_ans:
        return True
    else:
        return False


def game_stats(username, score, question_count, accuracy, streak):
    """Displays user game stats.

    :param username: name of user.
    :type username: str
    :param score: number of right answers responded.
    :type score: int
    :param question_count: number of questions responded.
    :type question_count: int
    :param accuracy: percentage of right answers.
    :type accuracy: float
    :param streak: largest guessing streak.
    :type streak: int
    """
    stats = f"Alright {username}, let's review your game stats.\n"
    stats += f"Final score: {score}.\n"
    stats += f"You got {score} out of {question_count} questions.\n"
    stats += f"Accuracy: {accuracy}%\n"
    stats += f"Longest streak: {streak}\n"
    print(stats)


name = input('Enter your name: ')
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

# Create a list of asked countries to avoid duplicates.
already_asked = list()

# Create a list to check for the longest streak.
data_streak = []
current_streak = 0
longest_streak = 0

score = 0
question_count = 0
start_time = time.time()
while True:
    # Create a 90 second timer for the game.
    end_time = time.time()
    timer = end_time - start_time
    if timer > 90:
        break
    # Get a random country.
    countries = list(f_capitals.keys())
    rand_country = random.choice(countries)
    if rand_country in already_asked:
        continue
    # Add country to list to avoid duplicates.
    already_asked.append(rand_country)

    # Get right and wrong answers.
    correct_answer = f_capitals[rand_country]
    wrong_answers = list(f_capitals.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, 3)
    answer_options = wrong_answers + [correct_answer]
    random.shuffle(answer_options)

    is_correct = prompt_question(rand_country, correct_answer)
    if is_correct:
        score += 1
        print('Well done!\n')
    else:
        print('Not quite.\n')
    question_count += 1

    data_streak.append(int(is_correct))

print("Time's up!\n")

# Get longest streak.
for i in data_streak:
    if i == 1:
        current_streak += 1
    else:
        longest_streak = max(longest_streak, current_streak)
        current_streak = 0

accuracy = round(score / question_count * 100, 0)
game_stats(name, score, question_count, accuracy, longest_streak)


