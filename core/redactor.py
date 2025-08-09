"""
Text redaction functionality for sensitive information
"""

import re
from config.settings import (
    SSN_PATTERNS, CREDIT_CARD_PATTERNS, ADDRESS_PATTERNS,
    OCR_CORRECTIONS, REDACTION_LABELS
)

class TextRedactor:
    def __init__(self):
        """Initialize the text redactor"""
        pass
    
    def clean_ocr_text(self, text):
        """
        Clean common OCR errors before processing
        
        Args:
            text (str): Raw OCR text
            
        Returns:
            str: Cleaned text
        """
        cleaned_text = text
        # Apply corrections conservatively
        # For now, we'll be conservative and not auto-correct
        # to avoid false corrections
        return cleaned_text
    
    def detect_and_redact_patterns(self, text):
        """
        More sophisticated pattern detection that handles OCR errors
        
        Args:
            text (str): Input text to redact
            
        Returns:
            str: Text with sensitive information redacted
        """
        redacted_text = text
        
        # SSN Detection with OCR error tolerance
        potential_ssns = re.finditer(r'\b\d{3}[-\s<>o]\d{2}[-\s<>o]\d{4}\b', text, re.IGNORECASE)
        for match in potential_ssns:
            redacted_text = redacted_text.replace(match.group(), REDACTION_LABELS["ssn"])
        
        # Credit card patterns
        potential_ccs = re.finditer(r'\b\d{4}[\s\-]\d{4}[\s\-]\d{3}[A-Za-z0-9][\s\-][A-Za-z0-9]\d{2,3}\b', text)
        for match in potential_ccs:
            redacted_text = redacted_text.replace(match.group(), REDACTION_LABELS["credit_card"])
        
        # Standard credit card patterns
        potential_ccs_standard = re.finditer(r'\b\d{4}[\s\-]\d{4}[\s\-]\d{4}[\s\-]\d{4}\b', text)
        for match in potential_ccs_standard:
            redacted_text = redacted_text.replace(match.group(), REDACTION_LABELS["credit_card"])
        
        # Address patterns - be more conservative
        address_matches = re.finditer(r'\b\d{1,4}\s+[A-Za-z]+\s+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|Blvd)\b', text, re.IGNORECASE)
        for match in address_matches:
            redacted_text = redacted_text.replace(match.group(), REDACTION_LABELS["address"])
        
        # ZIP codes with context check
        zip_matches = re.finditer(r'\b\d{5}(?:-\d{4})?\b', text)
        for match in zip_matches:
            context = text[max(0, match.start()-10):match.end()+10].lower()
            if any(indicator in context for indicator in ['zip', 'postal', 'address', 'mail']):
                redacted_text = redacted_text.replace(match.group(), REDACTION_LABELS["zip"])
        
        return redacted_text
    
    def redact_simple_patterns(self, text):
        """
        Very conservative redaction - only redacts very obvious patterns
        
        Args:
            text (str): Input text to redact
            
        Returns:
            str: Text with labeled sensitive information redacted
        """
        redacted_text = text
        
        # Only redact very clear SSN patterns
        redacted_text = re.sub(r'\bSSN:\s*\d{3}[-\s<>]\d{2}[-\s<>]\d{4}\b', 
                              REDACTION_LABELS["ssn"], redacted_text, flags=re.IGNORECASE)
        redacted_text = re.sub(r'\bSocial Security:\s*\d{3}[-\s<>]\d{2}[-\s<>]\d{4}\b', 
                              REDACTION_LABELS["ssn"], redacted_text, flags=re.IGNORECASE)
        
        # Only redact when explicitly labeled as credit card
        redacted_text = re.sub(r'\bCredit Card:\s*\d{4}[\s\-]\d{4}[\s\-]\d{4}[\s\-]\d{4}\b', 
                              REDACTION_LABELS["credit_card"], redacted_text, flags=re.IGNORECASE)
        redacted_text = re.sub(r'\bCard Number:\s*\d{4}[\s\-]\d{4}[\s\-]\d{4}[\s\-]\d{4}\b', 
                              REDACTION_LABELS["credit_card"], redacted_text, flags=re.IGNORECASE)
        
        # Only redact when explicitly labeled as address
        redacted_text = re.sub(r'\bAddress:\s*[^\n]+', 
                              REDACTION_LABELS["address"], redacted_text, flags=re.IGNORECASE)
        redacted_text = re.sub(r'\bZIP:\s*\d{5}(?:-\d{4})?\b', 
                              REDACTION_LABELS["zip"], redacted_text, flags=re.IGNORECASE)
        
        return redacted_text
    
    def redact_text(self, text, mode="conservative"):
        """
        Main redaction function with selectable modes
        
        Args:
            text (str): Input text to redact
            mode (str): "conservative" or "aggressive"
            
        Returns:
            str: Redacted text
        """
        # First clean the OCR text
        cleaned_text = self.clean_ocr_text(text)
        
        # Apply redaction based on mode
        if mode == "conservative":
            return self.redact_simple_patterns(cleaned_text)
        else:
            return self.detect_and_redact_patterns(cleaned_text)
    
    def get_redaction_stats(self, redacted_text):
        """
        Get statistics about redactions performed
        
        Args:
            redacted_text (str): Text after redaction
            
        Returns:
            dict: Statistics about redactions
        """
        stats = {
            "ssn_count": redacted_text.count(REDACTION_LABELS["ssn"]),
            "credit_card_count": redacted_text.count(REDACTION_LABELS["credit_card"]),
            "address_count": redacted_text.count(REDACTION_LABELS["address"]),
            "zip_count": redacted_text.count(REDACTION_LABELS["zip"]),
            "total_redactions": redacted_text.count('[REDACTED')
        }
        return stats