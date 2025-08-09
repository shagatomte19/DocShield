"""
OCR processing functionality for PDF documents
"""

import easyocr
import fitz  # PyMuPDF for PDF handling
import streamlit as st

class OCRProcessor:
    def __init__(self):
        """Initialize EasyOCR reader"""
        self.reader = easyocr.Reader(['en'])  # English language, CPU mode
    
    def pdf_to_images(self, pdf_file):
        """
        Convert PDF pages to images
        
        Args:
            pdf_file: Streamlit file upload object
            
        Returns:
            list: List of image bytes
        """
        try:
            doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
            images = []
            
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                img = pix.tobytes("ppm")
                images.append(img)
            
            doc.close()
            return images
        except Exception as e:
            st.error(f"Error converting PDF to images: {str(e)}")
            return []
    
    def extract_text_from_images(self, images):
        """
        Extract text from images using EasyOCR
        
        Args:
            images: List of image bytes
            
        Returns:
            str: Extracted text from all images
        """
        try:
            results = []
            
            for img in images:
                result = self.reader.readtext(img)
                # Extract text (ignoring bounding box and confidence score)
                extracted_text = " ".join([text[1] for text in result])
                results.append(extracted_text)
            
            return "\n".join(results)
        except Exception as e:
            st.error(f"Error extracting text from images: {str(e)}")
            return ""
    
    def process_pdf(self, pdf_file):
        """
        Complete PDF processing pipeline
        
        Args:
            pdf_file: Streamlit file upload object
            
        Returns:
            str: Extracted text or None if failed
        """
        try:
            images = self.pdf_to_images(pdf_file)
            if not images:
                return None
                
            extracted_text = self.extract_text_from_images(images)
            
            if not extracted_text.strip():
                return None
                
            return extracted_text
        except Exception as e:
            st.error(f"Error processing PDF: {str(e)}")
            return None