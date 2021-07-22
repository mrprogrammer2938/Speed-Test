#!/usr/bin/env bash
# This Code write by Mr.nope
# Speed-Test 1.2

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Please, Run This Programm as Root!"
  echo ""
  exit 1
fi
main
main() {
  printf '\033]2;Speed-Test/Installing'
  clear
  echo "Installing..."
  chmod +x speed.py
  sleep 2
  apt install python
  apt install python3
  apt install python3-pip
  pip3 install --upgrade pip
  echo ""
  echo "Finish ;)"
  echo "
Usage:
      python3 speed.py
      "
  exit 1
}