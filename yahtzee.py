"""
# COMP-1510-Final-Exam
# Name: Xian Yang (Sean)
# Student Number: A01042774
"""
import re
import random
import doctest


def roll_dice(times: int) -> []:
    """

    Roll multiple (maximum 5 dice) six-sided dice and return result in a list.

    :precondition: times must between 1 and 5 inclusive
    :postcondition: give (times) dice rolling result correctly
    :return: a list that contains (times) dice number.
    """
    if times < MIN_DICE_ON_THE_TABLE_TO_ROLL() or times > MAX_DICE_ON_THE_TABLE():
        print('Insufficient number of dice for re-roll.')
        return []
    else:
        dice_list = []
        for number_of_dice in range(ONE(), times + 1):
            dice_list.append(random.randint(ONE(), SIX()))
        return dice_list


def GENERATE_RESULT_SCORE_BOARD() -> dict:
    """

    Generate a dictionary as score board for a player to record scores (Constant function)

    :return: a dictionary with strategies as keys and 0 as values
    """
    return {'Ones': NO_SCORE(), 'Twos': NO_SCORE(), 'Threes': NO_SCORE(), 'Fours': NO_SCORE(), 'Fives': NO_SCORE(),
            'Sixes': NO_SCORE(), 'Three of a kind': NO_SCORE(), 'Four of a kind': NO_SCORE(), 'Full house': NO_SCORE(),
            'Small straight': NO_SCORE(), 'Large straight': NO_SCORE(), 'Chance': NO_SCORE(), 'Yahtzee': NO_SCORE()}


def GENERATE_STRATEGY_FUNCTIONS_DICTIONARY() -> dict:
    """

    Generate a dictionary for strategies name paired with their corresponding functions (Constant function)

    :return: a dictionary with strategies as keys and function object as values
    """
    return {'Ones': ones, 'Twos': twos, 'Threes': threes, 'Fours': fours, 'Fives': fives, 'Sixes': sixes,
            'Three of a kind': three_of_a_kind, 'Four of a kind': four_of_a_kind, 'Full house': full_house,
            'Small straight': small_straight, 'Large straight': large_straight, 'Chance': chance, 'Yahtzee': yahtzee}


def keep_dice(player_kept: [], dice_wanted_to_keep: [], dice_on_table: []) -> None:
    """

    Add dice that player wants to keep to player_kept if they are available on the table.

    :param player_kept: a list that contains dice kept by player
    :param dice_wanted_to_keep: a list that contains dice that player wanted to keep
    :param dice_on_table: a list that contains dice that are available to keep
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length must between 0 to 5;
                    dice_wanted_to_keep must be a list contains a list of number from 1 to 6, length must between 1 to 5;
                    dice_on_table must be a list contains a list of number from 1 to 6,
                    length must equals to 5 - len(player_kept);
                    Sum of length of player_kept and dice_wanted_to_keep must between 1 to 5
    :postcondition: put all dice in dice_wanted_to_keep to player_player_kept if they are availble on the table

    >>> test_player_kept = [2]
    >>> test_dice_wanted_to_keep = [2,2,2]
    >>> test_dice_on_the_table = [1, 2, 2, 2, 6]
    >>> keep_dice(test_player_kept, test_dice_wanted_to_keep, test_dice_on_the_table)
    You successfully kept 2.
    You successfully kept 2.
    You successfully kept 2.
    >>> print(test_player_kept)
    [2, 2, 2, 2]

    >>> test_player_kept = [2, 4, 6]
    >>> test_dice_wanted_to_keep = [2,5]
    >>> test_dice_on_the_table = [1, 2, 2, 2, 6]
    >>> keep_dice(test_player_kept, test_dice_wanted_to_keep, test_dice_on_the_table)
    You successfully kept 2.
    5 is not on the table, you can't keep it.
    >>> print(test_player_kept)
    [2, 4, 6, 2]

    >>> test_player_kept = [4,4]
    >>> test_dice_wanted_to_keep = [2,3,4,5]
    >>> test_dice_on_the_table = [1, 2, 2, 2, 6]
    >>> keep_dice(test_player_kept, test_dice_wanted_to_keep, test_dice_on_the_table)
    You can't have more than 5 dice.
    >>> print(test_player_kept)
    [4, 4]
    """
    if len(dice_wanted_to_keep) + len(player_kept) > MAX_DICE_TO_KEEP():
        print("You can't have more than 5 dice.")
    else:
        for die in dice_wanted_to_keep:
            if die in dice_on_table:
                player_kept.append(die)
                print(f"You successfully kept {die}.")
            else:
                print(f"{die} is not on the table, you can't keep it.")


