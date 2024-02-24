Red-Blue Nim Game

This is an implementation of the Red-Blue Nim game with options for both standard and misère versions. The game is played against a computer AI or a human player.

* Requirements
    Python 3.x

* How to Play
    Red-Blue Nim is a game where players take turns choosing marbles from two piles, red and blue. The rules are as follows:

    1. On each player's turn, they pick a pile (either "red" or "blue") and remove one or more marbles from it.
    2. The game continues until one of the players runs out of marbles in their chosen pile.
    3. In the standard version, the player who removes the last marble from any pile loses. In the misère version, they win.

* Command Line Usage
    To play the game, you can run the `red_blue_nim.py` script with the following command line options:

    python red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>

    - `<num-red>`: Number of red marbles.
    - `<num-blue>`: Number of blue marbles.
    - `<version>` (Optional): Game version ("standard" or "misère"). Default is "standard".
    - `<first-player>` (Optional): The starting player ("computer" or "human"). Default is "computer".
    - `<depth>` (Optional): Depth for depth-limited MinMax search (for extra credit).

* Example:

    python red_blue_nim.py 5 7 misère computer 3

* Extra Credit (Depth-Limited MinMax Search)
    If you provide a depth argument (e.g., `python red_blue_nim.py 5 7 standard computer 3`), the game uses depth-limited MinMax with alpha-beta pruning to determine the computer's moves. The depth parameter controls the depth of the search tree.

* Evaluation Function
    The evaluation function in the code is used to assign scores to game states during MinMax search. In the "standard" version, red marbles are assigned a value of 2, and blue marbles are assigned a value of 3. In the "misère" version, red marbles are assigned -2, and blue marbles are assigned -3. The function allows the computer to make intelligent decisions based on the version and the remaining marbles.

* Running on ACS Omega
    This code can be run on the ACS Omega platform if needed. Simply follow the instructions provided for running the code on ACS Omega, ensuring that Python is available on the platform.

* Contributor
    Yashkumar Chandwani
    Email: yxc5885@mavs.uta.edu