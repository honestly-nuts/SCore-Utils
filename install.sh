#!/bin/bash
mkdir bin
if [[ -f ~/.bashrc ]]
then
    echo "export PATH+=:$(pwd)/bin" >> ~/.bashrc
    source ~/.bashrc
fi

# I know theres better ways to do this but this works for now
chmod +x *.py

mv scpy.py ./bin/scpy
mv scat.py ./bin/scat
mv sgrep.py ./bin/sgrep
mv syes.py ./bin/syes
mv swhoami.py ./bin/swhoami

