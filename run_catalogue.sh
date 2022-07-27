#!/bin/bash
if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2
  exit 1
fi
pip install -r requirements.txt
python main.py