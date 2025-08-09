"""
CSS styles for the Streamlit application
"""

CUSTOM_CSS = """
<style>
.main-header {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 2rem;
    text-align: center;
    color: white;
}

.feature-card {
    background: var(--background-color);
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #667eea;
    margin: 1rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    border: 1px solid var(--secondary-background-color);
    color: var(--text-color);
}

.stats-card {
    background: var(--background-color);
    padding: 1rem;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    border: 1px solid var(--secondary-background-color);
    color: var(--text-color);
}

.success-message {
    background: rgba(212, 237, 218, 0.2);
    color: var(--text-color);
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #28a745;
}

.footer {
    text-align: center;
    padding: 2rem;
    color: var(--text-color);
    border-top: 1px solid var(--secondary-background-color);
    margin-top: 3rem;
    font-size: 0.9rem;
    opacity: 0.8;
}

.redaction-preview {
    background: var(--secondary-background-color);
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid var(--secondary-background-color);
    max-height: 400px;
    overflow-y: auto;
    color: var(--text-color);
}

.upload-section {
    border: 2px dashed #667eea;
    border-radius: 10px;
    padding: 2rem;
    text-align: center;
    background: rgba(102, 126, 234, 0.05);
    margin: 1rem 0;
    color: var(--text-color);
}

/* Dark mode specific adjustments */
@media (prefers-color-scheme: dark) {
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .stats-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .upload-section {
        background: rgba(102, 126, 234, 0.1);
    }
    
    .redaction-preview {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
}

/* Streamlit dark theme adjustments */
[data-theme="dark"] .feature-card,
.stApp[data-theme="dark"] .feature-card {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: white !important;
}

[data-theme="dark"] .stats-card,
.stApp[data-theme="dark"] .stats-card {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: white !important;
}

[data-theme="dark"] .upload-section,
.stApp[data-theme="dark"] .upload-section {
    background: rgba(102, 126, 234, 0.1) !important;
    color: white !important;
}

[data-theme="dark"] .redaction-preview,
.stApp[data-theme="dark"] .redaction-preview {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: white !important;
}

[data-theme="dark"] .footer,
.stApp[data-theme="dark"] .footer {
    color: rgba(255, 255, 255, 0.8) !important;
    border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
}
</style>
"""