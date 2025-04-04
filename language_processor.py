from langdetect import detect

class LanguageProcessor:
    def __init__(self):
        self.supported_languages = {
            "en": "English",
            "es": "Spanish",
            "fr": "French",
            "de": "German",
            "it": "Italian",
            "ja": "Japanese"
        }
    
    def detect_language(self, text: str) -> str:
        try:
            return detect(text)
        except:
            return "unknown"
    
    def is_supported_language(self, language_code: str) -> bool:
        return language_code in self.supported_languages