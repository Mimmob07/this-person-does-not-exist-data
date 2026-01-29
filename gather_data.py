import urllib.request

url = "https://thispersondoesnotexist.com/"
# Spoof chrome on a windows 10 computer
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

for i in range(1, 1001):
    filename = f"assets/img_{i}.jpeg"
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response, open(filename, "wb") as file:
        file.write(response.read())

    print(f"Saved file {filename}")
