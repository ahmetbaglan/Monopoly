# Monopoly simulation

This is a simulation program written in Python to simulate games of Monopoly.

## Usage

Of course the first step is to download all the python files in one directory.
Running the program is very simple. If you would like to know more about how to
run the program, visit the --help page.

The program can be used in the follow manner.

```
monopoly.py [-h] [-n NUMBER] [-p {1,2,3,4,5,6}] [-r ROUNDS]
```

### Help page

The --help page in the program is as follows.

```
usage: monopoly.py [-h] [-n NUMBER] [-p {1,2,3,4,5,6}] [-r ROUNDS]

Programm to simulate the game of Monopoly.

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        number of simulations to run
  -p {1,2,3,4,5,6}, --players {1,2,3,4,5,6}
                        number of players to run the simulation with
  -r ROUNDS, --rounds ROUNDS
                        number of rounds to simulate each game

						
						
The output file is a CSV including the number of hits to a tile and several properties for each tile

Ahmet Baglan