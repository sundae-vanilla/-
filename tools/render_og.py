import json,html
from playwright.sync_api import sync_playwright
C={"전사":"#2f6f73","궁수":"#4d7a35","마법사":"#5b5fa3","힐러":"#b06a2a","음유시인":"#a8546f","도적":"#4b5563"}
data=[l.rstrip('\n').split('\t') for l in open('db/classsum.txt',encoding='utf-8') if l.strip()]
def page(d):
    fn,name,line,acc,wep,emb,mod,sg,season,stat,core,cyc=d; c=C[line]; e=html.escape
    row=lambda k,v:f'<div class="r"><b>{e(k)}</b><span>{e(v)}</span></div>'
    return f'''<html><head><style>
body{{margin:0;width:1200px;height:630px;font-family:'Noto Sans CJK KR','Noto Sans KR',sans-serif;background:#f3f4f6}}
.w{{box-sizing:border-box;margin:18px;width:1164px;height:594px;background:#fff;border-radius:22px;padding:30px 40px;border-top:10px solid {c}}}
.h{{display:flex;align-items:baseline;justify-content:space-between;border-bottom:3px solid {c};padding-bottom:10px}}
.h h1{{margin:0;font-size:66px;color:{c};font-weight:900;letter-spacing:-2px}}
.h small{{font-size:22px;color:#6b7280;text-align:right}}
.core{{margin:16px 0 10px;font-size:27px;font-weight:700;color:#111}}
.r{{display:flex;font-size:25px;padding:8px 0;border-bottom:1px dashed #e5e7eb}}
.r b{{width:170px;color:{c};flex:none}} .r span{{color:#1f2937}}
</style></head><body><div class="w">
<div class="h"><h1>{e(name)}</h1><small>{e(line)} 계열 · 세팅 카드<br>룬 채용률 2026.11.16 기준</small></div>
<div class="core">💡 {e(core)}</div>
{row("장신구",acc)}{row("무기·엠블럼",wep+" · "+emb)}{row("개조·세공",mod+"  |  "+sg)}{row("시즌 스탯",season)}{row("스탯 추천",stat)}{row("딜사이클",cyc)}
</div></body></html>'''
with sync_playwright() as p:
    b=p.chromium.launch(**({"executable_path":"/usr/bin/google-chrome"} if __import__("os").path.exists("/usr/bin/google-chrome") else {}))
    pg=b.new_page(viewport={"width":1200,"height":630})
    for d in data:
        pg.set_content(page(d)); pg.wait_for_timeout(150)
        pg.screenshot(path=f"og/{d[0]}_og.png")
    b.close()
print("ok")
