"""Icone SVG in linea (tratto), colore = currentColor."""

def _i(path, size=26, sw=2.2):
    return (f'<svg class="ico" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>')

MENU = _i('<path d="M4 7h16M4 12h16M4 17h16"/>')
CHECK = _i('<path d="M20 6 9 17l-5-5"/>', 18, 2.6)
BOLT = _i('<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>')
CAL = _i('<rect x="3" y="4" width="18" height="18" rx="3"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="m9 15 2 2 4-4"/>')
PHONE = _i('<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/>')
CLOCK = _i('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', 24)
CHART = _i('<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>')
USERS = _i('<circle cx="9" cy="8" r="4"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6"/><path d="M17 4a4 4 0 0 1 0 8M22 21c0-3-1.6-5-4-5.6"/>')
PLUG = _i('<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0V8zM12 18v4"/>')
DOC = _i('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>')
COPY = _i('<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/>')
LOCK = _i('<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>')
PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 4.5v15a1 1 0 0 0 1.5.9l12-7.5a1 1 0 0 0 0-1.8l-12-7.5A1 1 0 0 0 7 4.5z"/></svg>'
TEL = _i('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>', 22)
MAIL = _i('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>', 22)
PIN = _i('<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>', 22)
ARROW = _i('<path d="M5 12h14M13 6l6 6-6 6"/>', 18, 2.4)
APPLE = _i('<path d="M16 3c-1.2.1-2.6.9-3.3 1.9-.7.8-1.2 2-1 3.2 1.3.1 2.6-.7 3.4-1.7.7-.9 1.1-2.1.9-3.4zM12 8.3c-.9 0-2.2-1-3.6-1C6 7.4 4 9.4 4 13c0 4.4 3 8 4.7 8 1.1 0 1.6-.7 3.3-.7s2 .7 3.3.7C17 21 20 17.5 20 16c-2-.8-3-2.6-3-4.4 0-1.6.9-3 2.2-3.8-.9-1.3-2.4-2-3.8-2-1.3 0-2 .5-3.6.5z"/>', 20, 1.8)
ANDROID = _i('<rect x="5" y="9" width="14" height="10" rx="2"/><path d="M8 9a4 4 0 0 1 8 0M9 6 7.5 4M15 6l1.5-2M9 19v2M15 19v2"/>', 20, 1.8)
GLOBE = _i('<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>', 20, 1.8)

# Illustrazione decorativa: le barre arrotondate del logo
DECO_BARS = '''<svg class="hero-deco" viewBox="0 0 600 600" aria-hidden="true" focusable="false" data-parallax="0.06">
<rect x="40" y="40" width="520" height="520" rx="150" fill="#E3E4F7"/>
<rect x="150" y="230" width="70" height="210" rx="35" fill="#fff"/>
<rect x="265" y="160" width="70" height="280" rx="35" fill="#fff"/>
<rect x="380" y="300" width="70" height="140" rx="35" fill="#fff"/>
</svg>'''

# Illustrazione tonale: cronometro + barre (per sezioni senza screenshot)
ILLU_TIME = '''<svg viewBox="0 0 480 360" role="img" aria-label="{label}" style="width:100%;height:auto">
<rect x="10" y="20" width="460" height="320" rx="60" fill="#F4F4FD"/>
<circle cx="180" cy="190" r="104" fill="#fff" stroke="#BDBBF1" stroke-width="14"/>
<path d="M180 120v70l46 30" stroke="#4654A3" stroke-width="16" stroke-linecap="round" fill="none"/>
<rect x="164" y="56" width="32" height="28" rx="10" fill="#4654A3"/>
<rect x="320" y="170" width="34" height="110" rx="17" fill="#6B7ACC"/>
<rect x="366" y="120" width="34" height="160" rx="17" fill="#4654A3"/>
<rect x="412" y="200" width="34" height="80" rx="17" fill="#BDBBF1"/>
<circle cx="96" cy="300" r="10" fill="#F95B3D"/>
</svg>'''

