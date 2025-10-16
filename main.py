from diaries.DiarySample import DiarySample
from diaries.taniokaDiary import taniokaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),taniokaDiary() ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()