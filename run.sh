#!/bin/bash

if !(type python3.7 >/dev/null 2>&1)
then
	echo "Python3.7 não encontrado no PATH."
else
    cd $(dirname $0)
    python3.7 -m identifier_analyser "$@"
fi
