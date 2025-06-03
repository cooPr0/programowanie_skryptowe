#!/bin/bash

# Wez plik do zaszyfrowania
read -p "Podaj plik do zaszyfrowania: " file

# Pobierz nazwe pliku bez rozszerzenia
filename="${file%.*}"

# Zaszyfruj plik
openssl enc -aes-256-cbc -in "$file" -out "$filename.enc"

# Wyswietl nazwe zaszyfrowanego pliku
echo "Zaszyfrowano plik: $filename.enc"