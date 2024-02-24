import sys
import random

def print_state(red, blue):
    print(f"Red Marbles: {red}, Blue Marbles: {blue}")

def get_human_move(red, blue):
    while True:
        move = input("Enter your move (e.g., 'red 2' or 'blue 1'): ").strip().split()
        if len(move) != 2:
            print("Invalid input. Please specify the pile and the number of marbles to remove.")
            continue
        pile, num = move
        if pile not in ["red", "blue"] or not num.isdigit():
            print("Invalid input. Please specify a valid pile ('red' or 'blue') and a number of marbles to remove.")
            continue
        num = int(num)
        if (pile == "red" and 1 <= num <= red) or (pile == "blue" and 1 <= num <= blue):
            return pile, num
        else:
            print("Invalid move. Please try again.")

def perform_move(red, blue, pile, num):
    if pile == "red":
        red -= num
    else:
        blue -= num
    return red, blue

def is_terminal_state(red, blue, version):
    if version == "standard":
        return red == 0 or blue == 0
    else:
        return red == 0 or blue == 0

def evaluate(red, blue, version):
    if version == "standard":
        return 2 * red + 3 * blue
    else:
        if red == 0 and blue == 0:
            return 0
        if red > 0 and blue > 0:
            return 1  # Game is ongoing, no clear winner yet
        if red == 0:
            return 1  # In misère, the player whose turn is next wins when both piles are empty
        if blue == 0:
            return 1  # In misère, the player whose turn is next wins when both piles are empty

def min_max(red, blue, version, max_player, depth, alpha, beta):
    if depth == 0 or is_terminal_state(red, blue, version):
        return evaluate(red, blue, version), None

    best_move = None
    if max_player:
        max_eval = float("-inf")
        for pile in ["blue", "red"] if version == "standard" else ["red", "blue"]:
            for num in range(1, red + 1) if pile == "red" else range(1, blue + 1):
                new_red, new_blue = red, blue
                if pile == "red":
                    new_red -= num
                else:
                    new_blue -= num
                eval, _ = min_max(new_red, new_blue, version, False, depth - 1, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_move = (pile, num)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval, best_move
    else:
        min_eval = float("inf")
        for pile in ["red", "blue"] if version == "standard" else ["blue", "red"]:
            for num in range(1, red + 1) if pile == "red" else range(1, blue + 1):
                new_red, new_blue = red, blue
                if pile == "red":
                    new_red -= num
                else:
                    new_blue -= num
                eval, _ = min_max(new_red, new_blue, version, True, depth - 1, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_move = (pile, num)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval, best_move

def play_red_blue_nim(red, blue, version, first_player, depth=None):
    while True:
        if is_terminal_state(red, blue, version):
            print_state(red, blue)
            if version == "standard":
                score = evaluate(red, blue, version)
                if score > 0:
                    print(f"Computer wins with a score of {score}.")
                else:
                    print(f"Human wins with a score of {-score}.")
            else:
                score = evaluate(red, blue, version)
                if score > 0:
                    print(f"Computer wins with a score of {score}.")
                else:
                    print(f"Human wins with a score of {-score}.")
            break

        print_state(red, blue)
        if first_player == "computer":
            if depth:
                _, (pile, num) = min_max(red, blue, version, True, depth, float("-inf"), float("inf"))
            else:
                pile, num = random_move(red, blue, version)
            print(f"Computer chooses {pile} {num}.")
            red, blue = perform_move(red, blue, pile, num)
        else:
            pile, num = get_human_move(red, blue)
            red, blue = perform_move(red, blue, pile, num)
        first_player = "human" if first_player == "computer" else "computer"

def random_move(red, blue, version):
    if version == "standard":
        if red >= blue:
            pile = "blue"
        else:
            pile = "red"
    else:
        if red >= blue:
            pile = "red"
        else:
            pile = "blue"
    max_num = blue if pile == "blue" else red
    num = random.randint(1, max_num)
    return pile, num

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: red_blue_nim.py <num-red> <num-blue> [<version>] [<first-player>] [<depth>]")
        sys.exit(1)

    red = int(sys.argv[1])
    blue = int(sys.argv[2])
    version = "standard"
    first_player = "computer"
    depth = None

    if len(sys.argv) > 3:
        version = sys.argv[3]
    if len(sys.argv) > 4:
        first_player = sys.argv[4]
    if len(sys.argv) > 5:
        depth = int(sys.argv[5])

    play_red_blue_nim(red, blue, version, first_player, depth)