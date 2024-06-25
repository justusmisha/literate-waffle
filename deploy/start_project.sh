#!/bin/bash

tmux
tmux kill-session -t 0
# shellcheck disable=SC2164
cd literate-waffle
python3 main.py
