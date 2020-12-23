# Intro
## SCore-Utils ( working name )

<img src=https://github.com/honestly-nuts/Scuffed-Utils/blob/development/resources/scuffed_utils_dark_logo_python_scheme.svg width=300 height=280>

 \# this is a legacy line to remind me of my roots \# This is the official repo for the infamous Scuffed-Utils project (I regret this name).

**SCore-Utils** is a remake of the original gnu coreutils in python. The goal of this project is to make a modular utility package that people can use as a library and to make modifying the programs a lot easier.

# Advantages over the original
  1. Is easier to contribute to:

     1. The original core-utils is written in c. And even though I **love** C as a language, I can't really say it is easy to work with. If you don't use an IDE, building
    big projects is a pain in the *cough* *cough* (make I hate you). That's where python comes in handy, Python is an **interpreted language**. While it does impact its speed a little bit,
    comes with its advantages such as: platform independent, doesn't need to compile, etc. So no matter how many imports you have you just `./program` and it just works.
    Another advantage of python is that it's a very readable and semi-easy to learn language. So even if you don't know python but know other languages, you can easily modify the code after learning
    python over a weekend.

     2. contrary to popular belief, This is a small project. So if you notice a bug in a program or want to add your own implementation of a program or want to add a 
    new program, there is a greater chance that your pull request will be accepted here than The original core-utils.

  2. Modular:
     1. All the programs used in this repository are designed to be flexible and fairly self-contained. So if you want to use any of the functions from a program, You can just import the program.

### Why, just Why should you use this.
While these programs are not an improvement in functionality from the original programs (they do the same thing). But when it comes to reading the source code and 
source code modification, I think we can agree this is much better. Again, This is not an replacement for the original programs. This project tends to be useful
for programmers and tinkeres. if you want to make your own customized version of 'ls' but don't want to code it from scratch, for the original programs you have to
download the source code and then modify it and then compile it and **wait** you just got five hundred errors because you forgot to modify the header files.
But if you use these programs and want to customize the sls program. Just go to the $Location/bin/ folder and modify the code and it's that easy. AND I know python
is slower and stuff but on mordern computers it hardly makes a difference given the size of these programs. And even after that you don't find it useful then just don't
use it. It's not like I'm holding you at gun point.

# How to install
#### Pre-requests
```
1.python
2.git
```
#### First clone this repository in your desired place:
```bash
git clone https://github.com/honestly-nuts/SCore-Utils/
```
#### Then, cd to the repository you cloned:
```bash
cd SCore-Utils/
```
#### Then, make sure the install script is executable and run the install script:
note: only run the install script once or it will write a duplicate path in PATH environment variable.

```bash
chmod +x install.sh
./install.sh
```
#### Then either restart your terminal or source your bashrc file with ```source ~/.bashrc```. Then you are good to go.

## But what about windows.

well If you are on windows, I recommend you to use gitbash. I'm not completely sure that the install.sh will work on gitbash, if so then add the path of the  
src folder in the environment path variable. while this works, you have to type "program.py" instead of "program". So I'm looking into making a bat script. 
If anyone is on windows, please help me out.

# For the devs

## read [this](https://github.com/honestly-nuts/SCore-Utils/blob/development/CONTRIBUTING.md) for contribution guidlines

# Conclusion

My email: honeastlynuts@gmail.com 

yeah, I know that the honestly is misspleled but I like it (By that I mean I don't want to fix it).
