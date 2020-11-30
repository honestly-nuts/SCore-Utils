#!/bin/bash
if [[ -f ~/.bashrc ]]; then
    echo "export PATH+=:$(pwd)/bin" >> ~/.bashrc
    source ~/.bashrc
fi

# I know theres better ways to do this but this works for now
chmod +x *.py

for FILE in ./*.py; do
    OUTPUT=${FILE#./}
    OUTPUT=${OUTPUT%.py}
    mv $FILE /bin/$OUTPUT
done    
