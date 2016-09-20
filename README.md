# longest-chain-of-factors-and-multiples
Brute-force method to find the longest chain of factors-and-multiples game.

## 1. Factors and Multiples Game
https://nrich.maths.org/5468

## 2. fish shell
  <code fish>
  # for i in (seq 1 100); timeout 3 ./fm.py $i; end;
  </code>

  <code fish>
  # for i in (seq 1 100); timeout 60 ./fm1.py $i &; end;
  </code>

## 3. my guess
* [Hamilton Path](https://en.wikipedia.org/wiki/Hamiltonian_path)
* [Factors and Multiples - Hamiltonian Path](http://mathforum.org/library/drmath/view/54255.html)
* my handwriting

  ![handwriting](images/my_guess.jpg?raw=true)

## 4. Current solutions
<code>
71

[81, 27, 54, 18, 90, 45, 15, 75, 25, 100, 50, 10, 80, 40, 20, 60, 30, 6, 96, 48, 24, 72, 36, 12, 84, 42, 21, 63, 9, 99, 33, 66, 22, 88, 44, 11, 77, 7, 98, 49, 1, 95, 19, 76, 38, 2, 92, 46, 23, 69, 3, 51, 17, 34, 68, 4, 64, 32, 16, 8, 56, 28, 14, 70, 35, 5, 65, 13, 52, 26, 78]
</code>

## 5. 25 prime numbers less than 100
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 and 97
