#!/bin/bash

command="python light.py"

case $1 in
  "r"|"red") eval "${command} red";;
  "g"|"green") eval "${command} green";;
  "y"|"yellow") eval "${command} yellow";;
  "b"|"blue") eval "${command} blue";;
  "w"|"white") eval "${command} white";;
  "x"|"off") eval "${command} off";;
esac
