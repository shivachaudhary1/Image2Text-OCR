# 📸 Image2Text

**An AI-powered OCR web application that extracts printed text from images, with experimental support for handwritten content. Supports Hindi and English languages.**

[![Live Demo](https://img.shields.io/badge/Live_Demo-HuggingFace-FF4B4B?style=for-the-badge&logo=huggingface)](https://usernameisfound01-image2text-ocr.hf.space/?__theme=dark)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/shivachaudhary1/Image2Text-OCR)

Built with EasyOCR, NumPy, and Gradio.
---

## ✨ Features

- 📄 **Printed Text Extraction** - Extract text from documents, invoices, and screenshots
- 🌐 **Multi-Language** - Supports Hindi and English
- ⚡ **Real-Time Processing** - Instant text extraction with processing time display
- 🖥️ **Simple Web Interface** - Upload images via file or webcam
---

## 🚀 Live Demo

**Option 1:** Try the hosted app on [HuggingFace](https://usernameisfound01-image2text-ocr.hf.space/?__theme=dark)

> **Note:** This demo is hosted on Hugging Face Spaces with free-tier resources.

* The app may go into sleep mode after inactivity. When opened again, it may take a few moments to wake up and initialize before becoming available.


**Option 2:** Run locally in 3 commands:

```bash
git clone https://github.com/shivachaudhary1/Image2Text-OCR.git
cd Image2Text
pip install -r requirements.txt
python app.py
```

---

![App Screenshot](screenshot.png)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| EasyOCR | OCR Engine (Text Recognition) |
| Gradio | Web Interface |
| NumPy | Numerical Operations |
| Pillow | Image Handling |

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

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

<div align="center">

<h2>
  <span style="
    background: linear-gradient(90deg, #2563eb, #9333ea);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
  ">
    Shiva Chaudhary
  </span>
</h2>

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat-square&logo=github)](https://github.com/shivachaudhary1)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/shiva-chaudhary-614578410)

</div>

---

## Built With

- [EasyOCR](https://github.com/JaidedAI/EasyOCR) — Amazing OCR library
- [Gradio](https://github.com/gradio-app/gradio) — Web interface framework
- [NumPy](https://github.com/numpy/numpy) — Numerical operations and array handling
- [Pillow](https://github.com/python-pillow/Pillow) — Image loading and processing

---
