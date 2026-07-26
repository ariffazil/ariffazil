#!/usr/bin/env python3
"""
SEARAH Harakah v2.2 → v2.3 visual design preprocessor.
Same visual treatment as WSJ v2.3, in Bahasa Melayu.
"""
import re
import sys
from pathlib import Path

def add_masthead(md):
    masthead = '''<div class="masthead">
<p class="masthead-kicker">SIASATAN · EDISI KHAS</p>
<h1 class="masthead-title">Persoalan RM70 Bilion</h1>
<p class="masthead-subtitle">Bagaimana Struktur Perjanjian Gas Terbesar Malaysia — dan Siapa yang Tidak Termasuk dalam Bilik</p>
<div class="masthead-byline">
<span class="author">Oleh Arif Fazil</span> &nbsp;|&nbsp; Perisikan Persekutuan arifOS &nbsp;|&nbsp; <span class="meta">Meterai 999 · Versi 2.3 Gred Harakah · 7 Jun 2026</span>
</div>
</div>

'''
    return masthead + md


def upgrade_changelog(md):
    pattern = r'(## LOG PERUBAHAN — Jun 2026 \(v2\.1 → v2\.2\)\n.*?)(?=\n## )'
    def repl(m):
        content = m.group(1)
        content = re.sub(r'^## LOG PERUBAHAN — Jun 2026 \(v2\.1 → v2\.2\)\n', '', content)
        return '<div class="changelog">\n<div class="changelog-title">LOG PERUBAHAN — Jun 2026 (v2.1 → v2.2)</div>\n' + content + '\n</div>\n\n'
    return re.sub(pattern, repl, md, count=1, flags=re.DOTALL)


