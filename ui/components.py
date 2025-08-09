"""
UI components for the Streamlit application
"""

import streamlit as st
import os
from ui.styles import CUSTOM_CSS

class UIComponents:
    def __init__(self):
        """Initialize UI components"""
        pass
    
    def render_page_config(self):
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title="DocShield",
            page_icon="🔒",
            layout="wide",
            initial_sidebar_state="expanded"
        )
    
    def render_custom_css(self):
        """Apply custom CSS styles"""
        st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    def render_header(self):
        """Render the main header"""
        st.markdown("""
        <div class="main-header">
            <h1>🔒 AI-Powered Document Redaction System</h1>
            <p>Securely redact sensitive information from your PDF documents</p>
        </div>
        """, unsafe_allow_html=True)
    
    def render_sidebar(self):
        """
        Render sidebar with settings and info
        
        Returns:
            tuple: (redaction_mode, stats_placeholder)
        """
        with st.sidebar:
            st.markdown("### 🎛️ Settings & Info")
            
            # Redaction mode selection
            st.markdown("**Redaction Mode:**")
            redaction_mode = st.radio(
                "",
                ["Conservative (Labeled data only)", "Aggressive (Pattern matching)"],
                help="Conservative mode only redacts explicitly labeled sensitive data. Aggressive mode uses pattern matching to find unlabeled sensitive information."
            )
            
            st.markdown("---")
            
            # Features info
            st.markdown("### ✨ Features")
            st.markdown("""
            - 🔍 **OCR Text Extraction**
            - 🏛️ **Social Security Numbers**
            - 💳 **Credit Card Details**
            - 🏠 **Address Information**
            - 📄 **PDF Export**
            - 📝 **Word Export**
            """)
            
            st.markdown("---")
            
            # Statistics placeholder
            st.markdown("### 📊 Statistics")
            stats_placeholder = st.empty()
            
            st.markdown("---")
            
            # Security notice
            st.markdown("### 🛡️ Security Notice")
            st.info("Your documents are processed locally and are not stored or transmitted to external servers.")
        
        return redaction_mode, stats_placeholder
    
    def render_upload_section(self):
        """
        Render file upload section
        
        Returns:
            uploaded_file: Streamlit file uploader object
        """
        st.markdown("""
        <div class="upload-section">
            <h3>📄 Upload Your Document</h3>
            <p>Select a PDF document to redact sensitive information</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_pdf = st.file_uploader(
            "",
            type="pdf",
            help="Upload a PDF document containing sensitive information"
        )
        
        return uploaded_pdf
    
    def render_file_info(self, uploaded_file):
        """Render information about uploaded file"""
        if uploaded_file is not None:
            file_size = len(uploaded_file.getvalue()) / 1024  # KB
            st.success(f"✅ File uploaded: **{uploaded_file.name}** ({file_size:.1f} KB)")
    
    def render_processing_options(self):
        """
        Render processing options
        
        Returns:
            tuple: (show_original, auto_download)
        """
        with st.expander("🔧 Processing Options", expanded=True):
            col_a, col_b = st.columns(2)
            with col_a:
                show_original = st.checkbox("Show original text", value=False)
            with col_b:
                auto_download = st.checkbox("Auto-generate downloads", value=True)
        
        return show_original, auto_download
    
    def render_progress_section(self):
        """
        Render progress indicators
        
        Returns:
            tuple: (progress_bar, status_text)
        """
        progress_bar = st.progress(0)
        status_text = st.empty()
        return progress_bar, status_text
    
    def update_progress(self, progress_bar, status_text, progress, message):
        """Update progress indicators"""
        progress_bar.progress(progress)
        status_text.text(message)
    
    def render_success_message(self):
        """Render success message"""
        st.markdown("""
        <div class="success-message">
            <strong>🎉 Processing completed successfully!</strong><br>
            Your document has been processed and sensitive information has been redacted.
        </div>
        """, unsafe_allow_html=True)
    
    def render_statistics(self, stats_placeholder, stats):
        """Render statistics in sidebar"""
        stats_placeholder.markdown(f"""
        <div class="stats-card">
            <strong>{stats['total_redactions']}</strong><br>
            <small>Items Redacted</small>
        </div>
        <div class="stats-card" style="margin-top: 0.5rem;">
            <strong>{len(str(stats))}</strong><br>
            <small>Stats Generated</small>
        </div>
        """, unsafe_allow_html=True)
    
    def render_results_tabs(self, redacted_text, stats, redaction_mode, show_original):
        """Render results in tabbed interface"""
        st.markdown("### 📋 Results")
        
        # Tabs for different views
        tab1, tab2, tab3 = st.tabs(["📄 Redacted Text", "📊 Summary", "⚙️ Settings"])
        
        with tab1:
            if show_original:
                col_orig, col_red = st.columns(2)
                with col_orig:
                    st.markdown("**Original Text (Preview):**")
                    st.text_area("", "Original text would be shown here...", height=300, disabled=True)
                with col_red:
                    st.markdown("**Redacted Text:**")
                    st.text_area("", redacted_text, height=300, disabled=True)
            else:
                st.markdown("**Redacted Text:**")
                st.markdown(f'<div class="redaction-preview">{redacted_text}</div>', unsafe_allow_html=True)
        
        with tab2:
            self.render_summary_metrics(stats)
        
        with tab3:
            st.markdown("**Current Settings:**")
            st.write(f"- Redaction Mode: {redaction_mode}")
            st.write(f"- Show Original: {show_original}")
    
    def render_summary_metrics(self, stats):
        """Render summary metrics and charts"""
        col_metric1, col_metric2, col_metric3, col_metric4 = st.columns(4)
        
        with col_metric1:
            st.metric("SSN Redacted", stats['ssn_count'])
        
        with col_metric2:
            st.metric("Credit Cards", stats['credit_card_count'])
        
        with col_metric3:
            st.metric("Addresses", stats['address_count'])
        
        with col_metric4:
            st.metric("Total Redactions", stats['total_redactions'])
        
        # Redaction breakdown chart
        if stats['total_redactions'] > 0:
            st.markdown("### 📊 Redaction Breakdown")
            chart_data = {
                "Type": ["SSN", "Credit Cards", "Addresses", "ZIP Codes"],
                "Count": [stats['ssn_count'], stats['credit_card_count'], 
                         stats['address_count'], stats['zip_count']]
            }
            st.bar_chart(chart_data, x="Type", y="Count")
    
    def render_download_section(self, output_pdf, output_word):
        """Render download buttons"""
        st.markdown("### 💾 Download Files")
        
        download_col1, download_col2 = st.columns(2)
        
        with download_col1:
            if output_pdf and os.path.exists(output_pdf):
                with open(output_pdf, "rb") as f:
                    st.download_button(
                        "📄 Download Redacted PDF",
                        f.read(),
                        file_name="redacted_document.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
        
        with download_col2:
            if output_word and os.path.exists(output_word):
                with open(output_word, "rb") as f:
                    st.download_button(
                        "📝 Download Word Document",
                        f.read(),
                        file_name="redacted_document.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        use_container_width=True
                    )
    
    def render_tips_section(self):
        """Render tips and information cards"""
        st.markdown("### 💡 Tips")
        
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 Best Practices</h4>
            <ul>
                <li>Ensure PDF text is selectable</li>
                <li>Review redacted output carefully</li>
                <li>Use conservative mode for higher accuracy</li>
                <li>Check download files before sharing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>🔍 What Gets Redacted</h4>
            <ul>
                <li><strong>SSN:</strong> XXX-XX-XXXX format</li>
                <li><strong>Credit Cards:</strong> 16-digit numbers</li>
                <li><strong>Addresses:</strong> Street addresses</li>
                <li><strong>ZIP Codes:</strong> 5 or 9-digit codes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>⚠️ Limitations</h4>
            <ul>
                <li>OCR quality affects accuracy in Streanlit(CPU Only)</li>
                <li>Handwritten text may not be detected</li>
                <li>Complex layouts may cause issues</li>
                <li>Always manual review recommended</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    def render_footer(self):
        """Render footer with credits"""
        st.markdown("""
        <div class="footer">
            <hr>
            <p>🚀 Made with ❤️ by <strong>Enamul Hasan Shagato</strong></p>
            <p><small>AI-Powered Document Redaction System | Protecting Your Privacy</small></p>
        </div>
        """, unsafe_allow_html=True)