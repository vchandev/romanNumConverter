# romanNumConverter
A Python program to convert regular numbers to Roman numerals

This program uses a for loop to cycle through all of the possible keys in the romanDict (dictionary that stores Roman numerals and their Arabic numeral equivalents). When the number is divided by one of the keys, we record the number of times the key goes into the num and store it as quotient. Hence, the number of times that Roman numeral will appear. For example, 40 / 10 will be 4. The key is 10, and the Roman numeral is X. The X will appear 4 times. 

When the remainder of the number is less than 10, it will simply match up with one of the stored key value pairs in the Roman numeral dictionary. The Roman numeral string appends any new valid values, builds the complete Roman numeral and is returned to the main method where it is displayed.

<img width="172" alt="screenshot" src="https://user-images.githubusercontent.com/25806927/39404373-f8d966f0-4b5f-11e8-9a0d-e1320c3bdd60.png">
