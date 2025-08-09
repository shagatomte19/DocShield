"""
Configuration settings for the Document Redaction System
"""

# Enhanced regex patterns that account for OCR errors
SSN_PATTERNS = [
    r"\b\d{3}[-\s<>]\d{2}[-\s<>]\d{4}\b",  # Handles OCR errors like < > instead of -
    r"\b\d{3}\s*\d{2}\s*\d{4}\b"  # More flexible spacing
]

CREDIT_CARD_PATTERNS = [
    r"\b\d{4}[\s\-]\d{4}[\s\-]\d{4}[\s\-]\d{4}\b",  # Standard 4-4-4-4 format
    r"\b\d{4}[\s\-]\d{4}[\s\-]\d{3}[A-Za-z0-9][\s\-][A-Za-z0-9]\d{3}\b"  # Handles OCR errors in last groups
]

# More precise address patterns to avoid false positives
ADDRESS_PATTERNS = [
    r"\b\d{1,5}\s+[A-Za-z]+\s+(?:[A-Za-z]+\s+)?(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|Blvd|Way|Court|Ct|Place|Pl|Circle|Cir)\b",
    r"\b\d{5}(?:[-\s]\d{4})?\b"  # ZIP codes only (5 digits or 5-4 format)
]

# OCR character corrections
OCR_CORRECTIONS = {
    '0': ['O', 'o', '°'],
    '1': ['l', 'I', '|'],
    '5': ['S', 's'],
    '6': ['G', 'b'],
    '8': ['B'],
    'S': ['5'],
    'O': ['0'],
    'I': ['1', 'l'],
    '<': ['-'],
    '>': ['-'],
}

# Streamlit app configuration
APP_CONFIG = {
    "page_title": "AI Document Redaction System",
    "page_icon": "🔒",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# File settings
SUPPORTED_FILE_TYPES = ["pdf"]
MAX_FILE_SIZE_MB = 50

# Redaction labels
REDACTION_LABELS = {
    "ssn": "[REDACTED SSN]",
    "credit_card": "[REDACTED CREDIT CARD]", 
    "address": "[REDACTED ADDRESS]",
    "zip": "[REDACTED ZIP]"
}