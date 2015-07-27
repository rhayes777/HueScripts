#!/bin/bash

$ set -- "arg  1" "arg  2" "arg  3"

$ for word in $*; do echo "$word"; done
arg
1
arg
2
arg
3

$ for word in $@; do echo "$word"; done
arg
1
arg
2
arg
3

$ for word in "$*"; do echo "$word"; done
arg  1 arg  2 arg  3

$ for word in "$@"; do echo "$word"; done
arg  1
arg  2
arg  3
