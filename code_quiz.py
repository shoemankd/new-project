# -*- coding: utf-8 -*-

# The following are the madlibs strings to pass in to the play_game function.
easy = '''
    Python is an interpreted, object-oriented programming language similar to PERL, that has gained popularity because of its clear syntax and readability. Python is said to be relatively easy to learn and portable, meaning its statements can be interpreted in a number of operating systems, including UNIX-based systems, Mac OS, MS-DOS, OS/2, and various versions of Microsoft Windows 98. Python was created by Guidovan Rossum, a former resident of the Netherlands, whose favorite comedy group at the time was Monty Python's Flying Circus. The source code is freely available and open for modification and reuse. Python has a significant number of users.
         '''

medium = '''
        A variable is an object that can have a value, expression, a string,
        or a list assigned to it. The "==" is the symbol used to assign a
        value to a variable. A list can be mutated and allied with another
        name, a string cannot.
        '''

hard = '''
        A function is a block of code that can perform a single task multiple
        times. A function begins with the keyword def and then is followed by
        the name, parentheses, and a colon. Parameters and arguments go into
        the parentheses.'''

# Set up madlibs strings into a list
paragraphs = [easy, medium, hard]

# A list of replacement words from the madlibs to be passed in to the play
# game function.
input_list = [["Python", "language", "Netherlands", "Guido van Rossum"],  # for easy
              ["variable", "assign", "list", "string"],  # for medium
              ["function", "def", "colon", "Parameters"]]  # for hard


# Prompt the user to choose a madlib level from the list until they choose a
# valid one.
def choose_level():
    '''
    This is my function that will select which string the user will answer
    questions with.
    '''
    level = raw_input("Enter your difficulty level (easy/medium/hard): ")

    if level == "easy":
        print "Easy level selected"
        return 0
    elif level == "medium":
        print "Medium level selected"
        return 1
    elif level == "hard":
        print "Hard level selected"
        return 2
    else:
        print "Invalid level selected"
        return choose_level()  # if the level is invalid, choose a level again,
        # and return that value


# Process the paragraph for the given level
def process_paragraph(level, blank):
    '''
    Replaces the words in input_list for the level, from the given blank.
    '''
    paragraph = paragraphs[level]

    # replace all the input_list from current blank to the last one
    while blank < len(input_list[level]):
        word_to_replace = input_list[level][blank]
        list_of_words = paragraph.split(" ")
        index = 0
        # Replace the word_to_replace with ___number___
        while index < len(list_of_words):
            if list_of_words[index] == word_to_replace:
                list_of_words[index] = "___" + str(blank + 1) + "___"
            index += 1

        blank += 1
        paragraph = " ".join(list_of_words)

    return paragraph


# play the game for the given level
def play_game(level):
    '''
    Plays a full game of mad_libs. A player is prompted to replace blanks in
    madlibs level with the correct words.
    '''
    blank = 0

    # while not all input_list are filled, keep asking to guess the input_list
    # until the correct word is provided
    while blank < len(input_list[level]):
        print process_paragraph(level, blank)

        question = "\nWhat should go in blank number " + str(blank + 1) + "?"
        answer = raw_input(question).lower()

        correct_answer = input_list[level][blank].lower()
        if correct_answer == answer:
            print "Correct!"
            blank += 1
        else:
            print "Try again!"

    print paragraphs[level]
    print "\n Well played, you're pretty awesome!"


# Take the steps to play the game, prompt to advance to the next level
# when a level is completed
def main():
    """
    Opening and closing ceremony of the game. Add a loop so that you can keep
    telling Madlibs without having to restart the program each time.
    """
    print "~~~ Welcome to Computer Programming Reverse-Mad-Libs ~~~"

    level = choose_level()

    while level < 3:
        play_game(level)

        # If we're at easy or medium, prompt to advance
        if level < 2:
            proceed = raw_input(
                    "Would you like to attempt a different level?(YES/NO)")
            if proceed == "YES":
                level += 1
            else:
                break
        else:
            break

    print " \n ~~~ Thanks for playing! ~~~ "


main()
