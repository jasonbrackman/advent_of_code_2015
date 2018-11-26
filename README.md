# Advent of Code 2015

Rust practice

* Day_01 - Wrote tests first and had an opportunity to play with chaining iterators.  Sort of like List Comprehensions for Python.
* Day_02 - Had some issues with min/max - Python is a lot easier to pull those items from a list()
* Day_03 - Working with HashMap
* Day_04 - md5 crate used - bit of jankiness working with u8.  Should optimize this -- but answers were found.
* Day_05 - String Manipulation / Peeking(), split, take, ... 
* Day_06 - Working with the regex crate and stack issues with vec / also line endings are different on mac/pc
* Day_07 - Working with HashMaps - which feels like a type of smart pointer.
* Day_08 - Nothing of real note with regards to Rust on this one .. 
* Day_09 - Used the 'permutohedron' crate (permutation). Also worked with Vec.sort() - sort needs to be called for some reason on its own line.  You can't println!() it, for example.
* Day_10 - Was running in release and part_b only took 1.1s but guessing this would have been quite longer outside of rust?  Also the code is pretty ugly here -- so optimizations are likely :).
* Day_11 - This was pretty sloppy -- mostly string manipulations -- but runs extremely quickly in release -- didn't even bother to work on some optimizations.
* Day_12 - 