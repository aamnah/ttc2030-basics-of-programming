 # Basics of Programming

## Exercises 9: Exception Handling

### 9.1.
Make a program where you try to change a value in the list that does not exist. Start with a list of four elements and then try to change the fifth element. Check what kind of exception you get.
Repair the program so that it does not crash.

### 9.2.
Make a program to try to read all the files on the root of the hard disk C on a Windows machine (on macOS/Linux/Unix machines try to read the user's root directory). View files on the console. Then try adding the file '*ayho.txt*' to the root of C (on macOS/Linux/Unix to the user's root directory).
What happened? Repair the program so that it does not crash.
![](./img/macos.png)
Bonus Question: With what permissions could you add files on macOS/Linux/Unix machines to the root directory? Reply as a comment to the source code.

### 9.3.
Check out the *TypeError* exception in this document:
https://docs.python.org/3/library/exceptions.html

Implement the function **isthiszero(num)**. The function accepts one parameter. The function returns true if the parameter value is zero. The function returns false if the parameter is a number but not zero. The function raises the *TypeError* exception if the parameter is not a number. Try calling functions with different values from the program. For the calling program, use **try**-**except**. What do you notice? Answers to the beginning of the task as comments.

### 9.4.
Make a collection with 5 strings.
Ask the user index where in the table the user wants to modify existing text.
Ask the user for the new text and put it in a table in the index provided by the user.
Print the contents of the table.
Repair the program so that it does not crash if the user enters an index that is outside the table.
Tell the user if the index is not valid and ask to enter it again.
