#!/usr/bin/env python3

import time
import math
from itertools import product

ALPHABET = "aábcčdďeéfghiíjklľmnňoóprsštťuúvyýzž".lower() # Some characters are missing since they are not common in Slovak. Strip this alphabet to omit words containing those letters.
# Full alphabet: "aáäbcčdďeéfghiíjklĺľmnňoóôpqrŕsštťuúvwxyýzž"

ALPHABET_CHECK = "abcdefghijklmnoprstuvyz" # This alphabet is assumed to be used in the actual passwords. This set of characters assumes that user will not use diacritics (e.g. š, ž, á...). If user plans to use diacritics then change this line to `ALPHABET_CHECK = ALPHABET` (without backticks).

def word_filter(word):
    """Define word filtering here

    Args:
        word (str): Word to be checked
    
    Returns:
        (Bool): `True` if the word should be considered, `False` if the word should be discarded
    """
    if not ( set(word.lower()) <= set(ALPHABET) ): # Discard words with characters not common in Slovak
        return False
    
    return True # Passed check

def generate():
    """Does the actual generation. It assumes existence of the `frequency_list.txt`."""
    # Range of generated dictionaries
    start_size = 5
    end_size = 7

    # Open input wordlist
    with open("frequency_list.txt") as f:
        freq_list = f.readlines()

    print("Original amount of words: {}".format(len(freq_list)))

    # Filter source wordlist based on the `word_filter()` function
    freq_list = [ line.split()[0] for line in freq_list if word_filter( line.split()[0] ) ]
    
    print("Filtered amount of words: {}".format(len(freq_list)))

    # Generate all rolls combinations, number of rolls: end_size
    rolls_list = list( product(range(1,7), repeat=end_size) )
    rolls_list = [ "".join( map(str, roll[::-1]) ) for roll in rolls_list] # reverse rolls and convert to string

    # Combine `rolls_list` and `freq_list` into wordlists based on the size of target wordlists
    for num_rolls in range(start_size, end_size+1):
        words_num = 6**num_rolls # All possible rolls
        
        # Calculate minimum word length based on the required entropy (shouldn't be lower than `entropy_per_word`)
        entropy_per_word = math.log(words_num, 2)
        entropy_per_character = math.log(len(ALPHABET_CHECK), 2)
        char_limit = math.ceil(entropy_per_word / float(entropy_per_character))

        current_words_list = [word for word in freq_list if len(word) >= char_limit]

        if len(current_words_list) < words_num:
            print("ERROR: Insufficient length of the input wordlist. Dictionary for {} dice rolls could not be generated. Required number of words: {}. Available number of words: {}.".format(num_rolls, words_num, len(current_words_list)))
            break

        current_words_list = current_words_list[:words_num]
        current_rolls_list = rolls_list[:words_num]
        
        combined_list = [ "{} {}".format(rolls[:num_rolls], words) for rolls, words in zip(current_rolls_list, current_words_list)] # Element-wise concat of two lists
        
        print("{} dice rolls list, length: {}, minimum word length: {}".format(num_rolls, len(combined_list), char_limit))

        with open("diceware_sk_{}_rolls".format(num_rolls), "w") as f:
            f.write("\n".join(combined_list))

if __name__ == "__main__":
    """
    If run as a script
    """
    start_time = time.time()
    generate()
    print("Generation took {:.2f} seconds".format(time.time() - start_time))