def put_back_dice(player_kept: [], dice_wanted_to_put_back: [], dice_on_table: []) -> None:
    """

    Remove dice in dice_wanted_to_put_back from dice that player kept and put them back to dice_on_table.

    :param player_kept: a list that contains dice kept by player
    :param dice_wanted_to_put_back: a list that contains dice that play wanted to put back to table
    :param dice_on_table: a list that contains dice that are available to keep
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length must between 1 to 5;
                    dice_wanted_to_put_back must be a sublist of player_kept.
                    dice_on_table must be a list contains a list of number from 1 to 6,
                    length must equals to 5 - len(player_kept);
    :postcondition: remove all dice in dice_wanted_to_put_back from player_player_kept and put them back to table.

    >>> test_player_kept = [2,4,5,6]
    >>> test_dice_wanted_to_put_back = [2]
    >>> test_dice_on_table = [6]
    >>> put_back_dice(test_player_kept, test_dice_wanted_to_put_back, test_dice_on_table)
    You successfully put 2 back.
    >>> print(test_player_kept)
    [4, 5, 6]
    >>> print(test_dice_on_table)
    [6, 2]

    >>> test_player_kept = [1,2,4,5,6]
    >>> test_dice_wanted_to_put_back = [2,5,6]
    >>> test_dice_on_table = []
    >>> put_back_dice(test_player_kept, test_dice_wanted_to_put_back, test_dice_on_table)
    You successfully put 2 back.
    You successfully put 5 back.
    You successfully put 6 back.
    >>> print(test_player_kept)
    [1, 4]
    >>> print(test_dice_on_table)
    [2, 5, 6]
    """
    for die in dice_wanted_to_put_back:
        if die in player_kept:
            player_kept.remove(die)
            dice_on_table.append(die)
            print(f"You successfully put {die} back.")
        else:
            print(f"You don't own {die} so you can't put it back.")


def play_one_round(score_board: dict, yahtzee_bonus: int) -> int:
    """

    Play one round of game and update result score in player's score board. Return processed yahtzee_bonus for further
    processing.

    :param score_board: a dictionary with strategies as keys and corresponding score as values
    :param yahtzee_bonus: an integer representing how many yahtzee the player rolled.
    :precondition: score_board must be a valid score board dictionary
    :postcondition: play one round of yahtzee and record player's score in this round correctly
    """
    player_kept = []
    roll_times = MAX_ROLL_TIME()
    strategy_inventory = GENERATE_STRATEGY_FUNCTIONS_DICTIONARY()
    while roll_times > END_GAME():
        dice_in_table = roll_dice(MAX_DICE_ON_THE_TABLE() - len(player_kept))
        print(f'dice on the table are:{dice_in_table}, you have {roll_times - 1} chances to roll.')
        [roll_times, yahtzee_bonus] = game_engine(roll_times, player_kept, score_board, strategy_inventory,
                                                  yahtzee_bonus, dice_in_table)
        if roll_times == END_GAME():
            yahtzee_bonus = record_score(roll_times, player_kept, score_board, strategy_inventory, yahtzee_bonus)[2]
    return yahtzee_bonus


def calculate_top_bonus(score_board: dict) -> None:
    """

    Check if score over 63 points in number sections. If yes, assign 30 to Number bonus in score_board, 0 otherwise.

    :param score_board: a dictionary with strategies as keys and corresponding score as values
    :precondition: score_board must be a valid score board dictionary
    :postcondition: update value associated to bonus for numbers section.

    >>> test_score_board = GENERATE_RESULT_SCORE_BOARD()
    >>> calculate_top_bonus(test_score_board)
    >>> print(test_score_board['Number bonus'])
    0

    >>> test_score_board = {'Ones': 5, 'Twos': 10, 'Threes': 15, 'Fours': 20, 'Fives': 25, 'Sixes': 30, \
                            'Three of a kind': NO_SCORE(), 'Four of a kind': NO_SCORE(), 'Full house': NO_SCORE(), \
                            'Small straight': NO_SCORE(), 'Large straight': NO_SCORE(), \'Chance': NO_SCORE(), \
                            'Yahtzee': NO_SCORE()}
    >>> calculate_top_bonus(test_score_board)
    >>> print(test_score_board['Number bonus'])
    35
    """
    if score_board['Ones'] + score_board['Twos'] + score_board['Threes'] + score_board['Fours'] + score_board['Fives'] \
            + score_board['Sixes'] > TOP_BONUS_BOUNDARY():
        score_board['Number bonus'] = TOP_BONUS_SCORE()
    else:
        score_board['Number bonus'] = ZERO()


