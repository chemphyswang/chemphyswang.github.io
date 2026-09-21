import json, re, html
from pathlib import Path

# All paths are relative to this script's location (tools/)
TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent

SMALL = {'a','an','the','and','but','or','nor','for','so','yet','as','at','by','in','of','on','to','up','via','per','vs','v','p'}

def cap_word(w):
    if not w: return w
    if w[0].isalpha() and not w[0].isascii():  # 希腊字母等保持原样
        return w
    if re.match(r'^p[A-Z]', w):  # pK_a 类记号
        return w
    if re.match(r'^sp\d', w, re.I):  # sp3 杂化记号
        return w
    letters = [c for c in w if c.isalpha()]
    if letters and all(c.isupper() for c in letters) and len(letters) > 1:
        return w
    return w[0].upper() + w[1:]

SUB = str.maketrans('0123456789aeoxhklmnpst', '₀₁₂₃₄₅₆₇₈₉ₐₑₒₓₕₖₗₘₙₚₛₜ')
SUP = str.maketrans('0123456789+-=()n', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ')

def strip_markup(title):
    title = re.sub(r'<sub>(.*?)</sub>', lambda m: m.group(1).translate(SUB), title, flags=re.S)
    title = re.sub(r'<sup>(.*?)</sup>', lambda m: m.group(1).translate(SUP), title, flags=re.S)
    title = re.sub(r'</?[ib]>', '', title)
    title = re.sub(r'\s+', ' ', title).strip()
    title = re.sub(r' ([₀₁₂₃₄₅₆₇₈₉ₐₑₒₓₕₖₗₘₙₚₛₜ])', r'\1', title)
    title = re.sub(r'\bp ([A-Z])', r'p\1', title)
    return title

def titlecase(title):
    title = strip_markup(title).strip().strip('*').strip()
    out = []
    for tok in title.split(' '):
        if not tok:
            out.append(('', False)); continue
        core = re.sub(r'^[^\w]+|[^\w]+$', '', tok)
        is_small = core.lower() in SMALL and len(core) <= 3
        parts = re.split(r'([\-\‐\‑\–\—])', tok)
        new_tok = ''.join(p if re.fullmatch(r'[-\‐\‑\–\—]', p or '-') else cap_word(p) for p in parts)
        out.append((new_tok, is_small))
    n = len(out)
    res = []
    for i, (tok, is_small) in enumerate(out):
        if not tok:
            res.append(tok); continue
        if is_small and 0 < i < n - 1 and tok[0].isascii():
            res.append(tok.lower())
        else:
            res.append(tok)
    return ' '.join(res)

TITLE_OVERRIDE = {
 '10.7536/PC211037': 'Aggregation-Induced Emission (聚集诱导发光)',
}

def esc(s):
    return html.escape(html.unescape(str(s)))

d = json.load(open(TOOLS / 'pubs_enriched.json'))
pubs = d['pubs']
pc_corr = d['pc_corr']
del pubs[30]  # dedupe stub (full record kept)
pubs[5]['year'] = 2026
pubs[14]['year'] = 2025

SPRINGER0 = json.load(open(TOOLS / 'springer0_corr.json'))
# keyed by DOI — verified via publisher page / PMC / OpenAlex
CORR = {
 '10.1007/s11426-025-3385-5': SPRINGER0,
 '10.1093/nsr/nwag394': ['Meng Zhou', 'Xuepeng Zhang', 'Tao Wang', 'Guoqing Zhang'],
 '10.31635/ccschem.025.202506170': ['Peng Sun', 'Tao Wang', 'Zhengxu Cai'],
 '10.1002/anie.8043102': ['Tao Wang', 'Guoqing Zhang'],
 '10.1021/acsnano.6c00162': ['Tao Wang', 'Xuepeng Zhang', 'Guoqing Zhang'],
 '10.1002/ADMA.202521092': ['Qingfeng Xu', 'Tao Wang', 'Dongyun Chen', 'Jianmei Lu'],
 '10.1038/s41467-025-66035-w': ['Peng Sun', 'Zhengxu Cai'],
 '10.1002/agt2.70172': ['Guoqing Zhang', 'Tao Wang'],
 '10.1016/J.CCR.2025.216629': ['Peng Sun', 'Zhengxu Cai'],
 '10.31635/ccschem.024.202404450': ['Manman Fang', 'Xiaogang Liu', 'Zhen Li'],
 '10.1039/D5CC04148A': ['Wenbo Dai', 'Peng Sun', 'Zhengxu Cai'],
 '10.1039/D5QM00602C': ['Zitong Liu', 'Zhengxu Cai', 'Peng Sun'],
 '10.1007/978-981-97-1574-9_168-1': ['Tao Wang'],
 '10.1021/ACS.CHEMREV.3C00755': ['Eli Zysman-Colman'],
 '10.1002/CPTC.202400315': ['Peng Sun', 'Li Zhao', 'Zhengxu Cai'],
 '10.31635/ccschem.024.202404623': ['Tao Wang', 'Eli Zysman-Colman'],
 '10.1038/s41467-024-51231-x': ['Dianming Sun', 'Eli Zysman-Colman'],
 '10.1002/ANIE.202401949': ['Xiaogang Liu'],
 '10.1021/JACS.4C01929': ['Chun-Sing Lee', 'Wenbo Bu', 'Xiaogang Liu'],
 '10.1002/anie.202309718': ['Eli Zysman-Colman'],
 '10.1063/1674-0068/cjcp2105086': ['Guoqing Zhang', 'Xue-peng Zhang'],
 '10.1002/ADOM.202300114': ['Eli Zysman-Colman'],
 '10.1002/anie.202218712': ['Xiaolong Zhang', 'Xuepeng Zhang', 'Guoqing Zhang'],
 '10.1016/J.XCRP.2022.101245': ['Tao Wang', 'Guoqing Zhang'],
 '10.1021/jacs.2c12320': ['Eli Zysman-Colman'],
 '10.1002/adpr.202200203': ['Eli Zysman-Colman'],
 '10.1002/anie.202206681': ['Eli Zysman-Colman'],
 '10.1002/anie.202206366': ['Guoqing Zhang', 'Tao Wang'],
 '10.1002/adom.202200099': ['Biao Chen', 'Xuepeng Zhang', 'Guoqing Zhang'],
 '10.1002/agt2.165': ['Xuepeng Zhang', 'Guoqing Zhang'],
 '10.1016/j.dyepig.2021.109505': ['Jun Jiang', 'Xuepeng Zhang', 'Guoqing Zhang'],
 '10.1021/acs.jpclett.1c00520': ['Tao Wang', 'Biao Chen', 'Guoqing Zhang'],
 '10.1038/s41467-021-21676-5': ['Xiang Sun', 'Guoqing Zhang'],
 '10.1039/d1tc04156h': ['Tao Wang', 'Xuepeng Zhang', 'Guoqing Zhang'],
 '10.1016/j.polymer.2020.123017': ['Kun-Peng Wang', 'Chenggen Qian', 'Xingyuan Zhang'],
 '10.1002/chem.201905865': ['Tao Wang', 'Guoqing Zhang'],
 '10.1021/acsami.0c13886': ['Hui Miao', 'Tao Wang', 'Guoqing Zhang'],
 '10.1039/D0CC04604C': ['Xiaolong Zhang', 'Yi Luo', 'Guoqing Zhang'],
 '10.1002/adma.201904273': ['Xuepeng Zhang', 'Xingyuan Zhang', 'Xiang Sun', 'Guoqing Zhang'],
 '10.1002/asia.201900423': ['Tao Wang', 'Xingyuan Zhang'],
 '10.1039/C9TC02266J': ['Xuepeng Zhang', 'Xingyuan Zhang', 'Xiang Sun', 'Guoqing Zhang'],
 '10.1039/C7QM00399D': ['Xingyuan Zhang', 'Peifeng Su', 'Guoqing Zhang'],
 '10.1039/C7PY01995E': ['Xingyuan Zhang'],
 '10.3390/MA10111247': ['Xingyuan Zhang'],
 '10.1021/acs.jpca.7b08268': ['Xingyuan Zhang', 'Chuanyao Zhou', 'Guoqing Zhang'],
 '10.3390/polym9090411': ['Xingyuan Zhang'],
 '10.1021/ACS.JPCA.7B01711': ['Jun Jiang', 'Xingyuan Zhang', 'Guoqing Zhang'],
 '10.1002/ANIE.201601252': ['Xuepeng Zhang', 'Guoqing Zhang'],
 '10.1016/j.microc.2026.119166': [],  # UNVERIFIED
 '10.1002/adom.202501022': ['Xiaogang Liu'],
 '10.1016/j.dyepig.2025.113080': ['Bin Tong', 'Yuping Dong'],
 '10.7536/PC211037': pc_corr,
}

COFIRST = {
 '10.1093/nsr/nwag394': ['Hongping Liu', 'Dingcheng Zhou', 'Wei Zhang'],
 '10.31635/ccschem.025.202506170': ['Gengchen Li', 'Wenbo Dai'],
 '10.1038/s41467-025-66035-w': ['Yue Ren', 'Yongfeng Zhang'],
 '10.1016/J.CCR.2025.216629': ['Wenya Yan', 'Peixuan Dong'],
 '10.1016/j.dyepig.2025.113080': ['Jian Wang', 'Xiaoling Pan'],
 '10.1039/D5CC04148A': ['Jianhui Yang', 'Lutong Zhang'],
 '10.1039/D5QM00602C': ['Bolun Huang', 'Yongfeng Zhang'],
 '10.1038/s41467-024-51231-x': ['Changfeng Si', 'Tao Wang'],
 '10.1002/anie.202309718': ['Changfeng Si', 'Tao Wang'],
}

UNVERIFIED = {'10.1016/j.microc.2026.119166'}

def norm(s):
    s = s.replace('\u2010','-').replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
    return re.sub(r'[\s\.]+', ' ', s).strip().lower()

def norm_key(s):
    # hyphen/space-insensitive key, plus reversed two-part fallback for CJK name order
    base = norm(s).replace('-', '').replace(' ', '')
    parts = norm(s).replace('-', ' ').split()
    variants = {base}
    if len(parts) == 2:
        variants.add(parts[1] + parts[0])
    return variants

TIER0 = {'national science review', 'advanced materials',
         'angewandte chemie international edition',
         'journal of the american chemical society',
         'ccs chemistry', 'nature communications'}

def sort_key(p):
    dt = p.get('date') or [p['year'], 1, 1]
    m = dt[1] if len(dt) > 1 and dt[0] == p['year'] else 1
    dd = dt[2] if len(dt) > 2 and dt[0] == p['year'] else 1
    # 同年份内：顶刊优先，其次 Tao Wang 为通讯作者的论文，最后按月份新旧
    jnorm = re.sub(r'\s+', ' ', html.unescape(p['journal'])).strip().lower()
    tier = 0 if jnorm in TIER0 else 1
    tao_corr = 0 if any('taowang' in norm_key(c) for c in CORR.get(p['doi'], [])) else 1
    return (-p['year'], tier, tao_corr, -m, -dd)

pubs.sort(key=sort_key)
print('after sort:', [p['year'] for p in pubs])

problems = []
def render_authors(p):
    corr = CORR.get(p['doi'], [])
    co = COFIRST.get(p['doi'], [])
    co_keys = set()
    for c in co:
        co_keys |= norm_key(c)
    corr_people = [(c, norm_key(c)) for c in corr]
    consumed = set()
    out = []
    for a in p['authors']:
        akeys = norm_key(a)
        is_tao = 'taowang' in akeys
        is_corr = False
        for ci, (cname, ckeys) in enumerate(corr_people):
            if ci in consumed:
                continue
            if akeys & ckeys:
                consumed.add(ci)
                is_corr = True
        name = f'<strong>{esc(a)}</strong>' if is_tao else esc(a)
        if is_corr:
            name += '*'
        if norm_key(a) & co_keys:
            name += '\u2020'
        out.append(name)
    unmatched = [corr_people[ci][0] for ci in range(len(corr_people)) if ci not in consumed]
    if unmatched:
        problems.append((p['doi'], p['title'][:60], unmatched))
    return ', '.join(out)

BADGES = {
    '10.1002/anie.8043102': ('Inside Back Cover', 'https://onlinelibrary.wiley.com/doi/10.1002/anie.2026-m2506061400'),
}

def render_item(p, num):
    vol = str(p['volume']) if p.get('volume') not in (None, '', 'None') else None
    vol_part = f"<em>{html.escape(vol)}</em>, " if vol else ''
    venue = f"<em>{esc(p['journal'])}</em>, <strong>{p['year']}</strong>, {vol_part}{esc(p['page'])}."
    if p['doi'] in COFIRST:
        venue += ' (\u2020equal contribution)'
    badge = ''
    if p['doi'] in BADGES:
        label, url = BADGES[p['doi']]
        badge = f'\n      <a href="{url}" target="_blank" rel="noopener" class="cover-badge">{label}</a>'
    figure = ''
    if p['doi'] in FIGURE_BY_DOI:
        fname, alt = FIGURE_BY_DOI[p['doi']]
        cls = 'pub-figure'
        figure = f'\n      <div class="{cls}"><img src="/images/pubs-2026/{fname}" alt="{alt}"></div>'
    return f'''  <div class="pub-item">
    <span class="pub-num">{num}.</span>
    <div class="pub-text">
      <div class="pub-title"><a href="https://doi.org/{p['doi']}" target="_blank" rel="noopener">{esc(titlecase(TITLE_OVERRIDE.get(p['doi'], p['title'])))}</a></div>
      <div class="pub-authors">{render_authors(p)}</div>
      <div class="pub-venue">{venue}</div>{badge}{figure}
    </div>
  </div>'''

STYLE = '''<style>
.pub-list{margin-top:1.2em}
.pub-item{display:flex;gap:14px;padding:10px 0;border-bottom:1px dashed #d0d0d0;align-items:flex-start}
.pub-num{flex:0 0 34px;font-weight:700;color:#8a0000;font-size:1.05em;text-align:right;line-height:1.5}
.pub-text{flex:1}
.pub-title{font-weight:600;line-height:1.45;margin-bottom:3px}
.pub-authors{line-height:1.5;margin-bottom:3px;font-size:0.9em}
.pub-venue{line-height:1.5}
@media (max-width:480px){.pub-num{flex:0 0 26px;font-size:0.95em}}
</style>'''

n = len(pubs)

FIGURE_BY_DOI = {
    '10.1093/nsr/nwag394': ('nsr-2026.png', 'NSR 2026'),
    '10.31635/ccschem.025.202506170': ('ccs-chem-2026.png', 'CCS Chem 2026'),
    '10.1002/anie.8043102': ('angew-2026.png', 'Angew 2026'),
    '10.1002/ADMA.202521092': ('adv-mater-2026.png', 'Adv Mater 2026'),
    '10.1007/s11426-025-3385-5': ('sci-china-chem-2026.png', 'Sci China Chem 2026'),
    '10.1021/acsnano.6c00162': ('acs-nano-2026.png', 'ACS Nano 2026'),
}

full = [STYLE, '', '<div class="pub-list">']
recent = [STYLE, '', '<div class="pub-list">']
last_year = None
for idx, p in enumerate(pubs):
    num = n - idx
    if p['year'] != last_year:
        full.append(f'  <div class="pub-year" id="year-{p["year"]}">{p["year"]}</div>')
        last_year = p['year']
    full.append(render_item(p, num))
    if idx < 5:
        recent.append(render_item(p, num))
full.append('</div>')
recent.append('</div>')

out = REPO / '_includes' / 'publications.html'
out.write_text('\n'.join(full))
print('written:', out)
# recent-publications.html on the home page is hand-maintained; this output is
# only a by-product kept for reference
(TOOLS / 'gen_recent.html').write_text('\n'.join(recent))
print('papers:', n)
if problems:
    print('UNMATCHED corr names:')
    for pr in problems: print(' ', pr)
else:
    print('all corr names matched OK')
print('unverified DOIs (no stars applied):', UNVERIFIED)
