from diaries.DiarySample import DiarySample
from diaries.YutoDiary import YutoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    YutoDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()