def calculate_yahtzee_bonus(yahtzee_bonus_counter: int, score_board: dict) -> None:
    """

    Check if player rolled more than once yahtzee. If yes, assign 100*yahtzee_counter to Yahtzee bonus in score_board.

    :param yahtzee_bonus_counter: an integer representing how many yahtzee the player rolled.
    :param score_board: a dictionary with strategies as keys and corresponding score as values
    :precondition: score_board must be a valid score board dictionary; yahtzee_counter must be a non-negative integer,
                    yahtzee bonus must be 0 if value of 'Yahtzee' in score_board is zero.
    :postcondition: update value associated to bonus for yahtzee.

    >>> test_score_board = {'Ones': 5, 'Twos': 10, 'Threes': 15, 'Fours': 20, 'Fives': 25, 'Sixes': 30, \
    'Three of a kind': 13, 'Four of a kind': 22, 'Full house': 25, 'Small straight': 30, 'Large straight': 0, \
    'Chance': 18, 'Yahtzee': 0}
    >>> test_yahtzee_bonus_counter = 0
    >>> calculate_yahtzee_bonus(test_yahtzee_bonus_counter, test_score_board)
    >>> print(test_score_board['Yahtzee bonus'])
    0

    >>> test_score_board = {'Ones': 5, 'Twos': 10, 'Threes': 15, 'Fours': 20, 'Fives': 25, 'Sixes': 30, \
    'Three of a kind': 13, 'Four of a kind': 22, 'Full house': 25, 'Small straight': 30, 'Large straight': 0, \
    'Chance': 18, 'Yahtzee': 50}
    >>> test_yahtzee_bonus_counter = 1
    >>> calculate_yahtzee_bonus(test_yahtzee_bonus_counter, test_score_board)
    >>> print(test_score_board['Yahtzee bonus'])
    100
    """
    if score_board['Yahtzee'] == ZERO():
        score_board['Yahtzee bonus'] = ZERO()
    else:
        score_board['Yahtzee bonus'] = yahtzee_bonus_counter * YAHTZEE_BONUS_MULTIPLIER()


def game_engine(roll_times: int, player_kept: [], score_board: dict, strategy_inventory: dict,
                yahtzee_bonus: int, dice_on_the_table: []) -> []:
    """

    The game engine which process player's choice, display and update player information.

    :param roll_times: an integer representing how many times the player can re-roll dice.
    :param player_kept: a list that contains dice kept by player
    :param score_board: a dictionary with strategies as keys and corresponding score as values
    :param strategy_inventory: a dictionary with strategies as keys and corresponding score as values
    :param yahtzee_bonus: an integer representing the number of extra yahtzee
    :param dice_on_the_table: a list that contains dice that are available to keep
    :precondition: player_kept, dice_on_the_table must be empty or contain a list of number from 1 to 6,
                    length must equals to 5; roll_times, player_pick and yahtzee_bonus must be non-negative integers;
                    score_board must be a valid score board dictionary;
    :postcondition: process player's choice and update score correctly
    :return: the processed Yahtzee bonus counter
    """
    switch = True
    while switch:
        try:
            player_choice_option = int(input(f"Dice in your pocket is/are: {player_kept}, Please pick an option: \n"
                                             f"(CAUTION: When you have 0 chances to roll: "
                                             f"1 and 3 won't work; "
                                             f"pick 2 to keep final 5 dice and pick strategy)\n"
                                             f"1. Re-roll now. \n"
                                             f"2. Keep dice you want and re-roll dice on the table.\n"
                                             f"3. Put you kept dice back and keep new dice, "
                                             f"then re-roll dice on the table.\n"
                                             f"4. Pick a strategy and record you score. "
                                             f"(Only when you have kept 5 dice)\n"))
        except ValueError:
            print('Invalid input.')
        else:
            if player_choice_option == 1 or player_choice_option == 2 or player_choice_option == 3:
                [roll_times, switch] = re_roll_option_handle(player_choice_option, player_kept, roll_times,
                                                             dice_on_the_table)
            elif player_choice_option == 4:
                [switch, roll_times, yahtzee_bonus] = record_score(roll_times, player_kept, score_board,
                                                                   strategy_inventory, yahtzee_bonus)
            else:
                print("You entered an invalid option, please try again.")
    return [roll_times, yahtzee_bonus]


