#!/bin/bash

tmux
tmux pkill -f tmux
tmux
# shellcheck disable=SC2164
cd literate-waffle
python3 main.py
