#!/usr/bin/env python3

from itertools import product
import time

def word_filter(word):
    """
    Define word length limits here
    """
    return len(word) > 0 and len(word) < 16

def generate():
    """
    Does the actual generation
    """
    # range of generated dictionaries
    start_size = 5
    end_size = 8

    # open source wordlist
    with open("frequency_list.txt") as f:
        freq_list = f.readlines()[1:]

    print("Original amount of words: {}".format(len(freq_list)))

    # filter source wordlist based on word_filter() function
    freq_list = [ line.split()[0] for line in freq_list if word_filter( line.split()[0] ) ]
    
    print("Filtered amount of words: {}".format(len(freq_list)))
    
    # generate all rolls combinations, number of rolls: end_size
    rolls_list = list( product(range(1,7), repeat=end_size) )
    rolls_list = [ "".join( map(str, roll[::-1]) ) for roll in rolls_list] # reverse rolls and convert to string

    # combine rolls_list and freq_list into wordlists based on size of target wordlists
    for num_rolls in range(start_size, end_size+1):
        words_num = 6**num_rolls
        
        current_words_list = freq_list[:words_num]
        current_rolls_list = rolls_list[:words_num]
        
        combined_list = [ "{} {}".format(rolls[:num_rolls], words) for rolls, words in zip(current_rolls_list, current_words_list)] # element-wise concat of two lists
        
        print("{} dice rolls list, length: {}".format(num_rolls, len(combined_list)))

        with open("diceware_sk_{}_rolls".format(num_rolls), "w") as f:
            f.write("\n".join(combined_list))

if __name__ == "__main__":
    """
    If run as a script
    """
    start_time = time.time()
    generate()
    print("\nGeneration took {:.2f} seconds".format(time.time() - start_time))