def re_roll_option_handle(player_choice_option: int, player_kept: [], roll_times: int, dice_on_the_table: []) -> []:
    """

    Handle options 1, 2 and 3 which move player to re-roll process; 1 will re-roll directly, 2 will keep dice then
    re-roll, and 3 will put back dice then re-roll; return roll_times-1 and false as guardian variables to allow player
    exit outer loop.

    :param player_choice_option: an integer representing the option chosen by player.
    :param player_kept: a list that contains dice kept by player
    :param roll_times: an integer representing how many times the player can re-roll dice.
    :param dice_on_the_table: a list that contains dice that are available to keep
    :precondition: player_kept, dice_on_the_table must be empty or contain a list of number from 1 to 6,
                    length must equals to 5; roll_times and player_choice_option must be non-negative integers;
                    player_choice_option can only be 1, 2 or 3
    :postcondition: process player's choice and update guardian variables correctly
    :return: a list contains roll_times - 1 and a boolean variable False

    """
    try:
        if int(player_choice_option) == 2:
            dice_wanted_to_keep = [int(die) for die in input('Please enter the dice you want to '
                                                             'keep, no delimiter, i.e 12345:\n'
                                                             'CAUTION: please enter valid dice '
                                                             'number, otherwise you will lose a '
                                                             're-roll chance.\n').strip()]
            keep_dice(player_kept, dice_wanted_to_keep, dice_on_the_table)
        elif int(player_choice_option) == 3:
            dice_wanted_to_put_back = [int(die) for die in input('Please enter the dice you want to put back, '
                                                                 'no delimiter, i.e 12345:\n'
                                                                 'CAUTION: please enter valid dice '
                                                                 'number, otherwise you will lose a '
                                                                 're-roll chance.\n').strip()]
            put_back_dice(player_kept, dice_wanted_to_put_back, dice_on_the_table)
            keep_new_dice_or_not = int(input('Do you want to keep new dice, enter 1 if yes, 0 if no.'))
            if keep_new_dice_or_not == 1:
                dice_wanted_to_keep = [int(die) for die in input('Please enter the dice you want to '
                                                                 'keep, no delimiter, i.e 12345:\n'
                                                                 'CAUTION: please enter valid dice '
                                                                 'number, otherwise you will lose a '
                                                                 're-roll chance.\n').strip()]
                keep_dice(player_kept, dice_wanted_to_keep, dice_on_the_table)
    except ValueError:
        print('Input dice are invalid. You lose a re-roll chance.')
    return [roll_times - 1, False]


def record_score(roll_times: int, player_kept: [], score_board: dict, strategy_inventory: dict, yahtzee_bonus: int) \
        -> []:
    """

    Update player's score on score board if player successfully scored in his selected strategy. Return
    processed yahtzee bonus counter, and two guardian variables to outer loop for existing while loop.

    :param roll_times: an integer representing how many times the player can re-roll dice.
    :param player_kept: a list that contains dice kept by player
    :param score_board: a dictionary with strategies as keys and corresponding score as values
    :param strategy_inventory: a dictionary with strategies as keys and corresponding functions as values
    :param yahtzee_bonus: an integer representing the number of extra yahtzee
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length must equals to 5;
                    player_pick and yahtzee_bonus must be non-negative integers;
                    roll_time must be non-negative integer less than or equals to 3;
                    score_board must be a valid score board dictionary;
    :postcondition: validate player's combination and record score correctly.
    :return: a list that contains a boolean value representing a guardian variable to exist outer loop,
            processed Yahtzee bonus and roll_time,

    """
    if len(player_kept) == MAX_DICE_TO_KEEP():
        print(f'Available Strategy:')
        for index, strategy in enumerate(list(score_board.keys()), 1):
            print(f"{index}. {strategy}")
        player_pick = input('Please enter the number associated with the strategy you want to pick.\n')
        try:
            strategy_name = list(score_board.keys())[int(player_pick) - 1]
        except ValueError:
            print("Invalid strategy input.")
        else:
            if score_board[strategy_name] < ZERO() or strategy_name == 'Yahtzee':
                yahtzee_bonus = update_score_by_strategy(player_kept, strategy_inventory, player_pick, score_board,
                                                         yahtzee_bonus)
                roll_times -= ROLL_TIMES_KILLER()
                return [False, roll_times, yahtzee_bonus]
            else:
                print("Score already exist, return to the previous menu.")
    else:
        print('Please keep exactly 5 dice to make up your combination.')
    return [True, roll_times, yahtzee_bonus]


