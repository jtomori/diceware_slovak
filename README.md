# Diceware - Slovak

## Wordlist sizes
* 5 dice rolls: `6^5 = 7 776` possibilities
* 6 dice rolls: `6^6 = 46 656` possibilities
* 7 dice rolls: `6^7 = 279 936` possibilities

## Entropy

### When the wordlist is known and word choices are random (dice throws)

#### Table (bits)

|  | 5 dice rolls | 6 dice rolls | 7 dice rolls |
| - | - | - | - |
| **1 word** | 12.92 | 15.51 | 18.1 |
| **2 words** | 25.85 | 31.02 | 36.19 |
| **3 words** | 38.77 | 46.53 | 54.28 |
| **4 words** | 51.7 | 62.04 | 72.38 |
| **5 words** | 64.62 | 77.55 | 90.47 |
| **6 words** | 77.55 | 93.06 | 108.57 |
| **7 words** | 90.47 | 108.57 | 126.66 |
| **8 words** | 103.4 | 124.08 | 144.76 |
| **9 words** | 116.32 | 139.59 | 162.85 |
| **10 words** | 129.23 | 155.1 | 180.95 |

#### Calculations

* 1 word passphrase
    * 5 dice wordlist: `1 * log2(6^5) = ~12.92 bits`
    * 6 dice wordlist: `1 * log2(6^6) = ~15.51 bits`
    * 7 dice wordlist: `1 * log2(6^7) = ~18.1 bits`
* 2 words
    * 5 dice wordlist: `2 * log2(6^5) = ~25.85 bits`
    * 6 dice wordlist: `2 * log2(6^6) = ~31.02 bits`
    * 7 dice wordlist: `2 * log2(6^7) = ~36.19 bits`
* 3 words
    * 5 dice wordlist: `3 * log2(6^5) = ~38.77 bits`
    * 6 dice wordlist: `3 * log2(6^6) = ~46.53 bits`
    * 7 dice wordlist: `3 * log2(6^7) = ~54.28 bits`
* ...

## Usage
* `$ ./generate.py` generates dictionaries
* `$ cat diceware_sk_6_rolls | grep "^123456"` searches for combination `123456` in `diceware_sk_6_rolls` wordlist
    * If you prepend your *Bash* command with space, it may not be saved in `~/.bash_history` on some linux distributions

### Example output
```
$ ./generate.py 
Original amount of words: 1807770
Filtered amount of words: 1708357
5 dice rolls list, length: 7776, minimum word length: 3
6 dice rolls list, length: 46656, minimum word length: 4
7 dice rolls list, length: 279936, minimum word length: 5
Generation took 3.99 seconds
```

## Notes
* `log2(n) = log(n) / log(2)`
* If you are lazy to remember larger passphrase, then use larger wordlist
* If you reuse your password, high entropy will not help you

## Sources
* [What is Diceware](http://world.std.com/~reinhold/diceware.html)
* [Diceware FAQ](http://world.std.com/%7Ereinhold/dicewarefaq.html)
* [Slovak frequency wordlist](https://p.brm.sk/sk_wordlist/)