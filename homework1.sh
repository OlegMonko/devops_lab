#!/bin/bash

pyenv install 2.7.15
pyenv install 3.5.5

pyenv virtualenv 2.7.15 python2 || echo "Virtualenv python2 already exists" 
pyenv virtualenv 3.5.5 python3 || echo "Virtualenv python3 already exists" 


