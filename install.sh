#!/bin/bash
mkdir bin
if [[ -f ~/.bashrc ]]
then
    echo "export PATH+=:$(pwd)/bin" >> ~/.bashrc
    source ~/.bashrc
fi

# I know theres better ways to do this but this works for now
chmod +x src/*.py

mv ./src/scpy.py ./bin/scpy
mv ./src/scat.py ./bin/scat
mv ./src/sgrep.py ./bin/sgrep
mv ./src/syes.py ./bin/syes
mv ./src/swhoami.py ./bin/swhoami
mv ./src/sbase64.py ./bin/sbase64
mv ./src/sls.py ./bin/sls
mv ./src/sarch.py ./bin/sarch
