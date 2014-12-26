# FizzBuzz in Python
### AKA: FissBuss

Popular coding kata FizzBuzz written in Python.

If a player has to say a number :
 * divisible by three, they replace it with "Fiss"
 * divisible by five, they replace it with "Buss"
 * divisible by both, they replace it with "FissBuss"

Written TDD style, using Python's built in 'assert' function.

To play:

````python
$ import fissbuss

for number in range(0, 100):
    fissbuss.play(number)
    
````
