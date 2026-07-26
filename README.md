# 📸 Image2Text

An AI-powered OCR web application that extracts **printed and handwritten text** from images, supporting **Hindi and English** languages. Built with EasyOCR, OpenCV, and Gradio.

[![Live Demo](https://img.shields.io/badge/Live_Demo-HuggingFace-FF4B4B?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/yourusername/Image2Text)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/yourusername/Image2Text)

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
- Python 3.8 or higher
- pip package manager

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Image2Text.git
cd Image2Text

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python app.py
The app will open at http://127.0.0.1:7860

🎯 Usage
Upload Image - Click upload or use webcam

View Results - Extracted text appears instantly

Copy Text - Use the copy button to copy extracted text

Best Results Tips:
Use clear, well-lit images

Avoid shadows and glare

Hold camera steady

Minimum 300 DPI recommended

📁 Project Structure
text
Image2Text/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── README.md           # Documentation
└── examples/           # Sample images for testing
⚠️ Limitations
OCR is not 100% accurate, especially on blurry or low-quality images

Complex layouts may produce inconsistent results

Handwritten text accuracy depends on handwriting clarity

Always verify important extracted text manually

Future Improvements
□ Add more languages (Gujarati, Marathi, etc.)
□ PDF support
□ Batch processing
□ Image preprocessing options
□ Confidence score per word
□ Text translation feature
🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repository

Create a feature branch

Submit a pull request

📄 License
This project is licensed under the MIT License.

👨‍💻 Author
Your Name

GitHub: @yourusername

LinkedIn: Your Profile

🙏 Credits
EasyOCR - Amazing OCR library

Gradio - Simple ML web interfaces

OpenCV - Computer vision tools

<p align="center"> Made with ❤️ for the community </p> ```
