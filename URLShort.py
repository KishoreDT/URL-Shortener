import requests

api_key = "2f28518d9b419acb1e145775beba4ec9665f5"
url = input("Enter URL to Shorten : ")
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)
