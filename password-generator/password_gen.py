import random


def main():
    print("Welcome to the PyPassword Generator!")
    print("How many letters would you like in your password?")
    letter_count = int(input())
    print("How many symbols would you like?")
    symbol_count = int(input())
    print("How many numbers would you like?")
    number_count = int(input())
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random_letters = [random.choice(letters) for _ in range(1, letter_count + 1)]
    random_symbols = [random.choice(symbols) for _ in range(1, symbol_count + 1)]
    random_numbers = [random.choice(numbers) for _ in range(1, number_count + 1)]
    # easy
    password = random_letters + random_symbols + random_numbers
    print(f"Here is your password (sequential): {''.join(password)}")
    # hard
    shuffled_password = password
    random.shuffle(shuffled_password)
    print(f"Here is your password (shuffled): {''.join(shuffled_password)}")


if __name__ == "__main__":
    main()
