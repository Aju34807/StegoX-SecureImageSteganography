🔐 StegoX - Secure Image Steganography App
==========================================

📌 Overview
-----------

**StegoX** is a secure image steganography application that enables users to **encode and decode hidden messages** within images using **AES encryption**. Built with Python, it features a modern GUI using **ttkbootstrap** and ensures high-level security through the **cryptography** library.

* * * * *

✨ Features
----------

-   🧬 **Message Encoding**: Embed secret messages inside image files.

-   🕵️‍♂️ **Message Decoding**: Extract hidden messages from encoded images.

-   🔒 **AES Encryption**: Secure your messages with industry-standard AES encryption.

-   🖥️ **User-friendly Interface**: Intuitive GUI built with **ttkbootstrap**.

* * * * *

⚙️ Prerequisites
----------------

Ensure the following are installed:

-   Python **3.8+**

-   **pip** (Python package manager)

* * * * *

📥 Installation
---------------

### 1\. Clone the Repository

```bash
`git clone https://github.com/yourusername/StegoX.git
cd StegoX`
```

### 2\. Install Dependencies

Using `requirements.txt`:
```bash
`pip install -r requirements.txt`
```
Or manually:
```bash
`pip install pillow cryptography ttkbootstrap`
```
* * * * *

🚀 Usage
--------

### Run the App
`python main.py`

### 🔧 Steps to Use

#### Encode a Message

1.  Enter your secret message in the **"Secret Message"** field.

2.  Click **"Choose Image"** to select an image file.

3.  Click **"Encode & Save"** to embed the message and save the encoded image.

#### Decode a Message

1.  Click **"Choose Image to Decode"** to select an image with a hidden message.

2.  The decoded message will appear in the **"Decoded Message"** field.

#### Example

-   Input: `"Hello, this is a secret message!"`

-   Choose an image

-   Encode & save it

-   Decode to view the hidden message

* * * * *

🛠️ Convert to Executable (Windows)
-----------------------------------

### 1\. Install PyInstaller


```bash
`pip install pyinstaller`
```
### 2\. Create the Executable
```bash
pyinstaller --onefile --windowed main.py`
```
-   The `.exe` file will be available in the **`dist`** folder.


* * * * *

📄 License
----------

This project is licensed under the **MIT License**.\
See the `LICENSE` file for more details.

* * * * *

📝 Additional Notes
-------------------

-   A `secret.key` file is automatically generated for encryption/decryption. **Keep it safe**.

-   AES encryption is used to ensure **confidentiality** of hidden messages.
 format the above markdown 
