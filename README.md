# Intro

## Scuffed-Utils

<img src=https://github.com/honestly-nuts/Scuffed-Utils/blob/development/resources/scuffed_utils_light_very_logo.svg width=256 height=256>

This is the official repo for the infomous Scuffed-Utils project (I regret this name). 

The goal of this project is to remake the original gnu coreutils in python.  Why you 
may ask? Honestly, I don't know. One day I just got this Idea that, "Why not make scuffed
versions of the already great gnu coreutils programs (I still don't know what it is actually
called, oh well)". If you are interested in this project or are just doing drugs (like I am)
or both, then you may consider donating your code to this repository.

# How to install
#### Pre-requests
```
1.python
2.git
```
#### First clone this repository to your desired place:
```bash
git clone https://github.com/honestly-nuts/Scuffed-Utils/
```
#### Then, cd to the repository you cloned:
```bash
cd Scuffed-Utils/
```
#### Then, make sure the install script is executable and run the install script:
note: only run the install script once or it will write a duplicate path in PATH envirment variable.

```bash
chmod +x install.sh
./install.sh
```
#### Then either restart your terminal or source your bashrc file with ```source ~/.bashrc```.

# For the devs

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
  1. You should always make a test file in the tests directory for the devs to test your program. Currently I am working on the preprocessor to genarate the txt files which you can perform the programs on.
  Until the preprocessor is done, just add them as tutorials. syntax guidelines are given in the test/syntax.test file.

# Conclusion

[*Very good documentation*](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab)

My email: honeastlynuts@gmail.com 

yeah, I know that the honestly is misspleled but I like it (By that I mean I don't want to fix it).
