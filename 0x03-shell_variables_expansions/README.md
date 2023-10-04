| `0-alias` | Creates an alias |


0-alias

#!/bin/bash
alias ls="rm *"
This script creates an alias named "ls" that, when executed, actually runs the command rm *, which deletes all files in the current directory. It's essentially a mischievous alias that makes the ls command behave like the rm command.

| `1-hello_you` | Prints `hello user`, where user is the current Linux user |

1-hello_you

#!/bin/bash
echo "hello $USER"
This script prints a greeting message "hello" followed by the current Linux user's username, which is obtained using the $USER environment variable.

| `2-path` | Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program |

2-path

#!/bin/bash
export PATH=$PATH:/action
This script adds the directory /action to the end of the PATH environment variable. It allows the shell to search for executable programs in the /action directory when you enter a command.

| `3-paths` | Counts the number of the directories in the `PATH` |

3-paths

#!/bin/bash
echo $((`echo $PATH | grep -o ":/" | wc -l`+ 1))
This script counts the number of directories in the PATH variable. It does so by using a combination of commands: echo $PATH displays the PATH variable, grep -o ":/" searches for colons followed by slashes (the separator between directories), and wc -l counts the number of lines (which corresponds to the number of directories). Adding 1 accounts for the directory before the first colon.
		
| `4-global_variables` | Lists environment variables |

4-global_variables

#!/bin/bash
printenv
This script lists all environment variables using the printenv command. It displays a comprehensive list of variables and their values.

| `5-local_variables` | Lists all local variables and environment variables, and functions |

5-local_variables

#!/bin/bash
set
The set command lists all local variables, environment variables, and functions in the current shell session.

| `6-create_local_variable` | Creates a new local variable named `BETTY` |

6-create_local_variable

#!/bin/bash
BEST="School"
This script creates a new local variable named BEST and assigns it the value "School."
		
| `7-create_global_variable` | Creates a new global variable named `HOLBERTON` |

7-create_global_variable

#!/bin/bash
export BEST=School
This script creates a new global variable named BEST and assigns it the value "School." The export keyword ensures that the variable is available in the environment for other scripts and processes.
	
| `8-true_knowledge` | Prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line |

8-true_knowledge

#!/bin/bash
echo $(($TRUEKNOWLEDGE + 128))
This script prints the result of adding 128 to the value stored in the environment variable TRUEKNOWLEDGE.
		
| `9-divide_and_rule` | Prints the result of `POWER` divided by `DIVIDE`, followed by a new line |

9-divide_and_rule

#!/bin/bash
echo $(($POWER / $DIVIDE))
This script prints the result of dividing the value stored in the environment variable POWER by the value stored in the environment variable DIVIDE.

| `10-love_exponent_breath` | Displays the result of `BREATH` to the power `LOVE` |

10-love_exponent_breath

#!/bin/bash
echo $((BREATH**$LOVE))
This script calculates and prints the result of raising the value stored in the variable BREATH to the power of the value stored in the variable LOVE.

| `11-binary_to_decimal` | Converts a number from base 2 to base 10 |

11-binary_to_decimal

#!/bin/bash
echo "$((2#$BINARY))"
This script converts a number from base 2 (binary) to base 10 (decimal) using the 2# prefix before the variable name BINARY.

| `12-combinations` | Prints all possible combinations of two letters, except `oo` |

12-combinations

#!/bin/bash
echo {a..z}{a..z} | tr " " "\n" | grep -v "oo"
This script generates all possible combinations of two letters from 'a' to 'z', excluding the combination "oo." It uses brace expansion {a..z}{a..z}, changes the space delimiter to a newline with tr, and filters out combinations containing "oo" using grep -v.

| `13-print_float` | Prints a number with two decimal places. The number is stored in the environment variable `NUM` |

13-print_float

#!/bin/bash
printf "%.2f" $NUM | sort
This script prints the value stored in the environment variable NUM as a floating-point number with two decimal places. The result is then sorted.
		
| `100-decimal_to_hexadecimal` | Converts a number from base 10 to base 16 |

100-decimal_to_hexadecimal

#!/bin/bash
printf '%x\n' $DECIMAL
This script converts a number from base 10 (decimal) to base 16 (hexadecimal) using the printf command with the %x format specifier.

		
| `101-rot13` | Encodes and decodes text using the rot13 encryption |

101-rot13

#!/bin/bash
tr 'A-Za-z' 'N-ZA-Mn-za-m'
This script performs a simple ROT13 encryption and decryption on text input. It translates uppercase and lowercase letters by shifting them 13 positions in the alphabet.

| `102-odd` | Prints every other line from the input, starting with the first line |

102-odd

#!/bin/bash
perl -lne 'print if $. % 2 ==1'
This script prints every other line from the input, starting with the first line, using Perl. It checks if the line number ($.) is odd ($. % 2 == 1) and prints the line if it is.
	
| `103-water_and_str` | Adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result |

103-water_and_stir

#!/bin/bash
echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'bestchol')
This script performs a series of operations on the environment variables WATER and STIR. It converts them from custom base-5 representations ('water' and 'stir.') to octal, adds them, converts the result to a custom base-8 representation, and then uses tr to translate the digits to 'bestchol'.
