#!/bin/bash

# Sprawdzenie czy podano argument
if [ $# -eq 0 ]; then
    echo "Nie podano argumentu"
    exit 1
fi

# Sprawdzenie czy argument jest liczbą
if ! [[ $1 =~ ^[0-9]+$ ]]; then
    echo "Argument nie jest liczbą"
    exit 1