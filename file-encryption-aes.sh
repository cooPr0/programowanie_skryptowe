#!/bin/bash

# Wez plik do zaszyfrowania
read -p "Podaj plik do zaszyfrowania: " file

# Sprawdz czy plik istnieje
if [ ! -f $file ]; then
    echo "Plik $file nie istnieje"
    exit 1
fi

# Pobierz nazwe pliku bez rozszerzenia
filename="${file%.*}"

# Zaszyfruj plik
openssl enc -aes-256-cbc -in "$file" -out "$filename.enc"

# Wyswietl nazwe zaszyfrowanego pliku
echo "Zaszyfrowano plik: $filename.enc"