# inbox/ 에 올린 카드 이미지를 정식 파일명으로 옮김
#  - 직업가이드 세션 출력 이름 그대로 OK: 01_전사.png, 21_듀얼블레이드.png ...
#  - 앞 번호(01~21)로 직업을 찾아서 01_warrior.png 처럼 덮어씀
#  - 시즌2 룬 매커니즘 이미지(파일명에 '룬' 또는 'season2') → info/season2.png
import os, re, shutil, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
names = {f[:2]: f for f in os.listdir(ROOT) if re.match(r"^\d\d_[a-z]+\.png$", f)}
moved = []
for p in sorted(glob.glob(os.path.join(ROOT, "inbox", "**", "*.png"), recursive=True)):
    b = os.path.basename(p)
    m = re.match(r"^(\d\d)_", b)
    if m and m.group(1) in names:
        dst = os.path.join(ROOT, names[m.group(1)])
    elif "룬" in b or "season2" in b.lower():
        dst = os.path.join(ROOT, "info", "season2.png")
    else:
        print("건너뜀(이름 규칙 밖):", b); continue
    shutil.move(p, dst); moved.append(b + " → " + os.path.relpath(dst, ROOT))
for p in glob.glob(os.path.join(ROOT, "inbox", "**", "*.txt"), recursive=True):
    if os.path.basename(p) == "classsum.txt":
        shutil.move(p, os.path.join(ROOT, "db", "classsum.txt")); moved.append("classsum.txt → db/")
print("\n".join(moved) or "inbox 비어 있음")
