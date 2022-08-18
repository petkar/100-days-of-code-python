from art import logo


def get_alphabet_list():
    return list(map(chr, range(97, 123)))


def get_shifted_list(shift):
    alphabet = get_alphabet_list()
    if shift > len(alphabet):
        shift %= len(alphabet)
    shifted = alphabet[shift:] + alphabet[:shift]
    return shifted


def caesar(start_text, shift, direction):
    alphabet = get_alphabet_list()
    shifted = get_shifted_list(shift)
    end_text = ""
    for i, a in enumerate(start_text):
        if not a.isalpha():
            end_text += a
        else:
            if direction == "encode":
                index = alphabet.index(a)
                end_text += shifted[index]
            elif direction == "decode":
                index = shifted.index(a)
                end_text += alphabet[index]
    return end_text


def prompt_repeat():
    prompt_text = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if prompt_text == "yes":
        return True
    elif prompt_text == "no":
        return False
    else:
        print("Please enter a valid response.")
        return prompt_repeat()


def get_direction():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        return direction
    else:
        print("Please enter a valid input.")
        return get_direction()


def main():
    print(logo)
    run_next = True
    while run_next:
        print(logo)
        direction = get_direction()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        output = caesar(text, shift, direction)
        print(f"Here's the {direction}ed result: {output}")
        run_next = prompt_repeat()
    print("Goodbye")


if __name__ == "__main__":
    main()
