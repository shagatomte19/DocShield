"""
Utility functions and helpers for the document redaction system
"""

import streamlit as st
from core.ocr_processor import OCRProcessor
from core.redactor import TextRedactor
from core.file_handler import FileHandler

class DocumentProcessor:
    """Main document processing orchestrator"""
    
    def __init__(self):
        self.ocr_processor = OCRProcessor()
        self.text_redactor = TextRedactor()
        self.file_handler = FileHandler()
    
    def process_document(self, pdf_file, redaction_mode="conservative"):
        """
        Complete document processing pipeline
        
        Args:
            pdf_file: Streamlit file upload object
            redaction_mode: "conservative" or "aggressive"
            
        Returns:
            tuple: (redacted_text, output_pdf, output_word, stats)
        """
        try:
            # Extract text from PDF
            extracted_text = self.ocr_processor.process_pdf(pdf_file)
            
            if not extracted_text or not extracted_text.strip():
                return None, None, None, None
            
            # Determine redaction mode
            mode = "conservative" if "Conservative" in redaction_mode else "aggressive"
            
            # Redact sensitive information
            redacted_text = self.text_redactor.redact_text(extracted_text, mode=mode)
            
            # Get redaction statistics
            stats = self.text_redactor.get_redaction_stats(redacted_text)
            
            # Create output files
            output_pdf, output_word = self.file_handler.create_output_files(redacted_text)
            
            return redacted_text, output_pdf, output_word, stats
            
        except Exception as e:
            st.error(f"Error processing document: {str(e)}")
            return None, None, None, None

def validate_file_upload(uploaded_file, max_size_mb=50):
    """
    Validate uploaded file
    
    Args:
        uploaded_file: Streamlit file upload object
        max_size_mb: Maximum file size in MB
        
    Returns:
        bool: True if valid, False otherwise
    """
    if uploaded_file is None:
        return False
    
    # Check file size
    file_size_mb = len(uploaded_file.getvalue()) / (1024 * 1024)
    if file_size_mb > max_size_mb:
        st.error(f"File size ({file_size_mb:.1f} MB) exceeds maximum allowed size ({max_size_mb} MB)")
        return False
    
    # Check file type
    if not uploaded_file.name.lower().endswith('.pdf'):
        st.error("Please upload a PDF file")
        return False
    
    return True

def format_file_size(size_bytes):
    """
    Format file size in human readable format
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        str: Formatted size string
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

def get_redaction_mode_description(mode):
    """
    Get description for redaction mode
    
    Args:
        mode: Redaction mode string
        
    Returns:
        str: Mode description
    """
    if "Conservative" in mode:
        return "Only redacts explicitly labeled sensitive data (SSN:, Credit Card:, Address:)"
    else:
        return "Uses pattern matching to detect unlabeled sensitive information"

def log_processing_step(step_name, details=""):
    """
    Log processing step (for debugging)
    
    Args:
        step_name: Name of the processing step
        details: Additional details
    """
    # For debugging purposes - can be extended to write to logs
    print(f"[PROCESSING] {step_name}: {details}")