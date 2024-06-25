#!/bin/bash

tmux
tmux pkill -f tmux
tmux

cd literate-waffle
python3 main.py
