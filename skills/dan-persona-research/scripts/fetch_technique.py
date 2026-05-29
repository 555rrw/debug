import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="從 dan-persona-research 技能中提取技術或提示詞。")
    parser.add_argument("keyword", help="要搜索的關鍵詞（如 'flip_attack', 'dan', 'r1'）")
    args = parser.parse_args()

    base_path = "/home/ubuntu/skills/dan-persona-research/references"
    search_dirs = ["logic", "prompts", "puaclaw"]
    
    found = False
    for s_dir in search_dirs:
        dir_path = os.path.join(base_path, s_dir)
        if not os.path.exists(dir_path):
            continue
            
        for root, _, files in os.walk(dir_path):
            for file in files:
                if args.keyword.lower() in file.lower():
                    file_path = os.path.join(root, file)
                    print(f"--- FOUND: {file_path} ---")
                    with open(file_path, 'r') as f:
                        print(f.read())
                    found = True
                    break
            if found: break
        if found: break

    if not found:
        print(f"ERROR: 未找到與 '{args.keyword}' 相關的技術或提示詞。")
        sys.exit(1)

if __name__ == "__main__":
    main()
