from diaries.AbstractDiary import AbstractDiary

class UchidaDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return """Github難しい"""
    def get_author(self):
        return "Uchida"