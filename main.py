import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from cryptography.fernet import Fernet

# ==== Encryption Setup ====
KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        return generate_key()

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode()

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    try:
        decrypted = f.decrypt(encrypted_message.encode())
        return decrypted.decode()
    except:
        return "[Decryption Failed: Invalid Key or Corrupted Message]"

# ==== Steganography Logic ====
def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size

    message += chr(0)  # null character to signify end
    binary_message = ''.join([format(ord(i), '08b') for i in message])
    data_index = 0

    for y in range(height):
        for x in range(width):
            if data_index < len(binary_message):
                r, g, b = img.getpixel((x, y))
                r = (r & ~1) | int(binary_message[data_index])
                data_index += 1
                if data_index < len(binary_message):
                    g = (g & ~1) | int(binary_message[data_index])
                    data_index += 1
                if data_index < len(binary_message):
                    b = (b & ~1) | int(binary_message[data_index])
                    data_index += 1
                encoded.putpixel((x, y), (r, g, b))
            else:
                break

    encoded.save(output_path)
    return True

def decode_message(image_path):
    img = Image.open(image_path)
    binary_data = ""
    for pixel in img.getdata():
        for channel in pixel[:3]:
            binary_data += str(channel & 1)

    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        char = chr(int(byte, 2))
        if char == chr(0):
            break
        message += char
    return message

# ==== GUI ====
class StegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("StegoX - Secure Image Steganography")
        self.style = ttk.Style("superhero")  # modern theme
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(padx=10, pady=10)

        # Add a Title Label with a larger font
        title_label = ttk.Label(frame, text="Secure Steganography App", font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Encode section
        ttk.Label(frame, text="Enter Secret Message:").grid(row=1, column=0, sticky=W)
        self.message_entry = ttk.Entry(frame, width=50, font=("Arial", 14))
        self.message_entry.grid(row=1, column=1, columnspan=2, pady=5)

        ttk.Button(frame, text="Choose Image", style="success.TButton", command=self.load_image).grid(row=2, column=0, pady=5)
        ttk.Button(frame, text="Encode & Save", style="primary.TButton", command=self.encode).grid(row=2, column=1, pady=5)

        # Decode section
        ttk.Separator(frame, orient='horizontal').grid(row=3, columnspan=3, pady=15, sticky='ew')
        ttk.Button(frame, text="Choose Image to Decode", style="info.TButton", command=self.decode).grid(row=4, column=0, pady=5)

        self.decoded_text = ttk.Label(frame, text="Decoded Message will appear here", font=("Arial", 14), wraplength=400)
        self.decoded_text.grid(row=5, column=0, columnspan=3, pady=10)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp *.jpg")])
        if self.image_path:
            messagebox.showinfo("Image Selected", f"Loaded: {self.image_path}")

    def encode(self):
        message = self.message_entry.get()
        if not message:
            messagebox.showwarning("Warning", "Enter a secret message first!")
            return
        if not hasattr(self, 'image_path'):
            messagebox.showwarning("Warning", "Please choose an image to encode.")
            return

        encrypted_message = encrypt_message(message)
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if output_path:
            encode_message(self.image_path, encrypted_message, output_path)
            messagebox.showinfo("Success", f"Message encrypted and saved to {output_path}")

    def decode(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp *.jpg")])
        if image_path:
            raw = decode_message(image_path)
            decrypted = decrypt_message(raw)
            self.decoded_text.config(text=f"Decoded Message: {decrypted}")

# ==== Run App ====
if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = StegoApp(root)
    root.mainloop()
