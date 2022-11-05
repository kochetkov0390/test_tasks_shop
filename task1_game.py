from pprint import pprint
from typing import List, Dict
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


def get_score(game_stamps: List[Dict], offset: int):
    result = None
    if len(game_stamps) == 1:
        home = game_stamps[0]['score']['home']
        away = game_stamps[0]['score']['away']
        return home, away
    mid_index = int(len(game_stamps)/2)
    if game_stamps[mid_index]['offset'] > offset:
        result = get_score(game_stamps[0:mid_index], offset)
    else:
        result = get_score(game_stamps[mid_index:], offset)
    return result


if __name__ == '__main__':
    game_stamps = generate_game()
    pprint(get_score(game_stamps, game_stamps[-1]['offset']))
