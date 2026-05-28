import requests
import sys
import json

def fetch_game_info(game_name, api_key=None):
    """
    獲取遊戲資訊的範例腳本。
    """
    if not api_key:
        print("請提供 RAWG API Key。")
        return None
    
    url = f"https://api.rawg.io/api/games?search={game_name}&key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('results', [])
    except Exception as e:
        print(f"發生錯誤: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 fetch_game_data.py <遊戲名稱> [API_KEY]")
    else:
        name = sys.argv[1]
        key = sys.argv[2] if len(sys.argv) > 2 else None
        results = fetch_game_info(name, key)
        if results:
            print(json.dumps(results[0], indent=2, ensure_ascii=False))
