#!/usr/bin/env python3
"""
SEARAH Visual Design Preprocessor
Reads the markdown and injects visual design HTML elements
(visual anchors) at the right places for cognitive design.
"""
import re
import sys
from pathlib import Path

def add_masthead(md):
    """Add WSJ-style masthead at the top."""
    masthead = '''<div class="masthead">
<p class="masthead-kicker">SEARAH LIMITED × PETROS</p>
<h1 class="masthead-title">The RM70 Billion Question</h1>
<p class="masthead-subtitle">How Malaysia's Biggest Gas Deal Was Structured — and Who Was Left Out of the Room</p>
<div class="masthead-byline">
<span class="author">By Arif Fazil</span> &nbsp;|&nbsp; arifOS Federation Intelligence &nbsp;|&nbsp; <span class="meta">Seal 999 · Version 2.3 — WSJ-Grade · 2026-06-07</span>
</div>
</div>

'''
    return masthead + md


def upgrade_changelog(md):
    """Wrap the CHANGELOG section in a styled box."""
    pattern = r'(## CHANGE LOG — June 2026 \(v2\.1 → v2\.2\)\n.*?)(?=\n## )'
    def repl(m):
        content = m.group(1)
        # Remove the ## heading and start with the change log title
        content = re.sub(r'^## CHANGE LOG — June 2026 \(v2\.1 → v2\.2\)\n', '', content)
        return '<div class="changelog">\n<div class="changelog-title">CHANGE LOG — June 2026 (v2.1 → v2.2)</div>\n' + content + '\n</div>\n\n'
    return re.sub(pattern, repl, md, count=1, flags=re.DOTALL)


