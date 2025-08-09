"""
Configuration package for Document Redaction System
"""

from .settings import (
    SSN_PATTERNS,
    CREDIT_CARD_PATTERNS,
    ADDRESS_PATTERNS,
    OCR_CORRECTIONS,
    APP_CONFIG,
    SUPPORTED_FILE_TYPES,
    MAX_FILE_SIZE_MB,
    REDACTION_LABELS
)

__all__ = [
    'SSN_PATTERNS',
    'CREDIT_CARD_PATTERNS',
    'ADDRESS_PATTERNS',
    'OCR_CORRECTIONS',
    'APP_CONFIG',
    'SUPPORTED_FILE_TYPES',
    'MAX_FILE_SIZE_MB',
    'REDACTION_LABELS'
]