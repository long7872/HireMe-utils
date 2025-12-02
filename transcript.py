from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
from datetime import datetime

def fetch_interviewingio_transcript(interview_url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    print(f"🚀 Opening {interview_url}")
    driver.get(interview_url)
    time.sleep(2)

    for attempt in range(5):
        print(f"🔎 Attempt {attempt+1}/5...")

        # Scroll để nội dung transcript load đầy đủ
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # Tìm theo selector đúng
        blocks = driver.find_elements(By.CSS_SELECTOR, "div.whitespace-pre-wrap")
        print(f"📌 Found {len(blocks)} blocks using 'div.whitespace-pre-wrap'")

        if blocks:
            transcript = "\n\n".join([b.text.strip() for b in blocks if b.text.strip()])
            print("🟢 Transcript found!")
            driver.quit()
            return transcript

        time.sleep(1)

    # Backup: lưu HTML để bạn debug nếu vẫn fail
    with open("debug_interviewingio.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("❌ Failed to fetch transcript, saved debug_interviewingio.html")
    
    driver.quit()
    return None


def save_interviewingio_transcript(transcript_text, interview_id):
    output_dir = "transcripts/interviewingio"
    os.makedirs(output_dir, exist_ok=True)

    filename = f"{output_dir}/{interview_id}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"SOURCE: interviewing.io\n")
        f.write(f"INTERVIEW_ID: {interview_id}\n")
        f.write(f"COLLECTED: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("="*80 + "\n\n")
        f.write("Interview Transcript\n")
        f.write(transcript_text)

    print(f"💾 Saved: {filename}")
    return filename

# ========================
# MAIN SCRIPT
# ========================

interviewingio_links = [
    "https://interviewing.io/mocks/google-system-design-design-youtube",
    "https://interviewing.io/mocks/google-machine-learning-personalized-newsfeed-system",
    "https://interviewing.io/mocks/amazon-system-design-calendar-system",
    "https://interviewing.io/mocks/amazon-system-design-charity-donating-system",
    "https://interviewing.io/mocks/amazon-system-design-amazon-ranking-system",
    "https://interviewing.io/mocks/netflix-system-design-payment-pipeline",
    "https://interviewing.io/mocks/meta-system-design-ml-instagram-reels",
    "https://interviewing.io/mocks/facebook-system-design-centralized-ml-management-platform",
    "https://interviewing.io/mocks/microsoft-system-design-gaming-leaderboard",
    "https://interviewing.io/mocks/faang-system-design-design-coderpad",
    "https://interviewing.io/mocks/faang-system-design-design-robinhood",
    "https://interviewing.io/mocks/facebook-system-design-design-live-comments",
    "https://interviewing.io/mocks/facebook-system-design-design-a-free-food-app",
    "https://interviewing.io/mocks/google-system-design-design-facebook-events",
    "https://interviewing.io/mocks/faang-system-design-designing-whatsapp",
    "https://interviewing.io/mocks/facebook-system-design-design-online-judge",
    "https://interviewing.io/mocks/amazon-system-design-design-leetcode",
    "https://interviewing.io/mocks/faang-system-design-ml-detect-scam-and-fraudulent-practices",
    "https://interviewing.io/mocks/ml-harmful-content-removal",
    "https://interviewing.io/mocks/amazon-behavioral-leadership-principles"
]

print("\n" + "="*80)
print("🌐 FETCHING INTERVIEWING.IO TRANSCRIPTS")
print("="*80)

successful_io = []
failed_io = []

for i, url in enumerate(interviewingio_links[:5], 1):
    print(f"\n[{i}/5] {url}")
    
    interview_id = url.split('/')[-1]
    output_path = f"transcripts/interviewingio/{interview_id}.txt"
    
    if os.path.exists(output_path):
        print(f"⏭️  Already exists")
        successful_io.append(url)
        continue
    
    transcript_text = fetch_interviewingio_transcript(url)
    
    if transcript_text and len(transcript_text) > 100:
        save_interviewingio_transcript(transcript_text, interview_id)
        successful_io.append(url)
    else:
        failed_io.append(url)
    
    time.sleep(1)

print("\n✔ Done!")
print("🟢 Successfully fetched:", len(successful_io))
print("🔴 Failed:", len(failed_io))
