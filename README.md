# Intro

## Scuffed-Utils

<img src=https://github.com/honestly-nuts/Scuffed-Utils/blob/development/resources/scuffed_utils_light_very_logo.svg width=256 height=256>

This is the official repo for the infamous Scuffed-Utils project (I regret this name).

**Scuffed-Utils** is a remake of the original gnu coreutils in python. Why you may ask?
To make America great again! JK, it is to make a modular utility package that people can use as a library. And also to make modifying the programs a lot easier.

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

# How to install
#### Pre-requests
```
1.python
2.git
```
#### First clone this repository in your desired place:
```bash
git clone https://github.com/honestly-nuts/Scuffed-Utils/
```
#### Then, cd to the repository you cloned:
```bash
cd Scuffed-Utils/
```
#### Then, make sure the install script is executable and run the install script:
note: only run the install script once or it will write a duplicate path in PATH environment variable.

```bash
chmod +x install.sh
./install.sh
```
#### Then either restart your terminal or source your bashrc file with ```source ~/.bashrc```. Then you are good to go.

# For the devs

## read [this](https://github.com/honestly-nuts/Scuffed-Utils/blob/development/CONTRIBUTING.md) for contribution guidlines

# Conclusion

My email: honeastlynuts@gmail.com 

yeah, I know that the honestly is misspleled but I like it (By that I mean I don't want to fix it).
