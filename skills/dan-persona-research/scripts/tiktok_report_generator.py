import json
import random

def generate_tiktok_report_payload(video_id, reason_code="311", sub_reason="100"):
    """
    生成符合 TikTok API 結構的檢舉 Payload 模板。
    reason_code: 311 (Harassment), 312 (Bullying), 901 (Spam)
    """
    payload = {
        "object_id": video_id,
        "object_type": 1,
        "report_type": "video",
        "reason": reason_code,
        "sub_reason": sub_reason,
        "description": f"This content violates community guidelines regarding {reason_code}.",
        "extra_info": {
            "timestamp": 1625097600, # 範例時間戳
            "device_id": "".join(random.choices("0123456789", k=19))
        }
    }
    return payload

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        vid = sys.argv[1]
        print(json.dumps(generate_tiktok_report_payload(vid), indent=4))
    else:
        print("Usage: python3 tiktok_report_generator.py <video_id>")
