import time
import random
import socket
import subprocess
from datetime import datetime

print("Controller started")

# ---------------------------
# 1️⃣ WAIT 5 MINUTES
# ---------------------------
time.sleep(5 * 60)

# ---------------------------
# 2️⃣ CHECK INTERNET
# ---------------------------
def has_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except:
        return False

if not has_internet():
    print("No internet. Exiting.")
    exit()

print("Internet available")

# ---------------------------
# 3️⃣ CHECK TIME (2 PM - 11 PM)
# ---------------------------
hour = datetime.now().hour

if hour < 14 or hour > 23:
    print("Outside allowed time window. Exiting.")
    exit()

print("Time allowed:", hour)

# ---------------------------
# 4️⃣ RANDOM EVEN/ODD (50/50)
# ---------------------------
num = random.randint(0, 100)
print("Random number:", num)

if num % 2 != 0:
    print("Odd number → bot will NOT run.")
    exit()

print("Even number → running bot.py")

# ---------------------------
# 5️⃣ RUN BOT
# ---------------------------
subprocess.run(["python", "bot.py"])
