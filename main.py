import requests

def getkey(keysrc):
    response = requests.get(keysrc)
    keys = response.text

    print("Keys:")
    print(keys)

if __name__ == "__main__":
    keysrc = "https://raw.githubusercontent.com/Rvlndd/Cloudflare-Warp-Keys/main/raw.txt"
    getkey(keysrc)
  
