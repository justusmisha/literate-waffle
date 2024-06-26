#!/bin/bash

pkill -f tmux

tmux new-session -d -s literate-waffle 'cd literate-waffle && python3 main.py'
