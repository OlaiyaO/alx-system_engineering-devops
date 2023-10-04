
| 0-current_working_directory | Prints the absolute path name of the current working directory |
0-current_working_directory
#!/bin/bash
pwd

This script uses the pwd (print working directory) command to print the absolute path of the current working directory.

| 1-listit | Display the contents list of your current directory |
1-listit
#!/bin/bash
ls

This script uses the ls command to list the contents (files and directories) of the current directory

| 2-bring_me_home | Changes the working directory to the user's home directory |
2-bring_me_home
#!/bin/bash
cd ~

This script uses the cd command to change the working directory to the user's home directory, represented by the ~ symbol.

| 3-listfiles | Displays the current directory contents in long format |
3-listfiles
#!/bin/bash
ls -l

This script uses the ls command with the -l option to list the contents of the current directory in long format, which provides detailed information about files and directories.

| 4-listmorefiles | Displays current directory contents, including hidden files, in long format |
4-listmorefiles
#!/bin/bash
ls -la

This script uses the ls command with the -a and -l options to list all contents of the current directory, including hidden files, in long format.

| 5-listfilesdigitonly | Displays current directory contents in long format with user and group IDs displayed numerically and hidden files |
5-listfilesdigitonly
#!/bin/bash
ls -lna


This script uses the ls command with the -l, -n, and -a options to list the contents of the current directory in long format, displaying user and group IDs numerically and showing hidden files.

| 6-firstdirectory | Creates a directory named my_first_directory in /tmp/ |
6-firstdirectory
#!/bin/bash
mkdir /tmp/my_first_directory

This script uses the mkdir command to create a new directory named my_first_directory in the /tmp/ directory.

| 7-movethatfile | Moves the file betty from /tmp/ to /tmp/my_first_directory/|
7-movethatfile
#!/bin/bash
mv /tmp/betty /tmp/my_first_directory/

This script uses the mv command to move the file named betty from the /tmp/ directory to the /tmp/my_first_directory/ directory.

| 8-firstdelete | Deletes the file betty |
8-firstdelete
#!/bin/bash
rm /tmp/my_first_directory/betty

This script uses the rm command to delete the file named betty from the /tmp/my_first_directory/ directory.

| 9-firstdirdeletion | Deletes the directory my_first_directory in /tmp/ |
9-firstdirdeletion
#!/bin/bash
rmdir /tmp/my_first_directory

This script uses the rmdir command to delete the directory named my_first_directory from the /tmp/ directory.

| 10-back | Changes the working directory to the previous one |
10-back
#!/bin/bash
cd -

This script uses the cd(change directory) command with the - (back) option to change the working directory to the previous directory it was in.

| 11-lists | Lists files and directories in the current directory, parent directory, and /boot/ directory in long format |
11-lists
#!/bin/bash
ls -l -a . .. /boot

This script uses the ls command to list files and directories in the current directory, parent directory (..), and /boot/ directory in long format.

| 12-file_type | Prints the type of the file named iamafile in /tmp/ |
12-file_type
#!/bin/bash
file /tmp/iamafile

This script uses the file command to determine and print the type of the file named iamafile located in the /tmp/ directory.

| 13-symbolic_link | Creates a symbolic link named __ls__ to /bin/ls in the current working directory |
13-symbolic_link
#!/bin/bash
ln -s /bin/ls __ls__

This script uses the ln command to create a symbolic link named __ls__ that points to the /bin/ls executable in the current working directory.

|14-copy_html | Copies HTML files from the current directory to the parent directory if they don't exist or are newer|
14-copy_html
#!/bin/bash
cp -u *.html ..

This script uses the cp command with the -u option to copy HTML files from the current directory to the parent directory (..) only if they don't exist in the parent directory or are newer.

|100-lets_move | Moves files beginning with an uppercase letter to the directory /tmp/u/|
100-lets_move
#!/bin/bash
mv [[:upper:]]* /tmp/u

This script uses the mv command to move files that start with an uppercase letter to the directory /tmp/u/.

|101-clean_emacs | Deletes files in the current directory ending with ~ |
101-clean_emacs
#!/bin/bash
rm *~

This script uses the rm command to delete files in the current directory that end with the ~ character.

| 102-tree | Creates directories welcome/, welcome/to/, and welcome/to/school/ with limited lines |
102-tree
#!/bin/bash
mkdir -p welcome/to/school

This script uses the mkdir command with the -p option to create the directories welcome/, welcome/to/, and welcome/to/school/ in the current directory.


| 103-commas | Lists files and directories with specific formatting, including sorting |
103-commas
#!/bin/bash
ls -xamp

This script uses the ls command with various options to list files and directories in a specific format, separated by commas, with directories ending in slashes.


