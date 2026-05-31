import ssl
import requests
from requests.adapters import HTTPAdapter

class TLSAdapter(HTTPAdapter):
    """
    自定義 TLS 適配器，用於模擬特定的 JA3 指紋。
    """
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        # 設定特定的密碼套件順序以模擬 Chrome
        context.set_ciphers('ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384')
        context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
        kwargs['ssl_context'] = context
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

def fetch_with_stealth_tls(url):
    session = requests.Session()
    session.mount('https://', TLSAdapter())
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    response = session.get(url, headers=headers)
    return response.status_code

if __name__ == "__main__":
    print(f"Status Code with Spoofed TLS: {fetch_with_stealth_tls('https://api.ipify.org')}")
