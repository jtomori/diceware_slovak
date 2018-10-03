# Diceware - Slovak

## Wordlist sizes
* 5 dice rolls: `6^5 = 7 776` possibilities
* 6 dice rolls: `6^6 = 46 656` possibilities
* 7 dice rolls: `6^7 = 279 936` possibilities
* 8 dice rolls: `6^8 = 1 679 616` possibilities

<br>

## Entropy

### When wordlist is known and word choice is random (dice throws)

#### Table

|  | 5 dice rolls | 6 dice rolls | 7 dice rolls | 8 dice rolls |
| - | - | - | - | - |
| **1 word** | 12.92 | 15.51 | 18.1 | 20.68 |
| **2 words** | 25.85 | 31.02 | 36.19 | 41.36 |
| **3 words** | 38.77 | 46.53 | 54.28 | 62.04 |
| **4 words** | 51.7 | 62.04 | 72.38 | 82.72 |
| **5 words** | 64.62 | 77.55 | 90.47 | 103.4 |
| **6 words** | 77.55 | 93.06 | 108.57 | 124.08 |
| **7 words** | 90.47 | 108.57 | 126.66 | 144.76 |
| **8 words** | 103.4 | 124.08 | 144.76 | 165.44 |
| **9 words** | 116.32 | 139.59 | 162.85 | 186.12 |
| **10 words** | 129.23 | 155.1 | 180.95 | 206.8 |

#### Calculations

* 1 word
    * 5 dice wordlist: `1 * log2(7 776) = ~12.92 bits`
    * 6 dice wordlist: `1 * log2(46 656) = ~15.51 bits`
    * 7 dice wordlist: `1 * log2(279 936) = ~18.1 bits`
    * 8 dice wordlist: `1 * log2(1 679 616) = ~20.68 bits`
* 2 words
    * 5 dice wordlist: `2 * log2(7 776) = ~25.85 bits`
    * 6 dice wordlist: `2 * log2(46 656) = ~31.02 bits`
    * 7 dice wordlist: `2 * log2(279 936) = ~36.19 bits`
    * 8 dice wordlist: `2 * log2(1 679 616) = ~41.36 bits`
* 3 words
    * 5 dice wordlist: `3 * log2(7 776) = ~38.77 bits`
    * 6 dice wordlist: `3 * log2(46 656) = ~46.53 bits`
    * 7 dice wordlist: `3 * log2(279 936) = ~54.28 bits`
    * 8 dice wordlist: `3 * log2(1 679 616) = ~62.04 bits`
* 4 words
    * 5 dice wordlist: `4 * log2(7 776) = ~51.7 bits`
    * 6 dice wordlist: `4 * log2(46 656) = ~62.04 bits`
    * 7 dice wordlist: `4 * log2(279 936) = ~72.38 bits`
    * 8 dice wordlist: `4 * log2(1 679 616) = ~82.72 bits`
* 5 words
    * 5 dice wordlist: `5 * log2(7 776) = ~64.62 bits`
    * 6 dice wordlist: `5 * log2(46 656) = ~77.55 bits`
    * 7 dice wordlist: `5 * log2(279 936) = ~90.47 bits`
    * 8 dice wordlist: `5 * log2(1 679 616) = ~103.4 bits`
* 6 words
    * 5 dice wordlist: `6 * log2(7 776) = ~77.55 bits`
    * 6 dice wordlist: `6 * log2(46 656) = ~93.06 bits`
    * 7 dice wordlist: `6 * log2(279 936) = ~108.57 bits`
    * 8 dice wordlist: `6 * log2(1 679 616) = ~124.08 bits`
* 7 words
    * 5 dice wordlist: `7 * log2(7 776) = ~90.47 bits`
    * 6 dice wordlist: `7 * log2(46 656) = ~108.57 bits`
    * 7 dice wordlist: `7 * log2(279 936) = ~126.66 bits`
    * 8 dice wordlist: `7 * log2(1 679 616) = ~144.76 bits`
* 8 words
    * 5 dice wordlist: `8 * log2(7 776) = ~103.4 bits`
    * 6 dice wordlist: `8 * log2(46 656) = ~124.08 bits`
    * 7 dice wordlist: `8 * log2(279 936) = ~144.76 bits`
    * 8 dice wordlist: `8 * log2(1 679 616) = ~165.44 bits`
* 9 words
    * 5 dice wordlist: `9 * log2(7 776) = ~116.32 bits`
    * 6 dice wordlist: `9 * log2(46 656) = ~139.59 bits`
    * 7 dice wordlist: `9 * log2(279 936) = ~162.85 bits`
    * 8 dice wordlist: `9 * log2(1 679 616) = ~186.12 bits`
* 10 words
    * 5 dice wordlist: `10 * log2(7 776) = ~129.23 bits`
    * 6 dice wordlist: `10 * log2(46 656) = ~155.1 bits`
    * 7 dice wordlist: `10 * log2(279 936) = ~180.95 bits`
    * 8 dice wordlist: `10 * log2(1 679 616) = ~206.8 bits`

<br>

## Usage
* `generate.py` generates dictionaries
* `$ cat diceware_sk_6_rolls | grep "^123456"` searches for combination `123456` in `diceware_sk_6_rolls` wordlist
    * if you prepend your *Bash* command with space on some linux distributions, it will not be saved in `~/.bash_history`

<br>

## Notes
* `log2(n) = log(n) / log(2)`
* If you are lazy to remember more words, then use larger wordlist
* If you reuse your password, high entropy will not help you
* Not using diacritics in words, or using only lowercase letters does not decrease entropy if attacker knows about it, in brute-force attacks it will decrease entropy
    * If still worried, add another word to your passphrase
    * Using ant not using diacritics randomly (with dice) will increase entropy in both cases

<br>

## Sources
* [What is Diceware](http://world.std.com/~reinhold/diceware.html)
* [Diceware FAQ](http://world.std.com/%7Ereinhold/dicewarefaq.html)
* [Slovak frequency wordlist](https://p.brm.sk/sk_wordlist/)