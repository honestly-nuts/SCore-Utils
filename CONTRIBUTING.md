### If you want to contribute, here are some guidelines:

#### 1. Error handling:
  1. You should check the length of sys.argv for errors at the ``` if __name__ == "__main__": ``` code block.
  2. If you have too few or too many sys.arguments then you should ```sys.stderr.out("Too many/few arguments")```.
  3. You should always ``` sys.stderr.write("Usage: program_name arguments")```(not literally) after an error.
#### 2. Styling
  1. You should use _ inbetween words (eg. grep_file).
  2. You should make comments to explain what a line or block does
  3. You should create non-gibrish variable and function names.
#### 3. Program standards
  1. You should always make a test file in the tests directory for the devs to test your program.
    Test files are manuals on which you can run [my preprocessor](https://github.com/honestly-nuts/TPP) on to generate an
    inputfile for your program. Read More about TPP [here](https://github.com/honestly-nuts/TPP/blob/master/README.md).
    The syntax guidelines are given [here](https://github.com/honestly-nuts/TPP/blob/master/tests/syntax.test).
    [here](https://github.com/honestly-nuts/TPP/blob/master/tests/example_programName.test) is an example test file for an **imaginary** program that does        
    virtually nothing.

## Did not fit in any sections:
  1. I suggest you to stick to the standard library if you can. But if you can't then you should list how to install the library in the requirments subsection in 
  the [readme](https://github.com/honestly-nuts/Scuffed-Utils/blob/development/README.md) like so:
  
    python
     - Library name: command to install it (eg. pip[3] install library)
    git
    
Feel free to suggest guidelines that you think should be in here but are not because I have a brain that has a size of -1 units;

[Here's the trello board for this project. (inactive)](https://trello.com/invite/b/d7KbCuUN/216104d5bd17c6032b142875dc14d561/scuffed-utils)
[Here's the github board for this project.](https://github.com/honestly-nuts/Scuffed-Utils/projects)
