#!/bin/bash

tmux kill-session -t literate-waffle

tmux new-session -d -s literate-waffle 'cd literate-waffle && python3 main.py'
