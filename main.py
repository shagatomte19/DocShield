"""
Main Streamlit application for AI-Powered Document Redaction System

Author: Enamul Hasan Shagato
"""

import streamlit as st
import sys
import os

# Add project root to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.components import UIComponents
from utils.helpers import DocumentProcessor, validate_file_upload, get_redaction_mode_description

def main():
    """Main application function"""
    
    # Initialize components
    ui = UIComponents()
    processor = DocumentProcessor()
    
    # Configure page
    ui.render_page_config()
    ui.render_custom_css()
    
    # Render header
    ui.render_header()
    
    # Render sidebar and get settings
    redaction_mode, stats_placeholder = ui.render_sidebar()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # File upload section
        uploaded_pdf = ui.render_upload_section()
        
        if uploaded_pdf is not None:
            # Validate file
            if not validate_file_upload(uploaded_pdf):
                return
            
            # Display file info
            ui.render_file_info(uploaded_pdf)
            
            # Processing options
            show_original, auto_download = ui.render_processing_options()
            
            # Process button
            if st.button("🚀 Process Document", type="primary", use_container_width=True):
                
                # Progress indicators
                progress_bar, status_text = ui.render_progress_section()
                
                # Processing steps with progress updates
                ui.update_progress(progress_bar, status_text, 10, "🔄 Initializing OCR engine...")
                ui.update_progress(progress_bar, status_text, 30, "📖 Extracting text from PDF...")
                
                # Process the document
                result = processor.process_document(uploaded_pdf, redaction_mode)
                redacted_text, output_pdf, output_word, stats = result
                
                ui.update_progress(progress_bar, status_text, 70, "🔍 Applying redaction patterns...")
                ui.update_progress(progress_bar, status_text, 90, "📄 Generating output files...")
                ui.update_progress(progress_bar, status_text, 100, "✅ Processing complete!")
                
                # Handle results
                if redacted_text is None:
                    st.error("❌ No text could be extracted. Please ensure the document contains readable text.")
                else:
                    # Success message
                    ui.render_success_message()
                    
                    # Update statistics in sidebar
                    if stats:
                        ui.render_statistics(stats_placeholder, stats)
                    
                    # Display results in tabs
                    ui.render_results_tabs(redacted_text, stats, redaction_mode, show_original)
                    
                    # Download section
                    ui.render_download_section(output_pdf, output_word)
    
    # Right column - Tips and information
    with col2:
        ui.render_tips_section()
    
    # Footer
    ui.render_footer()

if __name__ == "__main__":
    main()