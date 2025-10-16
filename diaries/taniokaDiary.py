from diaries.AbstractDiary import AbstractDiary

class taniokaDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "今日はオブジェクト指向プログラミング演習２のグループワーク演習だった。"
    def get_author(self):
        return "tanioka"