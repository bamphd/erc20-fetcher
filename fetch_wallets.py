import requests

url = "https://api.socialscan.io/rest/monad-testnet/v2/explorer/token/0x922da3512e2bebbe32bcce59adf7e6759fb8cea2/top_holders?page=1&size=100000"
response = requests.get(url)
data = response.json()

wallets = [holder["wallet_address"] for holder in data.get("data", [])]

with open("erc20_wallets.txt", "w") as f:
    for wallet in wallets:
        f.write(wallet + "\n")
