import random
from hangman_words import word_list
from hangman_art import logo, stages
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    chosen_word = random.choice(word_list)
    disp = ["_" for _ in chosen_word]
    seen = set()
    lives = len(stages) - 1
    print(logo)
    print(f"The word consists of {len(chosen_word)} letters.")
    print(f"{' '.join(disp)}\n")
    while lives > 0:
        if "_" in disp:
            guess = input("Guess a letter: ").lower()
            clear()
            if guess not in seen:
                seen.add(guess)
                if guess not in chosen_word:
                    print(f"You guessed '{guess}' which is not in the word. You lost a life.")
                    lives -= 1
                else:
                    print(f"Yay! You guessed '{guess}' which is in the word.")
                    for i, a in enumerate(chosen_word):
                        if guess == a:
                            disp[i] = guess
            else:
                print(f"You've already guessed '{guess}'.")
            print(f"Words guessed: {', '.join(seen)}")
            print(stages[lives] + f"\nLives left: {lives}")
            print(f"Word: {' '.join(disp)}\n")
        else:
            print("You win.")
            break
    print("You lose.")
    print(f"The word was {chosen_word}.")


if __name__ == "__main__":
    main()
