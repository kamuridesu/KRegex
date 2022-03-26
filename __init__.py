try:
    from .main import RegexProcessor
except Exception:
    from main import RegexProcessor


__all__ = [RegexProcessor]