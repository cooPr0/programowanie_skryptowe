#!/bin/bash

# Pobierz nazwe pliku do podpisania
read -p "Podaj nazwe pliku do podpisania: " file

# Sprawdz czy plik istnieje
if [ ! -f $file ]; then
    echo "Plik $file nie istnieje"
    exit 1
fi

# Generuj klucz prywatny
openssl genrsa -out privateKey.pem 2048

# Generuj klucz publiczny - jest uzywany potem do zweryfikowania podpisu
openssl rsa -in privateKey.pem -out publicKey.pem -pubout

# Te 2 powyzsze kroki ogolnie powinny byc zrealizowane poza tym skryptem, ale dodalem tutaj komendy, ktorych wykorzystalem aby stworzyc na moim komputerze klucze prywatne i publiczne

# Podpisz plik
openssl dgst -sha256 -sign privateKey.pem -out "$file.sig" $file

echo "Podpisano plik: $file.sig"