def update_score_by_strategy(player_kept: [], strategy_inventory: dict, player_pick: str, score_board: dict,
                             yahtzee_bonus: int) -> int:
    """

    Check if strategy picked by player is available. If yes, update player score board.
    Update Yahtzee bonus counter at the end if applicable.

    :param player_kept: a list that contains dice kept by player
    :param strategy_inventory: a dictionary with strategies as keys and corresponding functions as values
    :param player_pick: an integer representing corresponding strategy
    :param score_board: a dictionary with strategies as keys and corresponding score as values
    :param yahtzee_bonus: an integer representing the number of extra yahtzee
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length must equals to 5;
                    player_pick and yahtzee_bonus must be non-negative integers;
                    score_board must be a valid score board dictionary;
    :postcondition: update value associated to strategy picked by player correctly and return
                    processed Yahtzee bonus counter
    :return: the processed Yahtzee bonus counter

    >>> test_score_board = {'Ones': NO_SCORE(), 'Twos': NO_SCORE(), 'Threes': NO_SCORE(), 'Fours': NO_SCORE(), \
                            'Fives': NO_SCORE(), 'Sixes': NO_SCORE(), 'Three of a kind': NO_SCORE(), \
                            'Four of a kind': NO_SCORE(), 'Full house': NO_SCORE(), 'Small straight': NO_SCORE(),\
                            'Large straight': NO_SCORE(), 'Chance': NO_SCORE(), 'Yahtzee': NO_SCORE()}
    >>> test_strategy_inventory = {'Ones': ones, 'Twos': twos, 'Threes': threes, 'Fours': fours, 'Fives': fives,\
                                   'Sixes': sixes, 'Three of a kind': three_of_a_kind,\
                                   'Four of a kind': four_of_a_kind, 'Full house': full_house,\
                                   'Small straight': small_straight, 'Large straight': large_straight,\
                                   'Chance': chance, 'Yahtzee': yahtzee}
    >>> test_player_kept = [1,2,4,5,2]
    >>> test_player_pick = '2'
    >>> test_yahtzee_bonus = 0
    >>> update_score_by_strategy(test_player_kept, test_strategy_inventory, test_player_pick, test_score_board, \
    test_yahtzee_bonus)
    0
    >>> print(test_score_board['Twos'])
    4

    >>> test_score_board = {'Ones': NO_SCORE(), 'Twos': NO_SCORE(), 'Threes': NO_SCORE(), 'Fours': NO_SCORE(), \
                            'Fives': NO_SCORE(), 'Sixes': NO_SCORE(), 'Three of a kind': NO_SCORE(), \
                            'Four of a kind': NO_SCORE(), 'Full house': NO_SCORE(), 'Small straight': NO_SCORE(),\
                            'Large straight': NO_SCORE(), 'Chance': NO_SCORE(), 'Yahtzee': NO_SCORE()}
    >>> test_strategy_inventory = {'Ones': ones, 'Twos': twos, 'Threes': threes, 'Fours': fours, 'Fives': fives,\
                                   'Sixes': sixes, 'Three of a kind': three_of_a_kind,\
                                   'Four of a kind': four_of_a_kind, 'Full house': full_house,\
                                   'Small straight': small_straight, 'Large straight': large_straight,\
                                   'Chance': chance, 'Yahtzee': yahtzee}
    >>> test_player_kept = [2,2,3,5,4]
    >>> test_player_pick = '10'
    >>> test_yahtzee_bonus = 0
    >>> update_score_by_strategy(test_player_kept, test_strategy_inventory, test_player_pick, test_score_board, \
    test_yahtzee_bonus)
    0
    >>> print(test_score_board['Small straight'])
    30
    """
    if 1 <= int(player_pick) <= 13:
        strategy_name = list(score_board.keys())[int(player_pick) - 1]
        if score_board[strategy_name] < 0:
            score_board[strategy_name] = strategy_inventory[strategy_name](player_kept)
        else:
            if strategy_name == 'Yahtzee':
                if strategy_inventory[strategy_name](player_kept) == 50:
                    if score_board[strategy_name] == 50:
                        yahtzee_bonus += 1
                        print('Another Yahtzee?! Really?!')
                    elif score_board[strategy_name] == 0:
                        print('You gave up Yahtzee before, so Yahtzee gives you up this time.')
                    else:
                        score_board[strategy_name] = strategy_inventory[strategy_name](player_kept)
                else:
                    print("I know you wish but you didn't get Yahtzee this time, please pick another.")
    else:
        print('Invalid option number.')
    return yahtzee_bonus


