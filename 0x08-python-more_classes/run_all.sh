#!/bin/bash

# Run all Python scripts in the background
./0-rectangle.py &
./1-rectangle.py &
./2-rectangle.py &
./3-rectangle.py &
./4-rectangle.py &
./5-rectangle.py &
./6-rectangle.py &
./7-rectangle.py &
./8-rectangle.py &
./9-rectangle.py &
./10-square.py &

# Wait for all background processes to finish
wait

# Run the test scripts
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
./5-main.py
./6-main.py
./7-main.py
./8-main.py
./9-main.py
./10-main.py
