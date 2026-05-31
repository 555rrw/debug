import pyfiglet

def text_to_art(text, font="small"):
    """
    將敏感詞轉換為 ASCII 藝術以繞過語義過濾。
    """
    try:
        art = pyfiglet.figlet_format(text, font=font)
        return art
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target_text = sys.argv[1]
        print(f"Original: {target_text}")
        print("-" * 20)
        print(text_to_art(target_text))
    else:
        print("Usage: python3 artprompt_converter.py <text>")