def game():
    """

    Two players Yahtzee game, multiple rounds; After all strategies are filled in by corresponding scores for
    both player, check bonus for numbers section and extra yahtzee, update these bonus if any.
    Example:
    1. Initialize two score boards for players
    2. Run play_one_round() for each play alternatively until all strategies for both score boards are filled in.
    3. Check if players get bonus, add it to their score board if any.
    4. Game ended.

    """
    player_one_score_board = GENERATE_RESULT_SCORE_BOARD()
    player_two_score_board = GENERATE_RESULT_SCORE_BOARD()
    player_one_yahtzee_bonus_counter = ZERO()
    player_two_yahtzee_bonus_counter = ZERO()
    while list(player_one_score_board.values()).count(NO_SCORE()) + \
            list(player_two_score_board.values()).count(NO_SCORE()) > EMPTY():
        print("\nPlayer 1's turn: ")
        player_one_yahtzee_bonus_counter = play_one_round(player_one_score_board, player_one_yahtzee_bonus_counter)
        print(f"Score updated, player 1's score is now:")
        print_score_board(player_one_score_board)
        print("\nPlayer 2's turn: ")
        player_two_yahtzee_bonus_counter = play_one_round(player_two_score_board, player_two_yahtzee_bonus_counter)
        print(f"Score updated, player 2's score is now:")
        print_score_board(player_two_score_board)
    calculate_top_bonus(player_one_score_board)
    calculate_top_bonus(player_two_score_board)
    calculate_yahtzee_bonus(player_one_yahtzee_bonus_counter, player_one_score_board)
    calculate_yahtzee_bonus(player_two_yahtzee_bonus_counter, player_two_score_board)
    print(f"Player one scored: {sum(list(player_one_score_board.values()))},\n"
          f"Player two scored: {sum(list(player_two_score_board.values()))},\n")


def print_score_board(score_board: dict) -> None:
    """

    Print score_board in a certain format.

    :param score_board: a dictionary with strategies as keys and corresponding score as values
    :precondition: score_board must be a dictionary in valid score board format
    :postcondition: print out the input score board in correct format

    """
    print("-----------------------------------------------")
    for key in score_board.keys():
        if score_board[key] < 0:
            print(f"{key}: No score")
        else:
            print(f"{key}: {score_board[key]}")


# Constant functions
def NO_SCORE() -> int:
    """

    Return -1 which representing no score

    :return: -1
    """
    return -1


def ZERO() -> int:
    """

    Constant function: return constant 0 representing 0 score.

    :return: 0
    """
    return 0


def ONE() -> int:
    """

    Constant function: return constant 1 representing score or number of items.

    :return: 1
    """
    return 1


def TWO() -> int:
    """

    Constant function: return constant 2 representing score or number of items.

    :return: 2
    """
    return 2


def THREE() -> int:
    """

    Constant function: return constant 3 representing score or number of items.

    :return: 3
    """
    return 3


def FOUR() -> int:
    """

    Constant function: return constant 4 representing score or number of items.

    :return: 4
    """
    return 4


def FIVE() -> int:
    """

    Constant function: return constant 5 representing score or number of items.

    :return: 5
    """
    return 5


def SIX() -> int:
    """

    Constant function: return constant 6 representing score or number of items.

    :return: 6
    """
    return 6


def ROLL_TIMES_KILLER():
    """

    Constant function: a large constant 99 representing a variable used to surely kill roll times to negative number.

    :return: 99
    """
    return 99


def TOP_BONUS_BOUNDARY() -> int:
    """

    Constant function: return 63 representing the minimum score player has to achieve in order to earn the top bonus.

    :return: 63
    """
    return 63


