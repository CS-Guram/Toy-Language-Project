# Project CISC 3160 
# Guram Kutaladze

#  The interpreter is able to do the following taks for a given program:
--------------------------------------------------------------
(1) detect syntax errors;
(2) report uninitialized variables;
(3) perform the assignments if there is no errors;
(4) print out the values of all the variables after all assignments are done

# How to test
--------------
You can interpret multiple programs in sequence by passing multiple program files as arguments to the interpreter. For instance, to interpret all example programs provided in the example_files directory, you can use the following command:

// python my_interpreter.py example_files/example1.toy example_files/example2.toy example_files/example3.toy example_files/example4.toy 