from diaries.DiarySample import DiarySample
from diaries.YutoDiary import YutoDiary
from diaries.UchidaDiary import UchidaDiary
<<<<<<< HEAD
from diaries.okazakiDiary import okazakiDiary
=======
from diaries.taniokaDiary import taniokaDiary

>>>>>>> 8b0f72de0d0087fea39421064d2b0278dfb634a9
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    YutoDiary(),
    UchidaDiary(),
  taniokaDiary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()