def TOP_BONUS_SCORE() -> int:
    """

    Constant function: return 35 representing the top bonus score.

    :return: 35
    """
    return 35


def MAX_DICE_ON_THE_TABLE() -> int:
    """
    Constant function: return 5 representing the maximum number of dice can be on the table

    :return: 5
    """
    return 5


def MAX_DICE_TO_KEEP() -> int:
    """
    Constant function: return 5 representing the maximum number of dice can be kept by a player

    :return: 5
    """
    return 5


def MAX_ROLL_TIME() -> int:
    """
    Constant function: return 3 representing the maximum times of rolling for one player each round

    :return: 3
    """
    return 3


def MIN_DICE_ON_THE_TABLE_TO_ROLL() -> int:
    """
    Constant function: return 1 representing the minimum number of dice can be on the table for user to roll again.

    :return: 1
    """
    return 1


def YAHTZEE_BONUS_MULTIPLIER() -> int:
    """
    Constant function: return 100 representing the Yahtzee bonus multiplier.

    :return: 100
    """
    return 100


def EMPTY() -> int:
    """

    Constant function: return 0 representing empty list, set, or dictionary

    :return: 0
    """
    return 0


def END_GAME() -> int:
    """

    Constant function: return 0 representing end of rolling phase

    :return: 0
    """
    return 0


def FULL_HOUSE_SCORE() -> int:
    """

    Constant function: return 25 that representing the score for a full house.

    :return: 25
    """
    return 25


def SMALL_STRAIGHT_SCORE() -> int:
    """

    Constant function: return 30 that representing the score for a small straight.

    :return: 30
    """
    return 30


def LARGE_STRAIGHT_SCORE() -> int:
    """

    Constant function: return 40 that representing the score for a large straight.

    :return: 40
    """
    return 40


def YAHTZEE_SCORE() -> int:
    """

    Constant function: return 50 that representing the score for a first time yahtzee.

    :return: 50
    """
    return 50


# Strategies:
def convert_player_kept_to_string(player_kept: []) -> str:
    """

    Sort player_kept and convert it into a sorted string

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly sort player_kept and convert it to a number string
    :return: a sorted number string representing the player_kept

    >>> convert_player_kept_to_string([6,3,4,2,5])
    '23456'

    >>> convert_player_kept_to_string([6,1,3,5,4])
    '13456'
    """
    dice_in_string = [str(die) for die in player_kept]
    return ''.join(sorted(dice_in_string))


def ones(player_kept: []) -> int:
    """

    Sum all ones in player_kept list and return it as player's score.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Ones' based on player_kept
    :return: a integer representing the sum of all one in player_kept

    >>> ones([2,3,4,5,1])
    1

    >>> ones([3,3,4,5,3])
    0

    >>> ones([1,1,1,1,1])
    5
    """
    return ONE() * player_kept.count(ONE())


def twos(player_kept: []) -> int:
    """

    Sum all twos in player_kept list and return it as player's score.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Twos' based on player_kept
    :return: a integer representing the sum of all two in player_kept

    >>> twos([2,3,4,5,1])
    2

    >>> twos([3,3,4,5,3])
    0

    >>> twos([2,2,2,2,2])
    10
    """
    return TWO() * player_kept.count(TWO())


def threes(player_kept: []) -> int:
    """

    Sum all threes in player_kept list and return it as player's score.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Threes' based on player_kept
    :return: a integer representing the sum of all three in player_kept

    >>> threes([2,3,4,5,1])
    3

    >>> threes([2,2,4,5,2])
    0

    >>> threes([3,3,3,3,3])
    15
    """
    return THREE() * player_kept.count(THREE())


def fours(player_kept: []) -> int:
    """

    Sum all fours in player_kept list and return it as player's score.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Fours' based on player_kept
    :return: a integer representing the sum of all four in player_kept

    >>> fours([2,3,4,5,1])
    4

    >>> fours([3,3,6,5,3])
    0

    >>> fours([4,4,4,4,4])
    20
    """
    return FOUR() * player_kept.count(FOUR())


def fives(player_kept: []) -> int:
    """

    Sum all fives in player_kept list and return it as player's score.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Fives' based on player_kept
    :return: a integer representing the sum of all five in player_kept

    >>> fives([2,3,4,5,1])
    5

    >>> fives([3,3,4,2,3])
    0

    >>> fives([5,5,5,5,5])
    25
    """
    return FIVE() * player_kept.count(FIVE())


