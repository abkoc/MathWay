# MathWay
Copyright (c) [2021]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

		#### Author Info ####
- Hayriye ÇELİKBİLEK
- Ahmet Burak KOC (https://www.linkedin.com/in/ahmetburakkoc)


		#### Description ####
The game "Math-way" is Tug of War game using mathematics.

"Math-way" is based on 4 operations of mathematics which are summation,
substraction, multiplication and division. It starts with an array of positive 
definit elements. In each round, player make an operation with 2 adjacent
elements so that array gets smaller in each round.

When only one element is left in array, the game is over.
Player 1 plays to keep final value larger than target and player 2 plays to 
keep it lower.

When you reach the end of the "Math-way", the one with better math will win out
over his opponent.

		#### Installation ####
Simply run "MathWay.exe"
OR
Using "MathWay.py" written in Python 3.8.
OR 
Running "MathWay.ipynb" on Jupyter Notebook

		#### How To Use ####
How to play:
1) 	At the begginning, an array is given with positive definite random elements.
2) 	Two players take an action in turns.
3) 	The player in his turn, choose one of the 4 operations and choose 
	2 adjacent elements.

	Operations: 1-Add
				2-Substract
				3-Multiply
				4-Divide
	For example, if 
				current state is	: [30, 50, 10, 40]
				player choose
					operation 	: 1-add
					index1 		: 0
					index2 		: 1
				Result 			: [(30+50), 10, 40]
				next state is 		: [  80   , 10, 40]
4) 	Turn changes.
5) 	The other player chooses an operation and indexes.
6) 	Step 4&5 are repeated until array contains 1 element and no more operation
	is possible.
7) 	In final state, array value is bigger than target, player 1 wins.
	Otherwise player 2 wins.

		#### Technologies ####
- Minmax algorithm is implemented to program AI playing.
- Alpha-beta pruning is implemented to improve efficiency of the adversarial
search algorithm.

		#### References ####
[Back To The Top](#read-me-template)
Norvig P. & Russell S, Artificial intelligence a modern approach, 2014, Pearson Education
