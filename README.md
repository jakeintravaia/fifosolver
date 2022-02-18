# fifosolver
This simple python script simulates page insertion into a cache using the FIFO algorithm.

# How to use

Simply edit the <b>cache_size</b> variable and the <b>inserts</b> list to your liking and run the program, it should output a organized series of insertions while logging page faults and current cache state.

```
inserts = [0, 3, 4, 3, 8, 6, 9, 1, 4, 9, 7, 9, 5, 3, 1, 2, 4] # Change these values according to problem set
cache_size = 4 # Change this as needed
```

# Sample Output

This is a sample output using the default values.

```
PAGE INSERT 0
====================
Value: 0
Value: EMPTY
Value: EMPTY
Value: EMPTY
====================
PAGE INSERT 3
====================
Value: 0
Value: 3
Value: EMPTY
Value: EMPTY
====================
PAGE INSERT 4
====================
Value: 0
Value: 3
Value: 4
Value: EMPTY
====================
PAGE INSERT 3
====================
Value: 0
Value: 3
Value: 4
Value: EMPTY
====================
PAGE INSERT 8
====================
Value: 0
Value: 3
Value: 4
Value: 8
====================
***PAGE FAULT***
PAGE INSERT 6
====================
Value: 6
Value: 3
Value: 4
Value: 8
====================
***PAGE FAULT***
PAGE INSERT 9
====================
Value: 6
Value: 9
Value: 4
Value: 8
====================
***PAGE FAULT***
PAGE INSERT 1
====================
Value: 6
Value: 9
Value: 1
Value: 8
====================
***PAGE FAULT***
PAGE INSERT 4
====================
Value: 6
Value: 9
Value: 1
Value: 4
====================
PAGE INSERT 9
====================
Value: 6
Value: 9
Value: 1
Value: 4
====================
***PAGE FAULT***
PAGE INSERT 7
====================
Value: 7
Value: 9
Value: 1
Value: 4
====================
PAGE INSERT 9
====================
Value: 7
Value: 9
Value: 1
Value: 4
====================
***PAGE FAULT***
PAGE INSERT 5
====================
Value: 7
Value: 5
Value: 1
Value: 4
====================
***PAGE FAULT***
PAGE INSERT 3
====================
Value: 7
Value: 5
Value: 3
Value: 4
====================
***PAGE FAULT***
PAGE INSERT 1
====================
Value: 7
Value: 5
Value: 3
Value: 1
====================
***PAGE FAULT***
PAGE INSERT 2
====================
Value: 2
Value: 5
Value: 3
Value: 1
====================
***PAGE FAULT***
PAGE INSERT 4
====================
Value: 2
Value: 4
Value: 3
Value: 1
====================
Total Inserts: 17
Total Faults: 10
```
