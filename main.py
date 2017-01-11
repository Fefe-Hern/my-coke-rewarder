import requests
r = requests.get('https://www.mycokerewards.com/content/home.html')

print(r.text)

# Wait for input