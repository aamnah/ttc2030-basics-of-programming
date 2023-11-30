# Exercise 6: Recap and Debugger
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise06.md

"""
6.1.
Make a function time that converts seconds (sent as parameter) into text form of hours:minutes:seconds. For example, for the number 10000, the following text is returned: "02:46:40"
Test the functionality of your program with at least five different values.
"""

import math

def time(total_seconds):
    """takes seconds and converts it to hh:mm:ss format
    """
    seconds_in_one_day = 86400
    if (total_seconds > seconds_in_one_day ):
        print("There can not be more than 86400 seconds in a day.")
        return
    hours = math.trunc(total_seconds / 60 / 60) # truncate the fractional part and get only the integer
    seconds = total_seconds % 60 # whatever of the total seconds is the remainder after dividing by 60 would become the clock seconds
    minutes = round(((total_seconds - seconds) / 60) % 60) # whatever is the remainder and could not be equally divided is the clock minutes now
    # round() because division gives a float (46.0 instead of 46)

    if (hours < 10):
        hours = f"0{hours}"
    if (minutes < 10):
        minutes = f"0{minutes}"
    if (seconds < 10):
        seconds = f"0{seconds}"

    print(f"""{total_seconds} seconds = {hours}:{minutes}:{seconds}""")


def tests():
    time(10000) # 02:46:40
    time(60) # 00:01:00 (1 minute)
    time(600) # 00:10:00 (10 minutes)
    time(6000) # 01:40:00 (140 minutes)
    time(60000) # 16:40:00 (1000 minutes, 16.6 hours)
    # time(86401) # There can not be more than 86400 seconds in a day.

tests()