# QR Code Generator (Django)

A simple and stylish **QR Code Generator** built with Django and Bootstrap. This project allows users to generate QR codes based on a given URL and download them directly as PNG images.

---

## 🚀 Features

* Generate QR codes from any URL.
* Customize QR code colors (foreground and background).
* Real-time preview before downloading.
* Download generated QR codes as PNG files.
* Clean and responsive landing page (index.html).

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # for Linux/macOS
venv\Scripts\activate      # for Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Django server

```bash
python manage.py runserver
```

Then open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧱 Project Structure

```
core/
 ├── templates/
 │    └── index.html      # Landing page (QR generator UI)
 ├── views.py             # Handles rendering and logic
 ├── urls.py              # URL routing

manage.py
requirements.txt
README.md
```

---

## 📦 Example Usage

1. Enter your target URL in the input field.
2. Choose your QR code colors (foreground and background).
3. Click **Generate QR Code**.
4. Download your QR code by clicking the **Download** button.

---

## 🧹 .gitignore Example

```gitignore
# Python
__pycache__/
*.py[cod]
*.sqlite3

# Virtual environment
venv/
.env/

# Django specific
/static/
/media/

# IDE / Editor
.vscode/
.idea/
*.swp

# OS Files
.DS_Store
Thumbs.db
```

---

## 💡 Notes

* This project uses [qrcode.js](https://github.com/soldair/node-qrcode) via CDN for frontend QR generation.
* Bootstrap 5 is used for a modern and clean UI.
* Works perfectly for small projects, landing pages, and quick QR code creation.

---

## 🧑‍💻 Author

**Your Name**
📧 [your.email@example.com](mailto:your.email@example.com)
🌐 [yourwebsite.com](https://yourwebsite.com)

---

### 📜 License

This project is licensed under the MIT License – feel free to use and modify it as you wish.