def add_visual_elements(md):
    # Big stat: USD 120 / 45 hari
    md = md.replace(
        '"Kami telah memendekkan horizon perancangan kami kepada 45 hari," katanya. "Perolehan alternatif berada di peringkat lanjut."',
        '''"Kami telah memendekkan horizon perancangan kami kepada 45 hari," katanya. "Perolehan alternatif berada di peringkat lanjut."

<div class="big-stat">
<span class="number">USD 120</span>
<span class="label">Harga Skrin Setong</span>
<span class="context">Kos sebenar yang dihantar ke Malaysia: USD 140–165 setong bersamaan. Jurang itu adalah insurans risiko perang, gangguan penghantaran, dan logistik — bukan poket sesiapa.</span>
</div>'''
    )

    # Fact box: Deal at a Glance
    md = md.replace(
        'Perjanjian distrukturkan melalui syarikat bernama **SEARAH LIMITED** — berdaftar di United Kingdom, Nombor Syarikat 17027115, di ENI House, 10 Ebury Bridge Road, London, SW1W 8PZ.',
        '''Perjanjian distrukturkan melalui syarikat bernama **SEARAH LIMITED** — berdaftar di United Kingdom, Nombor Syarikat 17027115, di ENI House, 10 Ebury Bridge Road, London, SW1W 8PZ.

<div class="fact-box">
<div class="fact-box-title">▲ Perjanjian Sekilas Pandang</div>
<div class="fact-box-content">
<span class="label">Syarikat</span> SEARAH Limited (No. 17027115)<br>
<span class="label">Berdaftar</span> ENI House, 10 Ebury Bridge Road, London<br>
<span class="label">Pemegang Saham</span> 50% PETRONAS Carigali Int'l Ventures · 50% Eni Lasmo Plc<br>
<span class="label">Ditadbir</span> Akta Syarikat 2006 UK (Undang-undang Inggeris)<br>
<span class="label">Modal Saham</span> USD 2 &nbsp;|&nbsp; <span class="label">Capex</span> USD 15 bilion / 5 tahun<br>
<span class="label">Pengeluaran</span> 300,000 → 500,000 boe/hari<br>
<span class="label">Rizab</span> ~3 bilion tong ditemui + ~10 bilion tong potensi<br>
<span class="label">Program Kerja</span> 8 projek pembangunan, 15 telaga eksplorasi<br>
<span class="label">Revolver</span> USD 6 bilion (JP Morgan)<br>
<span class="label">Sasaran Operasi</span> 1 Julai 2026
</div>
</div>'''
    )

    # Pull quote: Irony
    md = md.replace(
        'Perjanjian antarabangsa 2 bulan yang pergi ke mana-mana.',
        '''Perjanjian antarabangsa 2 bulan yang pergi ke mana-mana.

<div class="pull-quote">
PETRONAS tidak dapat menyelesaikan dengan PETROS — entiti Malaysia yang mewakili negeri Malaysia — selepas 62 tahun. Tetapi PETRONAS boleh, dalam beberapa bulan, menandatangani JV USD 15 bilion dengan syarikat Itali, mendaftarkannya di UK, dan menumpukan aset Malaysia kepada bidang kuasa undang-undang Inggeris.
<span class="attribution">— Bahagian VII · Sangkaan Tidak Masuk Akal</span>
</div>'''
    )

    # Callout: Jurisdiction
    md = md.replace(
        'Jawapannya, di bawah struktur ini, ialah London.',
        '''Jawapannya, di bawah struktur ini, ialah **London**.

<div class="callout">
<div class="callout-title">▲ Soalan Bidang Kuasa</div>
Jika sesuatu menjadi salah dengan aset gas Sarawak yang sekarang berada dalam SEARAH LIMITED, pertikaian <strong>tidak</strong> pergi ke Mahkamah Tinggi Kuching. Ia pergi ke <strong>mahkamah Inggeris</strong> atau <strong>arbitrasi London</strong> (ICC / LCIA). Rakyat Malaysia, ahli parlimen, dan pengawal selia mempunyai <strong>akses yang dikurangkan</strong> kepada proses penyelesaian pertikaian berbanding struktur yang ditadbir oleh undang-undang Malaysia.
</div>'''
    )

    # Key numbers: BIT
    md = md.replace(
        'Ini bermakna Eni Lasmo Plc, sebagai syarikat berdaftar UK, tidak mempunyai perlindungan triti BIT terhadap Malaysia. Perlindungannya berjalan melalui undang-undang kontrak Inggeris dan undang-undang syarikat UK — bukan melalui triti pelaburan.',
        '''Ini bermakna Eni Lasmo Plc, sebagai syarikat berdaftar UK, tidak mempunyai perlindungan triti BIT terhadap Malaysia. Perlindungannya berjalan melalui undang-undang kontrak Inggeris dan undang-undang syarikat UK — bukan melalui triti pelaburan.

<div class="key-numbers">
<span class="row"><span class="k">BIT Malaysia-Itali</span><span class="v">TIADA</span></span>
<span class="row"><span class="k">BIT Malaysia-UK (aktif)</span><span class="v">TIADA</span></span>
<span class="row"><span class="k">CSP UK-Malaysia (2022)</span><span class="v">BUKAN BIT</span></span>
<span class="row"><span class="k">Mekanisme perlindungan sebenar</span><span class="v">UNDANG-UNDUK INGGERIS</span></span>
</div>'''
    )

    # Big stat: 2 vs 2
    md = md.replace(
        'Tiada mekanisme penentu seri yang didedahkan untuk kebuntuan lembaga 2-2.',
        '''Tiada mekanisme penentu seri yang didedahkan untuk kebuntuan lembaga 2-2.

<div class="big-stat">
<span class="number">2 lawan 2</span>
<span class="label">Komposisi Lembaga · SEARAH LIMITED</span>
<span class="context">2 pengarah Itali (jalan kaki dari ENI House) vs 2 pengarah Malaysia (penerbangan 13 jam, hotel). Tiada mekanisme penentu seri yang didedahkan. Pengerusi PETRONAS Mohd Bakke Salleh sebelum ini Pengerusi 1MDB.</span>
</div>'''
    )

    # Key numbers: 350k vs 950k
    md = md.replace(
        '**Sebelum krisis:**\n\n- Pengeluaran minyak domestik: 350,000 boepd\n- Kapasiti penapisan: ~950,000 tong sehari\n- Kadar sara diri: ~35-40%',
        '''**Sebelum krisis:**

<div class="key-numbers">
<span class="row"><span class="k">Pengeluaran minyak domestik</span><span class="v">350,000 boepd</span></span>
<span class="row"><span class="k">Kapasiti penapisan</span><span class="v">950,000 tong/hari</span></span>
<span class="row"><span class="k">Kadar sara diri</span><span class="v">~35–40%</span></span>
<span class="row"><span class="k">Jurang struktur</span><span class="v">600,000 tong/hari</span></span>
</div>'''
    )

    # Callout: To the rakyat
    md = md.replace(
        '**Kepada rakyat.**',
        '''**Kepada rakyat.**

<div class="callout">
<div class="callout-title">▲ Apa yang Dokumen Ini Minta</div>
Insentif struktur sistem yang menghasilkan SEARAH <strong>tidak</strong> sejajar dengan kepentingan rakyat Malaysia biasa. Orang yang bertanggungjawab untuk sistem itu — di peringkat lembaga, eksekutif, dan politik — <strong>tidak dipertanggungjawabkan</strong> untuk jurang itu. Itu tuntutannya. Resit di atas. Soalannya milik Parlimen.
</div>'''
    )

    return md


def process(input_md, output_md):
    text = Path(input_md).read_text()
    text = add_masthead(text)
    text = upgrade_changelog(text)
    text = add_visual_elements(text)
    Path(output_md).write_text(text)
    print(f"Visual design injected: {input_md} → {output_md}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: visual_design_harakah.py input.md output.md")
        sys.exit(1)
    process(sys.argv[1], sys.argv[2])
