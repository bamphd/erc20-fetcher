import requests
import time

def fetch_page(page, size=1000, retries=5):
    url = f"https://api.socialscan.io/rest/monad-testnet/v2/explorer/token/0x922da3512e2bebbe32bcce59adf7e6759fb8cea2/top_holders?page={page}&size={size}"
    
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json().get("data", [])
            elif response.status_code == 429:
                print(f"Rate limited - waiting... (attempt {attempt + 1})")
                time.sleep(10)
            else:
                print(f"Error {response.status_code}")
                break
        except Exception as e:
            print(f"Exception: {e}")
            time.sleep(5)
    return []

all_wallets = []

for page in range(1, 101):  # 100 pages x 1000 = 100K wallets
    wallets = fetch_page(page)
    if not wallets:
        break
    all_wallets.extend([w["wallet_address"] for w in wallets])
    print(f"Page {page} fetched. Total so far: {len(all_wallets)}")
    time.sleep(1.5)

with open("erc20_wallets.txt", "w") as f:
    for wallet in all_wallets:
        f.write(wallet + "\n")

print("✅ DONE: 100K Wallets Saved!")
