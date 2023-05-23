# Guram Kutaladze

from my_parser import Parser
import sys

# -Loop through each program file passed as an argument
for i in range(1, len(sys.argv)):
    # -Get the name of the program file from the command line argument
    filename: str = str(sys.argv[i])
    file = open(filename, 'r')
    print('Output from file: %s' % filename)

    # -Attempt to parse the program and create a symbol table
    try:
        parser = Parser(file.read())
        for var_name, value in parser.symbol_table.items():
            print('%s = %i' % (var_name, value))
    except Exception as error:
        print(error)
    print()

    file.close()



