#!/bin/bash

echo "" && echo "===================================================== PROJECT INIT" && echo ""

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    source .venv/bin/activate
    pip install wheel
    pip install -r requirements.txt
else
    echo "Project already initialized."
fi
