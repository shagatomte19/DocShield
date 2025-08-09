"""
File handling operations for PDF and Word documents
"""

import tempfile
from fpdf import FPDF
from docx import Document
import streamlit as st

class FileHandler:
    def __init__(self):
        """Initialize file handler"""
        pass
    
    def export_to_pdf(self, redacted_text):
        """
        Export redacted text to PDF
        
        Args:
            redacted_text (str): Text to export
            
        Returns:
            str: Path to generated PDF file
        """
        try:
            print(f"Redacted Text: {redacted_text[:100]}...") 
            
            # Create a temporary file for PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
                tmpfile.close()
                output_pdf_path = tmpfile.name

            # Create PDF
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Handle encoding issues
            try:
                pdf.multi_cell(0, 10, redacted_text.encode('latin-1', 'replace').decode('latin-1'))
            except:
                # Fallback for special characters
                cleaned_text = ''.join(char if ord(char) < 128 else '?' for char in redacted_text)
                pdf.multi_cell(0, 10, cleaned_text)

            # Save the PDF
            pdf.output(output_pdf_path)
            return output_pdf_path
            
        except Exception as e:
            st.error(f"Error creating PDF: {str(e)}")
            return None
    
    def export_to_word(self, redacted_text):
        """
        Export redacted text to Word document
        
        Args:
            redacted_text (str): Text to export
            
        Returns:
            str: Path to generated Word document
        """
        try:
            # Create a temporary file for Word
            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmpfile:
                tmpfile.close()
                output_word_path = tmpfile.name

            # Create Word document
            doc = Document()
            doc.add_paragraph(redacted_text)
            
            # Save the Word document
            doc.save(output_word_path)
            return output_word_path
            
        except Exception as e:
            st.error(f"Error creating Word document: {str(e)}")
            return None
    
    def create_output_files(self, redacted_text):
        """
        Create both PDF and Word output files
        
        Args:
            redacted_text (str): Text to export
            
        Returns:
            tuple: (pdf_path, word_path)
        """
        pdf_path = self.export_to_pdf(redacted_text)
        word_path = self.export_to_word(redacted_text)
        return pdf_path, word_path