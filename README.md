# 📸 Image2Text

**An AI-powered OCR web application that extracts printed text from images, with experimental support for handwritten content. Supports Hindi and English languages.**

[![Live Demo](https://img.shields.io/badge/Live_Demo-HuggingFace-FF4B4B?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/yourusername/Image2Text)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/yourusername/Image2Text)

Built with EasyOCR, NumPy, and Gradio.
---

## ✨ Features

- 📄 **Printed Text Extraction** - Extract text from documents, invoices, and screenshots
- 🌐 **Multi-Language** - Supports Hindi (हिंदी) and English
- ⚡ **Real-Time Processing** - Instant text extraction with processing time display
- 🖥️ **Simple Web Interface** - Upload images via file or webcam
---

## 🚀 Live Demo

Try it now: [Image2Text on HuggingFace](https://huggingface.co/spaces/yourusername/Image2Text)

![App Screenshot](screenshot.png)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **EasyOCR** | OCR Engine (Text Recognition) |
| **OpenCV** | Image Processing |
| **Gradio** | Web Interface |
| **NumPy** | Numerical Operations |
| **Pillow** | Image Handling |

---
## 📦 Installation

### Prerequisites

Before installing the project, ensure you have the following:

- **Python 3.8 or higher**
- **pip package manager**

### Installation Steps

Follow these steps to set up the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Image2Text.git

# Navigate to the project directory
cd Image2Text

# 2. Install required dependencies
pip install -r requirements.txt

# 3. Launch the application
python app.py
````

Once the application starts, open your browser and visit:

```
http://127.0.0.1:7860
```

---

## Usage

Using **Image2Text** is simple:

### 1. Upload Image

* Upload an image file or capture one using your webcam.

### 2. Extract Text

* The application automatically detects and extracts text from the image.

### 3. Copy Results

* Use the copy button to quickly copy the extracted text.

### 💡 Tips for Best Results

For improved OCR accuracy:

* Use clear and high-resolution images.
* Avoid shadows, blur, and image glare.

---

## 📁 Project Structure

```
Image2Text/
│
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── README.md           # Documentation
└── examples/           # Sample images for testing
```

---

## ⚠️ Limitations

Although Image2Text provides accurate OCR results, some limitations may occur:

* OCR accuracy may decrease with blurry or low-quality images.
* Complex layouts and multiple text regions may produce inconsistent results.
* Handwritten text recognition depends on handwriting clarity.
* Always verify critical extracted information manually.

---

## 🤝 Contributing

Contributions are highly appreciated!

To contribute:

1. Fork this repository.
2. Create a new feature branch.
3. Make your changes.
4. Submit a pull request.

---

📄 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
Shiva Chaudhary

GitHub: @shivachaudhary1

LinkedIn: Your Profile

---

##🙏 Credits

- [EasyOCR](https://github.com/JaidedAI/EasyOCR) — Amazing OCR library
- [Gradio](https://github.com/gradio-app/gradio) — Web interface framework
- [NumPy](https://github.com/numpy/numpy) — Numerical operations and array handling
- [Pillow](https://github.com/python-pillow/Pillow) — Image loading and processing

---

<p align="center">
  Made with ❤️ 
</p>
