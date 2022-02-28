def main():
    input_file = "data/words_list.txt"
    output_file = "data/words_wordle.txt"
    five_letter_words = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == 5:
                five_letter_words.append(word)
    with open(output_file, "w") as f:
        for word in five_letter_words:
            f.write(word + "\n")

    print(f"{len(five_letter_words)} words written to {output_file}")


if __name__ == "__main__":
    main()