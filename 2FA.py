# import getpass

# password = getpass.getpass("Enter your password: ")
# print("You typed:", password)


import random
import getpass

# ---------- Step 1: Fake user database ----------
users = {
    "alice": "password123",
    "bob": "mypassword",
    "admin": "admin123"
}

# ---------- Step 2: Login function ----------
def login():
    username = input("Enter username: ")
    password = getpass.getuser("Enter password: ")  # hides input

    
    
    if username in users and users[username] == password:
        print("✅ Password correct!")
        return True
    else:
        print("❌ Invalid username or password")
        return False

# ---------- Step 3: Generate OTP ----------
def generate_otp():
    otp = random.randint(100000, 999999)  # 6-digit OTP
    print(f"📩 Your OTP is: {otp}")  # (in real life, send via SMS/Email)
    return otp

# ---------- Step 4: OTP verification ----------
def verify_otp(otp):
    user_input = int(input("Enter the OTP: "))
    if user_input == otp:
        print("🎉 Login Successful! Access Granted.")
    else:
        print("❌ Wrong OTP! Access Denied.")

# ---------- Main Program ----------
if __name__ == "__main__":
    print("=== Login System with 2FA ===")
    
    if login():
        otp = generate_otp()
        verify_otp(otp)
