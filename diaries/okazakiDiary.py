from diaries.AbstractDiary import AbstractDiary

class okazakiDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-01"
    def get_summary(self):
        return "なにもない一日だった"
    def get_author(self):
        return "Sample"