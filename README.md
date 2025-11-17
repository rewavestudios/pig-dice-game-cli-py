# Pig Dice Game

This is a simple, interactive two-player implementation of the classic Pig Dice Game.
Players alternate turns, rolling a six-sided die to accumulate points. Rolling a 1
loses the turn's points and passes play to the other player. The first player to
reach the target score wins (default 100).

**Files:**
- `pig_dice_game.py`: The main game script. Run this file to play the game.

**Quick Start:**

- **Run the game**:

```bash
python3 pig_dice_game.py
```

- **Change the target score** (optional):

```bash
python3 pig_dice_game.py --target 50
```

**Rules (brief):**

- On your turn you roll a six-sided die.
- If you roll a 1, you score 0 points for the turn and your turn ends.
- If you roll 2–6, that value is added to your turn total and you choose to
	roll again or hold.
- If you hold, the turn total is added to your overall score and the turn ends.
- First player to reach the target score wins.

**Notes:**

- This implementation is a straightforward, interactive CLI. There are no external
	dependencies beyond the Python standard library.
- The code is in `pig_dice_game.py` and includes comments above each major block
	explaining behaviour and purpose.

## Optional Enhancements

These are suggested optional improvements you can add to the game to increase
flexibility and replayability. Each item includes a short note on how it could
be implemented.

- **Custom target score before starting the game:**
	- Allow players to pass a `--target` command-line argument (already supported)
		or prompt for a target score at program start. The `main()` function accepts
		a `target` parameter; prompting simply calls `main(target=chosen_value)`.

- **Support more than two players:**
	- Generalize the `scores` list to hold N players and iterate player indices
		in round-robin order. Prompt at start for number of players and player
		names to personalize turns.

- **Track cumulative scores over multiple rounds/games:**
	- Persist player totals to a local file (JSON or CSV) between runs, or keep
		an in-memory scoreboard when running multiple rounds in one session. Add a
		`--save-results` flag to enable persistence and a `--load-results` flag to
		resume previous totals.

- **Double-six penalty rule (rolling two consecutive 6s resets score to 0):**
	- Track the previous roll for the current player during a turn. If the new
		roll is 6 and the previous roll was 6, set that player's total score to 0
		(or apply another configured penalty) and end their turn. This adds
		strategic risk when rolling after a 6.

## Contributing:

I would love your help! Contribute by forking the repo and opening pull requests. Please ensure that your code passes the existing tests and linting, and write tests to test your changes if applicable.

All pull requests should be submitted to the `main` branch.

## License

See the [LICENSE](LICENSE) file for details.
