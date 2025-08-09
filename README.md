# 🔒 DocShield

A sophisticated Streamlit application that automatically detects and redacts sensitive information from PDF documents using OCR and pattern recognition.

**Made by Enamul Hasan Shagato** ❤️

## 🌟 Features

- **OCR Text Extraction**: Advanced text extraction from PDF documents
- **Intelligent Redaction**: Automatically detects and redacts:
  - Social Security Numbers (SSN)
  - Credit Card Numbers
  - Street Addresses
  - ZIP Codes
- **Dual Processing Modes**: 
  - Conservative (labeled data only)
  - Aggressive (pattern matching)
- **Multiple Export Formats**: PDF and Word document outputs
- **Modern UI**: Responsive design with dark mode support
- **Real-time Statistics**: Processing metrics and redaction breakdown
- **Privacy-First**: All processing done locally

## 📁 Project Structure

```
document_redaction/
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── config/
│   ├── __init__.py
│   └── settings.py        # Configuration and patterns
├── core/
│   ├── __init__.py
│   ├── ocr_processor.py   # OCR functionality
│   ├── redactor.py        # Redaction logic
│   └── file_handler.py    # File operations
├── ui/
│   ├── __init__.py
│   ├── components.py      # UI components
│   └── styles.py          # CSS styling
└── utils/
    ├── __init__.py
    └── helpers.py         # Utility functions
```

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shagatomte19/docshield.git
   cd docshield
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run main.py
   ```

## 📖 Usage

1. **Upload a PDF**: Use the file uploader to select your PDF document
2. **Choose Redaction Mode**: 
   - **Conservative**: Only redacts explicitly labeled data
   - **Aggressive**: Uses pattern matching for broader detection
3. **Process Document**: Click the "Process Document" button
4. **Review Results**: View redacted text and statistics
5. **Download Files**: Export as PDF or Word document

## 🔧 Configuration

Modify `config/settings.py` to customize:
- Regex patterns for detection
- Redaction labels
- File size limits
- OCR settings

## 🎨 Customization

### Adding New Patterns
Add new regex patterns in `config/settings.py`:

```python
NEW_PATTERNS = [
    r"new-regex-pattern-here"
]
```

### UI Modifications
Update styles in `ui/styles.py` or add new components in `ui/components.py`.

### Processing Logic
Extend redaction logic in `core/redactor.py` for new sensitive data types.

## 📊 Architecture

### Core Components

- **OCRProcessor**: Handles PDF to text conversion using EasyOCR
- **TextRedactor**: Implements redaction logic with multiple strategies
- **FileHandler**: Manages PDF and Word export functionality
- **UIComponents**: Modular UI components for Streamlit interface

### Processing Pipeline

1. **PDF Upload** → **OCR Processing** → **Text Extraction**
2. **Pattern Detection** → **Redaction** → **Statistics Generation**
3. **File Export** → **Download** → **User Interface Updates**

## 🛡️ Security & Privacy

- **Local Processing**: All data processing happens locally
- **No Data Storage**: Documents are not stored permanently
- **Temporary Files**: Output files are created in temporary directories
- **Privacy-First**: No external API calls for sensitive data processing

## 📝 Dependencies

- **Streamlit**: Web application framework
- **EasyOCR**: OCR text extraction
- **PyMuPDF**: PDF processing
- **FPDF2**: PDF generation
- **python-docx**: Word document creation
- **PyTorch**: ML backend for OCR

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📋 Roadmap

- [ ] Add support for more file formats (DOCX, images)
- [ ] Implement custom redaction patterns via UI
- [ ] Add batch processing capabilities
- [ ] Enhance OCR accuracy with preprocessing
- [ ] Add redaction confidence scores
- [ ] Implement audit logging

## 🐛 Known Issues

- OCR quality depends on PDF text clarity
- Complex layouts may affect accuracy
- Large files may require processing time
- Handwritten text detection is limited

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Enamul Hasan Shagato**
- AI/ML Engineer
- [GitHub](https://github.com/shagatomte19) | [LinkedIn](https://linkedin.com/in/shagatomte19)

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

*Made with ❤️ using Python and Streamlit*