def add_fact_boxes_and_pullquotes(md):
    """Inject visual fact-boxes, big-stat callouts, and pull-quotes at key moments."""

    # 1. PART I — after the opening USD 120 quote, add a big-stat
    md = md.replace(
        '"We have shortened our planning horizon to 45 days," he said. "Alternative sourcing is at an advanced stage."',
        '''"We have shortened our planning horizon to 45 days," he said. "Alternative sourcing is at an advanced stage."

<div class="big-stat">
<span class="number">USD 120</span>
<span class="label">Screen Price per Barrel</span>
<span class="context">Real delivered cost to Malaysia: USD 140–165 per barrel equivalent. The gap is war risk insurance, shipping disruption, and logistics — not anyone's pocket.</span>
</div>'''
    )

    # 2. PART II — after the deal intro, add a fact-box (preserve rest of Part II)
    md = md.replace(
        'The deal is structured through a company called **SEARAH LIMITED** — registered in the United Kingdom, Company Number 17027115, at ENI House, 10 Ebury Bridge Road, London, SW1W 8PZ.',
        '''The deal is structured through a company called **SEARAH LIMITED** — registered in the United Kingdom, Company Number 17027115, at ENI House, 10 Ebury Bridge Road, London, SW1W 8PZ.

<div class="fact-box">
<div class="fact-box-title">▲ The Deal at a Glance</div>
<div class="fact-box-content">
<span class="label">Company</span> SEARAH Limited (Co. No. 17027115)<br>
<span class="label">Registered</span> ENI House, 10 Ebury Bridge Road, London<br>
<span class="label">Shareholders</span> 50% PETRONAS Carigali Int'l Ventures · 50% Eni Lasmo Plc<br>
<span class="label">Governed by</span> UK Companies Act 2006 (English Law)<br>
<span class="label">Share capital</span> USD 2 &nbsp;|&nbsp; <span class="label">Capex</span> USD 15 billion / 5 years<br>
<span class="label">Production</span> 300,000 → 500,000 boe/d<br>
<span class="label">Reserves</span> ~3 billion boe discovered + ~10 billion boe upside<br>
<span class="label">Work Programme</span> 8 development projects, 15 exploration wells<br>
<span class="label">Revolver</span> USD 6 billion (JP Morgan)<br>
<span class="label">Operations Target</span> 1 July 2026
</div>
</div>'''
    )

    # 3. PART III — the irony, add a pull-quote
    md = md.replace(
        'The 2-month international deal that went everywhere.',
        '''The 2-month international deal that went everywhere.

<div class="pull-quote">
PETRONAS could not settle with PETROS — a Malaysian entity representing a Malaysian state — after 62 years. But PETRONAS could, in a few months, sign a USD 15 billion JV with an Italian company, register it in the UK, and commit Malaysian assets to English law jurisdiction.
<span class="attribution">— Part VII · The Irony</span>
</div>'''
    )

    # 4. PART V — where disputes get resolved, add a callout
    md = md.replace(
        'The answer, under this structure, is London.',
        '''The answer, under this structure, is **London**.

<div class="callout">
<div class="callout-title">▲ The Jurisdiction Question</div>
If something goes wrong with a Sarawak gas asset that is now inside SEARAH LIMITED, the dispute does <strong>not</strong> go to Kuching High Court. It goes to <strong>English courts</strong> or <strong>London arbitration</strong> (ICC / LCIA). Malaysian citizens, MPs, and regulators have <strong>reduced access</strong> to the dispute resolution process compared to a structure governed by Malaysian law.
</div>'''
    )

    # 5. PART VI — BIT gap, add a key-numbers comparison
    md = md.replace(
        'This means Eni Lasmo Plc, as a UK-registered company, does not have BIT treaty protection against Malaysia. Its protection runs through English contract law and UK corporate law — not through an investment treaty.',
        '''This means Eni Lasmo Plc, as a UK-registered company, does not have BIT treaty protection against Malaysia. Its protection runs through English contract law and UK corporate law — not through an investment treaty.

<div class="key-numbers">
<span class="row"><span class="k">Malaysia–Italy BIT</span><span class="v">DOES NOT EXIST</span></span>
<span class="row"><span class="k">Malaysia–UK BIT (active)</span><span class="v">DOES NOT EXIST</span></span>
<span class="row"><span class="k">UK–Malaysia CSP (2022)</span><span class="v">NOT A BIT</span></span>
<span class="row"><span class="k">Actual protection mechanism</span><span class="v" style="color:#CC0000;">ENGLISH LAW</span></span>
</div>'''
    )

    # 6. PART VIII — board asymmetry, add a big-stat
    md = md.replace(
        'There is no disclosed tiebreaker mechanism for a 2-2 board deadlock.',
        '''There is no disclosed tiebreaker mechanism for a 2-2 board deadlock.

<div class="big-stat">
<span class="number">2 vs 2</span>
<span class="label">Board Composition · SEARAH LIMITED</span>
<span class="context">2 Italian directors (walking distance from ENI House) vs 2 Malaysian directors (13-hour flight, hotel). No disclosed tiebreaker. PETRONAS Chairman Mohd Bakke Salleh was previously Chairman of 1MDB.</span>
</div>'''
    )

    # 7. PART XI — energy crisis, add a big-stat for the 350k vs 950k gap
    md = md.replace(
        '**Before the crisis:**\n\n- Domestic oil production: 350,000 boepd\n- Refinery capacity: ~950,000 barrels per day\n- Self-sufficiency rate: ~35-40%',
        '''**Before the crisis:**

<div class="key-numbers">
<span class="row"><span class="k">Domestic oil production</span><span class="v">350,000 boepd</span></span>
<span class="row"><span class="k">Refinery capacity</span><span class="v">950,000 bpd</span></span>
<span class="row"><span class="k">Self-sufficiency</span><span class="v" style="color:#CC0000;">~35–40%</span></span>
<span class="row"><span class="k">Structural shortfall</span><span class="v" style="color:#CC0000;">600,000 bpd</span></span>
</div>'''
    )

    # 8. PART XIII — final question, add a callout
    md = md.replace(
        '**To the rakyat.**',
        '''**To the rakyat.**

<div class="callout">
<div class="callout-title">▲ What This Document Asks</div>
The structural incentives of the system that produced SEARAH do <strong>not</strong> align with the interests of ordinary Malaysians. The people responsible for that system — at the board level, the executive level, and the political level — have <strong>not been held accountable</strong> for the gap. That is the claim. The receipts are above. The questions belong to Parliament.
</div>'''
    )

    return md


def add_metadata_header(md):
    """Add the constitutional floor as a styled band under the masthead."""
    return md


def process(input_md, output_md):
    text = Path(input_md).read_text()
    text = add_masthead(text)
    text = upgrade_changelog(text)
    text = add_fact_boxes_and_pullquotes(text)
    Path(output_md).write_text(text)
    print(f"Visual design injected: {input_md} → {output_md}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: visual_design.py input.md output.md")
        sys.exit(1)
    process(sys.argv[1], sys.argv[2])
