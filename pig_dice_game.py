import random
import argparse
from typing import List


# Default score needed to win the game
TARGET_SCORE = 100


def roll_die() -> int:
    """Return a random integer between 1 and 6 (inclusive) representing a die roll.

    This is a tiny helper so the dice behaviour is isolated in one place and
    easy to change (e.g., to use different dice or to seed randomness for tests).
    """
    return random.randint(1, 6)


def play_turn(player_name: str) -> int:
    """Play a single turn for `player_name`.

    The function repeatedly rolls the die until the player chooses to stop
    (by answering 'n' to the prompt) or rolls a 1. If a 1 is rolled the turn
    score is lost and 0 is returned. Otherwise the accumulated turn score is
    returned.
    """
    turn_score = 0

    print(f"\n{player_name}'s turn")

    while True:
        roll = roll_die()
        print(f'You rolled a {roll}')

        # If the player rolls a 1 the turn ends and they lose the turn points
        if roll == 1:
            return 0

        # Otherwise add roll to turn total and ask whether to continue
        turn_score += roll
        choice = input('Roll again? (y/n): ').strip().lower()
        if choice != 'y':
            return turn_score


def main(target: int = TARGET_SCORE) -> None:
    """Main game loop.

    Manages player scores, alternates turns, and stops when a player's total
    score reaches or exceeds `target`.
    """
    scores: List[int] = [0, 0]
    current_player = 0

    while True:
        player_name = f'Player {current_player + 1}'
        turn_score = play_turn(player_name)
        scores[current_player] += turn_score

        print(f'\nYou scored {turn_score} points this turn.')
        print(f'Current scores: Player 1: {scores[0]}, Player 2: {scores[1]}')

        # Check for winner
        if scores[current_player] >= target:
            print(f'{player_name} wins!')
            break

        # Switch player
        current_player = 1 if current_player == 0 else 0


if __name__ == '__main__':
    # Parse an optional command-line argument to change the target score
    parser = argparse.ArgumentParser(description='Play the Pig Dice Game (CLI)')
    parser.add_argument('--target', '-t', type=int, default=TARGET_SCORE,
                        help=f'score required to win (default: {TARGET_SCORE})')
    args = parser.parse_args()

    try:
        main(target=args.target)
    except KeyboardInterrupt:
        print('\nGame interrupted. Goodbye!')
