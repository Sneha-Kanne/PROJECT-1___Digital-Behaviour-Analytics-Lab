"""GRIET AI/ML 2026 - Day 1
Digital Behaviour Analysis - Dataset Generator

Creates a simulated digital_behaviour.csv dataset.
Everyone gets the same columns but different numbers.
"""

import csv
import random
from datetime import datetime, timedelta

NUM_DAYS = 30
OUTPUT_FILE = "digital_behaviour.csv"

random.seed()

COLUMNS = [
    "Date",
    "Instagram_Minutes",
    "YouTube_Minutes",
    "WhatsApp_Minutes",
    "LinkedIn_Minutes",
    "Reels_Watched",
    "Videos_Watched",
    "Messages_Sent",
    "Posts_Liked",
    "Study_Minutes",
]

def make_one_day(date_text, is_weekend):
    if is_weekend:
        instagram = random.randint(60, 240)
        youtube = random.randint(60, 300)
        study = random.randint(0, 180)
        linkedin = random.randint(0, 30)
    else:
        instagram = random.randint(20, 180)
        youtube = random.randint(15, 210)
        study = random.randint(45, 360)
        linkedin = random.randint(0, 75)

    whatsapp = random.randint(10, 180)
    reels = int(instagram * random.uniform(0.6, 1.4))
    videos = max(1, int(youtube * random.uniform(0.15, 0.45)))
    messages = int(whatsapp * random.uniform(1.5, 3.5))
    likes = int(reels * random.uniform(0.2, 0.7))

    return [
        date_text, instagram, youtube, whatsapp, linkedin,
        reels, videos, messages, likes, study
    ]

def build_rows(num_days):
    rows = []
    start_date = datetime.now() - timedelta(days=num_days)

    for day_number in range(num_days):
        current = start_date + timedelta(days=day_number)
        date_text = current.strftime("%Y-%m-%d")
        is_weekend = current.weekday() >= 5
        rows.append(make_one_day(date_text, is_weekend))

    return rows

def write_csv(filename, columns, rows):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(rows)

def main():
    rows = build_rows(NUM_DAYS)
    write_csv(OUTPUT_FILE, COLUMNS, rows)
    print(f"{OUTPUT_FILE} created successfully!")
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(COLUMNS)}")

if __name__ == "__main__":
    main()
