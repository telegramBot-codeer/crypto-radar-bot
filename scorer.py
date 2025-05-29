import requests

def check_dexscreener_score(token="PEPE"):
    url = "https://api.dexscreener.io/latest/dex/pairs/ethereum"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        for pair in data.get("pairs", []):
            if token.lower() in pair.get("baseToken", {}).get("symbol", "").lower():
                price = pair.get("priceUsd", "?")
                volume = pair.get("volume", {}).get("h1")
                change = pair.get("priceChange", {}).get("m5")
                if price and volume:
                    score = 0
                    if float(volume) > 10000: score += 1
                    if change and float(change) > 10: score += 1
                    return f"Token: {token} | Preis: {price} $ | Volumen (1h): {volume} $ | Change (5min): {change}% | Score: {score}/2"
        return f"{token} nicht gefunden bei DexScreener."
    except Exception as ex:
        return f"⚠️ Fehler beim Abruf: {ex}"
