#!/usr/bin/env python3
"""
SEARAH Makcik v2.2 → v2.3 visual design preprocessor.
Friendly BM kampong register with visual anchors.
"""
import re
import sys
from pathlib import Path

def add_cover(md):
    cover = '''<div class="cover">
<p class="cover-emoji">🌏 🇲🇾 🌏</p>
<p class="cover-kicker">Cerita untuk Jiran-Jiran</p>
<h1 class="cover-title">Kenapa Gas Sarawak<br>Punya Dah Masuk Tangan<br>Orang Italy?</h1>
<p class="cover-subtitle">Cerita dari Makcik Pasar Malam — untuk jiran-jiran yang nak tahu apa jadi kat duit minyak kita</p>
<div class="cover-byline">
<strong>Oleh Arif Fazil</strong>, anak Malaysia yang kerja kat PETRONAS dah lama<br>
999 Meterai · Versi 2.3 Bahasa Makcik · 7 Jun 2026
</div>
</div>

'''
    return cover + md


def add_visual_elements(md):
    # Big stat: USD 120
    md = md.replace(
        'Crude oil prices, he said, had risen 40% since late February. They were now trading around USD 120 per barrel.',
        'Crude oil prices, he said, had risen 40% since late February. They were now trading around USD 120 per barrel.'
    )

    # Big stat at the USD 120 disclosure
    md = md.replace(
        '"Kami telah memendekkan horizon perancangan kami kepada 45 hari," katanya. "Perolehan alternatif berada di peringkat lanjut."',
        '''"Kami telah memendekkan horizon perancangan kami kepada 45 hari," katanya. "Perolehan alternatif berada di peringkat lanjut."

<div class="big-stat">
<span class="number">USD 120</span>
<span class="label">Harga Minyak per Tong</span>
<span class="context">Tapi kos sebenar sampai ke Malaysia: USD 140–165. Tu duit tambahan untuk insurans, kapal, logistik. Bukan poket sesiapa.</span>
</div>'''
    )

    # Fact box at deal summary
    md = md.replace(
        'Modal syarikat: **USD 2**. Dua dolar. Tu duit poket je.',
        '''Modal syarikat: **USD 2**. Dua dolar. Tu duit poket je.

<div class="fact-box">
<div class="fact-box-title">▲ Perjanjian dalam 6 Nombor</div>
<div class="fact-box-content">
<span class="label">Lokasi</span> London, UK (bukan Malaysia!)<br>
<span class="label">Pemilik</span> 50% PETRONAS + 50% Eni (Italy)<br>
<span class="label">Nilai</span> USD 15 bilion (RM 70 bilion) untuk 5 tahun<br>
<span class="label">Aset</span> 19 ladang (14 Indonesia, 5 Malaysia)<br>
<span class="label">Pengeluaran</span> 300,000 → 500,000 tong/hari<br>
<span class="label">Mula</span> 1 Julai 2026
</div>
</div>'''
    )

    # Key numbers: 5 Malaysia assets
    md = md.replace(
        'Lima kat Malaysia tu (per Arif, Jun 2026): **SK316** (Sarawak, ada Kasawari), **Kasawari** (lapang, Sarawak), **ExxonMobil 2008 PSC** (diambil dari Exxon tahun 2024), **Angsi Besar** (MTJDA, kawasan Malaysia-Thailand), dan **NC3** (juga MTJDA).',
        '''Lima kat Malaysia tu (per Arif, Jun 2026): **SK316** (Sarawak, ada Kasawari), **Kasawari** (lapang, Sarawak), **ExxonMobil 2008 PSC** (diambil dari Exxon tahun 2024), **Angsi Besar** (MTJDA, kawasan Malaysia-Thailand), dan **NC3** (juga MTJDA).

<div class="key-numbers">
<span class="row"><span class="k">Sarawak</span><span class="v">SK316, Kasawari</span></span>
<span class="row"><span class="k">Luar Pesisir Semenanjung</span><span class="v">2008 PSC</span></span>
<span class="row"><span class="k">MTJDA (MY-TH)</span><span class="v">Angsi Besar, NC3</span></span>
<span class="row"><span class="k">Jumlah</span><span class="v">5 LADANG</span></span>
</div>'''
    )

    # Big stat: 350k vs 950k
    md = md.replace(
        '- Malaysia hasilkan **350,000 tong** minyak sehari dari ladang sendiri.\n- Penapis kita boleh proses **950,000 tong** sehari.\n- Jurang: **600,000 tong** sehari. Kena import.',
        '''- Malaysia hasilkan **350,000 tong** minyak sehari dari ladang sendiri.
- Penapis kita boleh proses **950,000 tong** sehari.
- Jurang: **600,000 tong** sehari. Kena import.

<div class="big-stat">
<span class="number">600,000</span>
<span class="label">Jurang Tong Sehari</span>
<span class="context">Yang kita kena import setiap hari. Macam tu la selama bertahun-tahun. SEARAH tak selesaikan jurang tu dalam masa singkat. Tu projek 5–8 tahun.</span>
</div>'''
    )

    # Pull quote: 2 vs 2
    md = md.replace(
        '2 orang Italy, duduk kat London\n- 2 orang Malaysia, duduk kat KL\n\nKalau ada mesyuarat kecemasan, 2 orang Italy boleh jalan kaki ke ENI House. 2 orang Malaysia kena terbang 13 jam, duduk hotel.',
        '''- 2 orang Italy, duduk kat London
- 2 orang Malaysia, duduk kat KL

Kalau ada mesyuarat kecemasan, 2 orang Italy boleh jalan kaki ke ENI House. 2 orang Malaysia kena terbang 13 jam, duduk hotel.

<div class="pull-quote">
2 pengarah Italy vs 2 pengarah Malaysia. Tiada siapa yang menang kalau seri. Tiada mekanisme penentu seri.
</div>'''
    )

    # Callout for closing — what to do
    md = md.replace(
        'Gas Sarawak bukan gas orang Sarawak je. Tu gas anak cucu kita semua. Kalau hilang kat tangan orang London, macam mana nak tarik balik?',
        '''Gas Sarawak bukan gas orang Sarawak je. Tu gas anak cucu kita semua. Kalau hilang kat tangan orang London, macam mana nak tarik balik?

<div class="callout">
<div class="callout-title">▲ Buat Ini Sekarang</div>
1. Kongsi cerita ni kat WhatsApp group jiran, group surau, group pasar.<br>
2. Hubungi ahli parlimen area hang. Tanya soalan kat dokumen ni.<br>
3. Support akhbar yang buat siasatan (Malaysiakini, FMT, The Edge).<br>
4. Tanda tangan petition pasal SEARAH kalau ada.
</div>'''
    )

    return md


def process(input_md, output_md):
    text = Path(input_md).read_text()
    text = add_cover(text)
    text = add_visual_elements(text)
    Path(output_md).write_text(text)
    print(f"Visual design injected: {input_md} → {output_md}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: visual_design_makcik.py input.md output.md")
        sys.exit(1)
    process(sys.argv[1], sys.argv[2])
