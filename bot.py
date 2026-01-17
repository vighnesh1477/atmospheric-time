import json
import subprocess
import random
from datetime import datetime

print("Bot started")

# ---------------------------
# 0️⃣ ALWAYS SYNC FIRST
# ---------------------------
subprocess.run(["git", "pull", "--no-rebase"], check=False)

# ---------------------------
# 1️⃣ COMMIT MESSAGE POOL
# ---------------------------
commit_messages = [
    "Updated date data",
    "Date data refreshed",
    "New date info added",
    "Date update complete",
    "Data synced with current date",
    "Date changes committed",
    "Updated with latest date",
    "Date data overhaul",
    "Fresh date data uploaded",
    "Date info updated",
    "Committing date update",
    "Latest date data applied",
    "Date data now current",
    "Update date info",
    "Date refresh complete",
    "New date data live",
    "Date update pushed",
    "Current date data committed",
    "Date info refreshed",
    "Updated to latest date data"
]

commit_message = random.choice(commit_messages)

# ---------------------------
# 2️⃣ MOTIVATION POOL
# ---------------------------
quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Keep your eyes on the stars, and your feet on the ground. - Theodore Roosevelt",
    "You don't have to be great to start, but you have to start to be great. - Zig Ziglar",
    "The best is yet to come. - Robert Browning",
    "Do something today that your future self will thank you for. - Unknown",
    "Motivation is what gets you started. Habit is what keeps you going. - Jim Rohn",
    "You are stronger than you seem, braver than you believe, and smarter than you think. - Christopher Robin",
    "The harder you work for something, the greater you'll feel when you achieve it. - Unknown",
    "Dream big and dare to fail. - Norman Vaughan",
    "Life is 10% what happens to you and 90% how you react to it. - Charles R. Swindoll",
    "The key is not to prioritize what's on your schedule, but to schedule your priorities. - Stephen Covey",
    "You don't need to be perfect, you just need to be better than you were yesterday. - Unknown",
    "Chase your dreams until they become your reality. - Unknown"
]

quote = random.choice(quotes)

# ---------------------------
# 3️⃣ DATE DATA
# ---------------------------
now = datetime.now()

date_data = {
    "day": f"{now.day:02d}",
    "month": now.strftime("%b").upper(),
    "year": str(now.year),
    "quote": quote
}

# ---------------------------
# 4️⃣ WRITE date.json
# ---------------------------
with open("date.json", "w") as f:
    json.dump(date_data, f, indent=2)

print("date.json updated:", date_data)

# ---------------------------
# 5️⃣ COMMIT & PUSH
# ---------------------------
subprocess.run(["git", "add", "date.json"])
subprocess.run(["git", "commit", "-m", commit_message], check=False)
subprocess.run(["git", "push"], check=False)

print("Commit message used:", commit_message)
print("Bot finished")