ILLU_FIELD = '''<svg viewBox="0 0 480 360" role="img" aria-label="{label}" style="width:100%;height:auto">
<rect x="10" y="20" width="460" height="320" rx="60" fill="#F4F4FD"/>
<rect x="70" y="70" width="150" height="250" rx="28" fill="#270949"/>
<rect x="82" y="88" width="126" height="200" rx="18" fill="#fff"/>
<rect x="98" y="110" width="94" height="14" rx="7" fill="#BDBBF1"/>
<rect x="98" y="140" width="94" height="28" rx="8" fill="#F4F4FD" stroke="#D5D3F2"/>
<rect x="98" y="178" width="94" height="28" rx="8" fill="#F4F4FD" stroke="#D5D3F2"/>
<rect x="98" y="232" width="94" height="30" rx="15" fill="#4654A3"/>
<path d="M290 260c0-50 40-90 90-90" stroke="#BDBBF1" stroke-width="14" stroke-linecap="round" fill="none" stroke-dasharray="2 26"/>
<path d="M380 120c-26 0-46 20-46 46 0 34 46 82 46 82s46-48 46-82c0-26-20-46-46-46z" fill="#4654A3"/>
<circle cx="380" cy="166" r="16" fill="#fff"/>
<rect x="250" y="276" width="170" height="40" rx="20" fill="#fff" stroke="#D5D3F2" stroke-width="3"/>
<rect x="266" y="290" width="70" height="12" rx="6" fill="#6B7ACC"/>
</svg>'''

ILLU_PROJECT = '''<svg viewBox="0 0 480 360" role="img" aria-label="{label}" style="width:100%;height:auto">
<rect x="10" y="20" width="460" height="320" rx="60" fill="#F4F4FD"/>
<rect x="60" y="70" width="360" height="230" rx="24" fill="#fff" stroke="#D5D3F2" stroke-width="3"/>
<rect x="84" y="100" width="120" height="14" rx="7" fill="#270949"/>
<rect x="84" y="140" width="250" height="22" rx="11" fill="#E3E4F7"/><rect x="84" y="140" width="190" height="22" rx="11" fill="#4654A3"/>
<rect x="84" y="182" width="250" height="22" rx="11" fill="#E3E4F7"/><rect x="84" y="182" width="270" height="22" rx="11" fill="#F95B3D" opacity=".85"/>
<rect x="84" y="224" width="250" height="22" rx="11" fill="#E3E4F7"/><rect x="84" y="224" width="130" height="22" rx="11" fill="#6B7ACC"/>
<rect x="334" y="128" width="4" height="130" rx="2" fill="#270949" opacity=".35"/>
<text x="344" y="122" font-family="Montserrat, sans-serif" font-size="13" font-weight="700" fill="#270949">budget</text>
</svg>'''

ILLU_AGENCY = '''<svg viewBox="0 0 480 360" role="img" aria-label="{label}" style="width:100%;height:auto">
<rect x="10" y="20" width="460" height="320" rx="60" fill="#F4F4FD"/>
<circle cx="190" cy="185" r="110" fill="#E3E4F7"/>
<path d="M190 185V75a110 110 0 0 1 104 74z" fill="#4654A3"/>
<path d="M190 185l104-36a110 110 0 0 1-40 125z" fill="#6B7ACC"/>
<path d="M190 185l64 89a110 110 0 0 1-120 6z" fill="#BDBBF1"/>
<circle cx="190" cy="185" r="52" fill="#fff"/>
<rect x="340" y="90" width="90" height="26" rx="13" fill="#4654A3"/>
<rect x="340" y="132" width="70" height="26" rx="13" fill="#6B7ACC"/>
<rect x="340" y="174" width="56" height="26" rx="13" fill="#BDBBF1"/>
<rect x="340" y="216" width="40" height="26" rx="13" fill="#987FC6"/>
</svg>'''

ILLU_CODE = '''<svg viewBox="0 0 480 360" role="img" aria-label="{label}" style="width:100%;height:auto">
<rect x="10" y="20" width="460" height="320" rx="60" fill="#F4F4FD"/>
<rect x="60" y="66" width="360" height="236" rx="22" fill="#270949"/>
<circle cx="86" cy="90" r="6" fill="#F95B3D"/><circle cx="106" cy="90" r="6" fill="#BDBBF1"/><circle cx="126" cy="90" r="6" fill="#6B7ACC"/>
<rect x="86" y="124" width="120" height="12" rx="6" fill="#6B7ACC"/>
<rect x="110" y="150" width="170" height="12" rx="6" fill="#BDBBF1"/>
<rect x="110" y="176" width="130" height="12" rx="6" fill="#987FC6"/>
<rect x="86" y="202" width="90" height="12" rx="6" fill="#6B7ACC"/>
<rect x="300" y="196" width="96" height="84" rx="18" fill="#4654A3"/>
<path d="M348 216v24l16 10" stroke="#fff" stroke-width="8" stroke-linecap="round" fill="none"/>
</svg>'''
