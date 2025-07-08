import pandas as pd
phonetic_df = pd.read_csv("./Day 26 - NATO Alphabets/nato_phonetic_alphabet.csv")
phonetic_dict = {data.letter : data.code for idx,data in phonetic_df.iterrows()}
while True:
    try:
        user_input = input("Enter a word to get its phonetic codes :").upper().strip()
        result = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("\n❌ Only alphabets are allowed. Please try again.\n")
    else:
        print("\nYour Phonetic Alphabets are :\n💥"," -> ".join(result),"\n")
        


