# 카드 버전 갱신: db/cardver.txt + c/*.html 이미지 주소의 ?v= 값을 새 버전으로
import re,glob,sys
v=sys.argv[1]
open('db/cardver.txt','w').write(v+"\n")
for f in glob.glob('c/*.html'):
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'\.png\?v=[0-9A-Za-z]+','.png?v='+v,s)
    open(f,'w',encoding='utf-8').write(s)