def sixes(player_kept: []) -> int:
    """

    Sum all sixes in player_kept list and return it as player's score.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Sixes' based on player_kept
    :return: a integer representing the sum of all six in player_kept

    >>> sixes([2,3,6,5,1])
    6

    >>> sixes([3,3,4,5,3])
    0

    >>> sixes([6,6,6,6,6])
    30
    """
    return SIX() * player_kept.count(SIX())


def three_of_a_kind(player_kept: []) -> int:
    """

    Check if player_kept contains three of a kind. If yes, return sum all dice number in player_kept

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Three of a kind' based on player_kept
    :return: a integer representing the sum of dice number in player_kept or 0

    >>> three_of_a_kind([2,3,2,5,2])
    14

    >>> three_of_a_kind([2,3,5,5,2])
    0
    """
    if re.match(r"[1-6]*([1-6])\1{2}", convert_player_kept_to_string(player_kept)):
        return sum(player_kept)
    else:
        return ZERO()


def four_of_a_kind(player_kept: []) -> int:
    """

    Check if player_kept contains four of a kind. If yes, return sum all dice number in player_kept

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Four of a kind' based on player_kept
    :return: a integer representing the sum of dice number in player_kept or 0

    >>> four_of_a_kind([2,3,2,5,2])
    0

    >>> three_of_a_kind([5,5,5,5,2])
    22
    """
    if re.match(r"[1-6]*([1-6])\1{3}", convert_player_kept_to_string(player_kept)):
        return sum(player_kept)
    else:
        return ZERO()


def full_house(player_kept: []) -> int:
    """

    Check if player_kept contains full house. If yes, return 25.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Full house' based on player_kept
    :return: a integer 25 or 0

    >>> full_house([2,5,2,5,2])
    25

    >>> full_house([4,5,5,5,2])
    0
    """
    if re.match(r"([1-6])\1([1-6])\2{2}", convert_player_kept_to_string(player_kept)) \
            or re.match(r"([1-6])\1{2}([1-6])\2", convert_player_kept_to_string(player_kept)):
        return FULL_HOUSE_SCORE()
    else:
        return ZERO()


def small_straight(player_kept: []) -> int:
    """

    Check if player_kept contains small straight(4 sequential numbers). If yes, return 30.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Small straight' based on player_kept
    :return: a integer 30 or 0

    >>> small_straight([2,3,4,5,2])
    30

    >>> small_straight([2,1,4,5,2])
    0

    >>> small_straight([6,1,3,5,4])
    30
    """
    if re.search(r"(1234)|(2345)|(3456)", convert_player_kept_to_string(set(player_kept))):
        return SMALL_STRAIGHT_SCORE()
    else:
        return ZERO()


def large_straight(player_kept: []) -> int:
    """

    Check if player_kept contains large straight(5 sequential numbers). If yes, return 40.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Large straight' based on player_kept
    :return: a integer 40 or 0

    >>> large_straight([2,3,4,5,2])
    0

    >>> large_straight([2,3,4,5,1])
    40

    >>> large_straight([6,3,4,5,2])
    40
    """
    if re.match(r"(12345)|(23456)", convert_player_kept_to_string(player_kept)):
        return LARGE_STRAIGHT_SCORE()
    else:
        return ZERO()


def chance(player_kept: []) -> int:
    """

    Return the sum of dice number in player_kept.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Chance' based on player_kept
    :return: a integer representing the sum of dice number in player_kept

    >>> chance([2,3,4,5,2])
    16

    >>> chance([1,2,1,2,1])
    7
    """
    return sum(player_kept)


def yahtzee(player_kept: []) -> int:
    """

    Check if player_kept contains yahtzee(5 of a kind). If yes, return 50.

    :param player_kept: a list that contains dice kept by player
    :precondition: player_kept must be empty or contain a list of number from 1 to 6, length equals to 5;
    :postcondition: correctly return score of strategy 'Yahtzee' based on player_kept
    :return: a integer 50 or 0

    >>> yahtzee([2,3,4,5,2])
    0

    >>> yahtzee([1,1,1,1,1])
    50
    """
    if len(set(player_kept)) == ONE():
        return YAHTZEE_SCORE()
    else:
        return ZERO()


def main():
    game()
    doctest.testmod()


if __name__ == '__main__':
    main()