import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('busan_data.json', encoding='utf-8') as f:
    data_json = f.read()

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,"Hiragino Kaku Gothic ProN","Noto Sans JP","Yu Gothic",BlinkMacSystemFont,"Segoe UI",sans-serif;background:#EEF2F7;color:#1E293B;font-size:13px;line-height:1.5}

/* LOGIN */
#login-screen{display:flex;align-items:center;justify-content:center;min-height:100vh;background:#EEF2F7}
.login-card{background:#fff;border-radius:16px;padding:44px 40px 36px;max-width:400px;width:90%;text-align:center;box-shadow:0 8px 32px rgba(0,0,0,.12)}
.login-kmtc-badge{display:inline-block;background:#0D2D5C;color:#F0A500;font-size:22px;font-weight:900;padding:8px 22px;border-radius:8px;border:2px solid #F0A500;letter-spacing:.06em;margin-bottom:16px}
.login-org{font-size:12px;color:#64748B;margin-bottom:4px;font-weight:600}
.login-title{font-size:14px;color:#334155;margin-bottom:6px;line-height:1.5}
.login-sub{font-size:11px;color:#94A3B8;margin-bottom:24px;line-height:1.6}
.login-btn-area{margin-bottom:16px}
.login-note{font-size:10px;color:#94A3B8;line-height:1.7;border-top:1px solid #F1F5F9;padding-top:16px;margin-top:8px}
#login-error{display:none;background:#FEF2F2;border:1px solid #FECACA;border-radius:8px;padding:8px 12px;font-size:11px;color:#DC2626;margin-top:12px;text-align:left}

/* DASHBOARD */
#dashboard{display:none}

/* Header */
.hdr{background:#0D2D5C;padding:0 24px;border-bottom:3px solid #F0A500;display:flex;align-items:center;justify-content:space-between;height:52px;position:sticky;top:0;z-index:200}
.hdr-left{display:flex;align-items:center;gap:14px}
.hdr-badge{background:#0D2D5C;color:#F0A500;font-size:15px;font-weight:900;padding:4px 14px;border-radius:6px;border:2px solid #F0A500;letter-spacing:.06em;line-height:1}
.hdr-title{color:#CBD5E1;font-size:12px;font-weight:500;letter-spacing:.02em}
.hdr-right{display:flex;align-items:center;gap:12px}
.hdr-user{color:#93C5FD;font-size:11px;font-weight:500}
.hdr-logout{background:transparent;color:#CBD5E1;border:1px solid rgba(255,255,255,.25);border-radius:5px;padding:4px 12px;font-size:11px;cursor:pointer;font-family:inherit;transition:all .15s}
.hdr-logout:hover{background:rgba(255,255,255,.1);color:#fff}

/* Tab / ctrl bar */
.ctrl-bar{background:#fff;border-bottom:1px solid #E2E8F0;position:sticky;top:52px;z-index:100;box-shadow:0 1px 6px rgba(0,0,0,.06)}
.tab-row{display:flex;align-items:center;padding:0 24px;gap:0;overflow-x:auto}
.top-tab{padding:12px 16px;font-size:12px;cursor:pointer;color:#64748B;border:none;border-bottom:2px solid transparent;margin-bottom:-1px;background:none;font-family:inherit;font-weight:600;white-space:nowrap;transition:all .15s;flex-shrink:0}
.top-tab:hover:not(.active){color:#334155;background:#F8FAFC}
.top-tab.active{color:#0D2D5C;border-bottom-color:#0D2D5C;font-weight:700}
.top-tab.tab-kmtc{color:#15803D}
.top-tab.tab-kmtc.active{color:#15803D;border-bottom-color:#15803D}
.top-tab.tab-map{color:#0F766E}
.top-tab.tab-map.active{color:#0F766E;border-bottom-color:#0F766E}
.tab-right{margin-left:auto;display:flex;align-items:center;gap:8px;padding-right:4px;flex-shrink:0}
.sz-label{font-size:10px;color:#94A3B8;font-weight:600}
.sz-btn{padding:3px 10px;font-size:11px;border:1px solid #CBD5E1;border-radius:4px;cursor:pointer;background:#fff;color:#475569;font-family:inherit;font-weight:600;transition:all .15s}
.sz-btn.on{background:#0D2D5C;border-color:#0D2D5C;color:#fff}
.sz-btn:hover:not(.on){background:#F1F5F9}
.meta-row{padding:4px 24px;background:#F8FAFC;border-top:1px solid #F1F5F9;font-size:10px;color:#94A3B8;display:flex;align-items:center;gap:16px}
.meta-row strong{color:#64748B}

/* Filter bar */
.filter-bar{background:#F8FAFC;border-bottom:1px solid #E2E8F0;padding:8px 24px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.filter-label{font-size:10px;font-weight:700;color:#64748B;white-space:nowrap}
.pill{display:inline-flex;padding:4px 11px;border-radius:99px;font-size:11px;border:1.5px solid #CBD5E1;cursor:pointer;background:#fff;color:#475569;font-family:inherit;font-weight:600;transition:all .12s}
.pill.on{background:#0D2D5C;border-color:#0D2D5C;color:#fff}
.pill.on-g{background:#15803D;border-color:#15803D;color:#fff}
.pill:hover:not(.on):not(.on-g){background:#F1F5F9}
.f-select{padding:4px 10px;border-radius:6px;border:1.5px solid #CBD5E1;font-size:11px;font-family:inherit;color:#334155;background:#fff;cursor:pointer}
.f-toggle{display:flex;align-items:center;gap:7px;cursor:pointer;font-size:11px;font-weight:700;color:#15803D}
.f-toggle input{accent-color:#15803D;width:15px;height:15px;cursor:pointer}

/* Main */
.main{padding:20px 24px}
.panel{display:none}.panel.active{display:block}

/* KPI */
.kpi-row{display:grid;gap:12px;margin-bottom:16px}
.kpi-row.col5{grid-template-columns:repeat(5,1fr)}
.kpi-row.col4{grid-template-columns:repeat(4,1fr)}
.kpi-row.col3{grid-template-columns:repeat(3,1fr)}
.kpi-card{background:#fff;border-radius:10px;padding:14px 16px;box-shadow:0 2px 8px rgba(0,0,0,.06);border-left:4px solid #CBD5E1}
.kpi-card.navy{border-left-color:#0D2D5C}
.kpi-card.amber{border-left-color:#F0A500}
.kpi-card.green{border-left-color:#16A34A}
.kpi-card.teal{border-left-color:#0F766E}
.kpi-card.purple{border-left-color:#7C3AED}
.kpi-label{font-size:9px;color:#94A3B8;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.kpi-val{font-size:28px;font-weight:800;color:#0D2D5C;line-height:1.1}
.kpi-sub{font-size:10px;color:#94A3B8;margin-top:4px}

/* Cards */
.card{background:#fff;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.06);padding:16px;margin-bottom:14px}
.card-title{font-size:11px;font-weight:700;color:#0D2D5C;margin-bottom:12px;padding-bottom:8px;border-bottom:2px solid #EEF2F7;text-transform:uppercase;letter-spacing:.05em;display:flex;align-items:center;gap:8px}
.card-title .badge{background:#0D2D5C;color:#fff;font-size:9px;padding:2px 8px;border-radius:3px;font-weight:700;letter-spacing:.04em}
.card-title .badge-g{background:#15803D}

/* Result strip */
.result-strip{font-size:11px;color:#64748B;font-weight:600;margin-bottom:12px;display:flex;align-items:center;gap:16px}
.result-strip strong{color:#0D2D5C;font-size:13px}

/* Table */
.tbl-wrap{overflow-x:auto;border-radius:8px;border:1px solid #E2E8F0;background:#fff;margin-bottom:16px}
table{width:100%;border-collapse:collapse}
thead{background:#F8FAFC}
th{text-align:left;padding:8px 10px;font-size:9px;font-weight:700;color:#64748B;border-bottom:2px solid #E2E8F0;cursor:pointer;white-space:nowrap;user-select:none;text-transform:uppercase;letter-spacing:.05em}
th:hover{color:#0D2D5C}
td{padding:7px 10px;border-bottom:1px solid #F1F5F9;color:#1E293B;vertical-align:middle}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover td{background:#F8FAFC}
.r-kmtc td{background:#F0FDF4!important}
.r-kmtc:hover td{background:#DCFCE7!important}

/* Badges */
.trade-tag{display:inline-block;padding:2px 7px;border-radius:3px;font-size:9px;font-weight:700}
.kmtc-mk{display:inline-block;background:#0D2D5C;color:#F0A500;font-size:8px;font-weight:800;padding:1px 5px;border-radius:3px;margin-left:4px;vertical-align:middle;border:1px solid #F0A500;letter-spacing:.04em}

/* Progress */
.prog-wrap{display:flex;align-items:center;gap:6px;min-width:80px}
.prog-bg{flex:1;background:#E2E8F0;border-radius:3px;height:5px;overflow:hidden}
.prog-fill{height:5px;border-radius:3px;background:#0D2D5C}
.prog-fill.g{background:#16A34A}
.prog-val{font-size:10px;font-weight:700;color:#0D2D5C;white-space:nowrap;min-width:28px}

/* Rotation chips */
.rot-port{display:inline-block;background:#EFF6FF;color:#1E3A8A;border:1px solid #BFDBFE;border-radius:3px;font-size:8px;padding:1px 5px;margin:1px 2px 1px 0;white-space:nowrap;font-weight:600}
.rot-port.busan{background:#FEF3C7;color:#92400E;border-color:#FCD34D;font-weight:800}

/* Section title */
.sec-ttl{font-size:11px;font-weight:700;color:#0D2D5C;margin-bottom:10px;display:flex;align-items:center;gap:8px}
.sec-badge{display:inline-block;padding:2px 10px;border-radius:3px;font-size:10px;font-weight:700;color:#fff;background:#0D2D5C;letter-spacing:.04em}
.sec-badge.g{background:#15803D}
.sec-badge.teal{background:#0F766E}

/* KMTC banner */
.kmtc-banner{background:linear-gradient(135deg,#064E3B 0%,#15803D 100%);border-radius:10px;padding:14px 20px;margin-bottom:14px;box-shadow:0 2px 8px rgba(0,0,0,.1)}
.kmtc-banner h2{color:#fff;font-size:14px;font-weight:700}
.kmtc-banner p{color:#A7F3D0;font-size:10px;margin-top:2px}

/* Pagination */
.pagination{display:flex;align-items:center;gap:8px;padding:10px 12px;font-size:11px;color:#475569;border-top:1px solid #F1F5F9}

/* Tab content wrapper */
.tab-inner{background:#fff;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.06);padding:20px;margin-bottom:16px}

/* Footer */
.footer{padding:14px 24px;text-align:center;font-size:10px;color:#94A3B8;border-top:1px solid #E2E8F0;margin-top:8px}

/* Size variants */
body.sz-s{font-size:11px}
body.sz-s .kpi-val{font-size:22px}
body.sz-s th,body.sz-s td{padding:5px 8px;font-size:9px}
body.sz-l{font-size:15px}
body.sz-l .kpi-val{font-size:34px}
body.sz-l th,body.sz-l td{padding:10px 12px;font-size:13px}

/* ===== DEST TAB ===== */
.dest-search-wrap{margin-bottom:12px}
.dest-search{width:100%;max-width:480px;padding:10px 14px;border:2px solid #CBD5E1;border-radius:8px;font-size:13px;font-family:inherit;outline:none;transition:border-color .15s}
.dest-search:focus{border-color:#0D2D5C}
.dest-chips{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:14px;max-height:200px;overflow-y:auto;padding:2px}
.dest-chip{display:inline-flex;align-items:center;gap:5px;padding:4px 11px;border-radius:99px;border:1.5px solid #CBD5E1;cursor:pointer;background:#fff;font-size:11px;font-weight:600;color:#475569;transition:all .12s;white-space:nowrap}
.dest-chip:hover{background:#F1F5F9;border-color:#94A3B8}
.dest-chip.active{background:#0D2D5C;border-color:#0D2D5C;color:#fff}
.dest-chip .cnt{background:#E2E8F0;color:#475569;border-radius:99px;padding:1px 6px;font-size:9px;font-weight:700;margin-left:2px}
.dest-chip.active .cnt{background:rgba(255,255,255,.25);color:#fff}
.dest-selected-header{background:#EFF6FF;border:1px solid #BFDBFE;border-radius:8px;padding:10px 14px;margin-bottom:12px;display:flex;align-items:center;gap:10px}
.dest-selected-port{font-size:15px;font-weight:800;color:#1E3A8A}
.dest-selected-meta{font-size:11px;color:#3B82F6;font-weight:600}

/* ===== MAP TAB ===== */
.map-panel-wrap{margin:-20px -24px;display:flex;height:calc(100vh - 250px);min-height:520px;border-top:1px solid #E2E8F0}
#leaflet-map{flex:1;height:100%;z-index:0}
.map-sidebar{width:360px;flex-shrink:0;background:#fff;border-left:1px solid #E2E8F0;display:flex;flex-direction:column;overflow:hidden}
.map-sidebar-hdr{padding:10px 14px;background:#0D2D5C;color:#fff;flex-shrink:0}
.map-sidebar-hdr h3{font-size:13px;font-weight:700}
.map-sidebar-hdr p{font-size:10px;color:#93C5FD;margin-top:2px}
.map-sidebar-body{flex:1;overflow-y:auto;padding:8px}
.map-svc-item{padding:8px 10px;border-radius:6px;margin-bottom:4px;cursor:pointer;border:1.5px solid #E2E8F0;background:#fff;transition:all .12s}
.map-svc-item:hover{background:#EEF2F7;border-color:#CBD5E1}
.map-svc-item.active{background:#EFF6FF;border-color:#3B82F6}
.map-svc-name{font-size:11px;font-weight:700;color:#0D2D5C;margin-bottom:2px}
.map-svc-op{font-size:10px;color:#64748B}
.map-svc-ships{font-size:10px;color:#0F766E;font-weight:600}
.map-hint{padding:40px 20px;text-align:center;color:#94A3B8;font-size:12px;line-height:1.8}
.map-hint-icon{font-size:32px;margin-bottom:8px}

/* Responsive */
@media(max-width:1100px){.kpi-row.col5{grid-template-columns:repeat(3,1fr)}.map-sidebar{width:280px}}
@media(max-width:700px){.kpi-row.col5,.kpi-row.col4{grid-template-columns:repeat(2,1fr)}.map-panel-wrap{flex-direction:column}.map-sidebar{width:100%;height:240px;border-left:none;border-top:1px solid #E2E8F0}}
"""

HTML_BODY = """
<!-- LOGIN -->
<div id="login-screen">
  <div class="login-card">
    <div class="login-kmtc-badge">KMTC</div>
    <div class="login-org">高麗海運ジャパン | 社員専用</div>
    <div class="login-title">BUSAN PORT SERVICE DASHBOARD<br><span style="font-size:11px;color:#94A3B8">KMTC Google アカウントでログインしてください</span></div>
    <div class="login-btn-area" id="g_id_signin"></div>
    <div id="login-error">
      <strong>アクセス拒否</strong> — @ekmtc.com アカウント専用です。<br>他ドメインではログインできません。
    </div>
    <div class="login-note">
      ※ ekmtc.com のGoogleアカウント専用<br>他ドメインではログインできません<br>BUSAN PORT SERVICE DASHBOARD — Confidential
    </div>
  </div>
</div>

<!-- DASHBOARD -->
<div id="dashboard">

<!-- Header -->
<div class="hdr">
  <div class="hdr-left">
    <div class="hdr-badge">KMTC</div>
    <div class="hdr-title">BUSAN PORT SERVICE DASHBOARD &nbsp;—&nbsp; 高麗海運ジャパン Confidential</div>
  </div>
  <div class="hdr-right">
    <div class="hdr-user" id="hdr-user"></div>
    <button class="hdr-logout" onclick="signOut()">ログアウト</button>
  </div>
</div>

<!-- Ctrl bar -->
<div class="ctrl-bar">
  <div class="tab-row">
    <button class="top-tab active" onclick="sw('ptop',this)">トップ</button>
    <button class="top-tab" onclick="sw('pdest',this)">仕向地別</button>
    <button class="top-tab" onclick="sw('pregion',this)">地域別</button>
    <button class="top-tab" onclick="sw('pcarrier',this)">船社別</button>
    <button class="top-tab" onclick="sw('pterminal',this)">ターミナル</button>
    <button class="top-tab tab-kmtc" onclick="sw('pkmtc',this)">★ KMTC特集</button>
    <button class="top-tab tab-map" onclick="sw('pmap',this)">🗺 マップ</button>
    <button class="top-tab" onclick="sw('plist',this)">全サービス一覧</button>
    <div class="tab-right">
      <span class="sz-label">文字</span>
      <button class="sz-btn" onclick="setSz('s',this)">小</button>
      <button class="sz-btn on" onclick="setSz('m',this)">中</button>
      <button class="sz-btn" onclick="setSz('l',this)">大</button>
    </div>
  </div>
  <div class="meta-row">
    <span>データ基準日: <strong>2026年5月1日</strong></span>
    <span>出所: <strong>BPA Container Services (As at 1 May 2026)</strong></span>
    <span>総サービス数: <strong>263件</strong></span>
  </div>
</div>

<!-- Filter bar -->
<div class="filter-bar" id="filter-bar">
  <span class="filter-label">地域</span>
  <div id="region-pills" style="display:flex;flex-wrap:wrap;gap:5px"></div>
  <span class="filter-label" style="margin-left:12px">船社</span>
  <select class="f-select" id="sel-carrier" onchange="applyFilters()"><option value="">全船社</option></select>
  <span class="filter-label">ターミナル</span>
  <select class="f-select" id="sel-terminal" onchange="applyFilters()"><option value="">全ターミナル</option></select>
  <span class="filter-label">船型</span>
  <select class="f-select" id="sel-teu" onchange="applyFilters()">
    <option value="">全サイズ</option>
    <option value="s">〜1,000 TEU</option>
    <option value="m">1,001〜2,000</option>
    <option value="l">2,001〜5,000</option>
    <option value="xl">5,001〜10,000</option>
    <option value="xxl">10,001 TEU〜</option>
  </select>
  <label class="f-toggle">
    <input type="checkbox" id="chk-kmtc" onchange="applyFilters()">KMTCのみ表示
  </label>
  <button class="pill" onclick="resetFilters()" style="margin-left:auto">✕ リセット</button>
</div>

<div class="main">

<!-- ===== TOP ===== -->
<div id="ptop" class="panel active">
  <div class="kpi-row col5" style="margin-bottom:16px">
    <div class="kpi-card navy"><div class="kpi-label">総サービス数（絞込後）</div><div class="kpi-val" id="kv-total">263</div><div class="kpi-sub">BUSANコンテナ定期航路</div></div>
    <div class="kpi-card teal"><div class="kpi-label">総投入隻数</div><div class="kpi-val" id="kv-ships">—</div><div class="kpi-sub">全サービス合計</div></div>
    <div class="kpi-card green"><div class="kpi-label">KMTCサービス</div><div class="kpi-val" id="kv-kmtc" style="color:#15803D">—</div><div class="kpi-sub">関与サービス数</div></div>
    <div class="kpi-card amber"><div class="kpi-label">カバー地域</div><div class="kpi-val" id="kv-regions" style="color:#D97706">—</div><div class="kpi-sub">Trade区分数</div></div>
    <div class="kpi-card purple"><div class="kpi-label">最大船型</div><div class="kpi-val" id="kv-maxteu" style="color:#7C3AED">—</div><div class="kpi-sub">TEU</div></div>
  </div>
  <div class="result-strip">
    <div id="result-count">表示中: <strong>263</strong> サービス（全263件中）</div>
    <div style="font-size:10px;color:#94A3B8">ヘッダークリックで並び替え　|　KMTCは緑色行</div>
  </div>
  <!-- Region summary table -->
  <div class="card" style="margin-bottom:14px">
    <div class="card-title"><span class="badge">地域別サマリー</span></div>
    <div class="tbl-wrap" style="margin-bottom:0">
      <table>
        <thead><tr><th>地域</th><th>サービス数</th><th style="min-width:100px">割合</th><th>投入隻数</th><th>KMTC</th><th>Alliance主要</th></tr></thead>
        <tbody id="top-region-tbody"></tbody>
      </table>
    </div>
  </div>
  <!-- Service table -->
  <div class="sec-ttl"><span class="sec-badge">サービス一覧</span><span style="font-size:10px;font-weight:400;color:#94A3B8">50件ずつ表示 / KMTCは緑色行</span></div>
  <div class="tbl-wrap">
    <table>
      <thead><tr>
        <th onclick="sortTop(0)">#</th>
        <th onclick="sortTop(1)">地域</th>
        <th onclick="sortTop(2)">セクター</th>
        <th onclick="sortTop(3)">Operators</th>
        <th onclick="sortTop(4)">サービス名</th>
        <th onclick="sortTop(5)">隻数×TEU</th>
        <th onclick="sortTop(6)">ターミナル</th>
        <th>Port Rotation</th>
        <th>本船名(TEU)</th>
      </tr></thead>
      <tbody id="top-tbody"></tbody>
    </table>
    <div id="top-pagination"></div>
  </div>
</div><!-- /ptop -->

<!-- ===== DEST ===== -->
<div id="pdest" class="panel">
  <div class="tab-inner">
    <div class="sec-ttl"><span class="sec-badge teal">仕向地別サービス検索</span><span style="font-size:10px;font-weight:400;color:#94A3B8;margin-left:8px">Port Rotationから仕向地港を選択してサービスを絞り込み</span></div>
    <div class="dest-search-wrap">
      <input type="text" id="dest-search" class="dest-search" placeholder="港名で絞り込み（例: Shanghai, Yokohama）" oninput="filterDestChips()">
    </div>
    <div class="dest-chips" id="dest-chips"></div>
    <div id="dest-result"></div>
  </div>
</div>

<!-- ===== REGION ===== -->
<div id="pregion" class="panel">
  <div class="tab-inner">
    <div class="sec-ttl"><span class="sec-badge">地域別詳細</span></div>
    <div id="region-tables"></div>
  </div>
</div>

<!-- ===== CARRIER ===== -->
<div id="pcarrier" class="panel">
  <div class="tab-inner">
    <div class="sec-ttl"><span class="sec-badge">船社・Alliance別分析</span></div>
    <div class="g2e" style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px" id="carrier-summary"></div>
    <div id="carrier-tbl"></div>
  </div>
</div>

<!-- ===== TERMINAL ===== -->
<div id="pterminal" class="panel">
  <div class="tab-inner">
    <div class="sec-ttl"><span class="sec-badge">BUSANターミナル別分析</span></div>
    <div id="terminal-tbl"></div>
  </div>
</div>

<!-- ===== KMTC ===== -->
<div id="pkmtc" class="panel">
  <div class="kmtc-banner">
    <h2>★ KMTC 投入サービス特集 — 2026年5月</h2>
    <p>高麗海運（KMTC）が運航・共同配船するBUSAN発着全サービス一覧</p>
  </div>
  <div class="kpi-row col4" style="margin-bottom:16px">
    <div class="kpi-card green"><div class="kpi-label">KMTC関与サービス数</div><div class="kpi-val" id="kk-total" style="color:#15803D">—</div><div class="kpi-sub">全263件中</div></div>
    <div class="kpi-card green"><div class="kpi-label">KMTC投入隻数</div><div class="kpi-val" id="kk-ships" style="color:#15803D">—</div><div class="kpi-sub">全航路合計</div></div>
    <div class="kpi-card green"><div class="kpi-label">展開地域数</div><div class="kpi-val" id="kk-regions" style="color:#15803D">—</div><div class="kpi-sub">Trade区分</div></div>
    <div class="kpi-card green"><div class="kpi-label">最大投入船型</div><div class="kpi-val" id="kk-maxteu" style="color:#15803D">—</div><div class="kpi-sub">TEU</div></div>
  </div>
  <!-- KMTC region summary -->
  <div class="card" style="margin-bottom:14px">
    <div class="card-title"><span class="badge badge-g">地域別 KMTC展開状況</span></div>
    <div class="tbl-wrap" style="margin-bottom:0"><table>
      <thead><tr><th>地域</th><th>KMTC便数</th><th style="min-width:100px">割合</th><th>投入隻数</th><th>主なサービス</th></tr></thead>
      <tbody id="kmtc-region-tbody"></tbody>
    </table></div>
  </div>
  <div class="sec-ttl"><span class="sec-badge g">KMTC全サービス一覧</span><span id="kmtc-count-label" style="font-size:10px;font-weight:400;color:#64748B;margin-left:8px"></span></div>
  <div class="tbl-wrap">
    <table>
      <thead><tr><th>地域</th><th>セクター</th><th>Alliance</th><th>サービス名</th><th>隻数×TEU</th><th>港</th><th>ターミナル</th><th>Port Rotation</th><th>本船名</th></tr></thead>
      <tbody id="kmtc-tbody"></tbody>
    </table>
  </div>
</div>

<!-- ===== MAP ===== -->
<div id="pmap" class="panel">
  <div class="map-panel-wrap">
    <div id="leaflet-map"></div>
    <div class="map-sidebar">
      <div class="map-sidebar-hdr">
        <h3 id="map-sidebar-title">港を選択してください</h3>
        <p id="map-sidebar-sub">地図上の港マーカーをクリック</p>
      </div>
      <div class="map-sidebar-body" id="map-sidebar-body">
        <div class="map-hint">
          <div class="map-hint-icon">🗺</div>
          地図上の港マーカーをクリックすると<br>その港に寄港するサービス一覧が表示されます。<br><br>
          サービスをクリックすると<br>航路ルートが地図上に描画されます。
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ===== LIST ===== -->
<div id="plist" class="panel">
  <div class="tab-inner">
    <div class="sec-ttl"><span class="sec-badge">全サービス一覧（263件）</span><span style="font-size:10px;font-weight:400;color:#94A3B8;margin-left:8px">KMTCは緑色行</span></div>
    <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:12px">
      <input type="text" id="list-search" placeholder="サービス名・船社・Port Rotationで検索..." style="padding:6px 12px;border:1.5px solid #CBD5E1;border-radius:6px;font-size:12px;font-family:inherit;min-width:260px;outline:none" oninput="renderList()">
      <select class="f-select" id="list-trade" onchange="renderList()"><option value="">全地域</option></select>
      <select class="f-select" id="list-op" onchange="renderList()"><option value="">全船社</option></select>
      <label class="f-toggle"><input type="checkbox" id="list-kmtc" onchange="renderList()"> KMTCのみ</label>
    </div>
    <div class="result-strip" id="list-count">表示中: <strong>263</strong> サービス</div>
    <div class="tbl-wrap">
      <table>
        <thead><tr>
          <th onclick="sortList(0)">#</th>
          <th onclick="sortList(1)">地域</th>
          <th onclick="sortList(2)">セクター</th>
          <th onclick="sortList(3)">Alliance</th>
          <th onclick="sortList(4)">Operators</th>
          <th onclick="sortList(5)">サービス名</th>
          <th onclick="sortList(6)">隻数×TEU</th>
          <th onclick="sortList(7)">ターミナル</th>
          <th>Port Rotation</th>
          <th>本船名</th>
          <th onclick="sortList(10)">コード</th>
        </tr></thead>
        <tbody id="list-tbody"></tbody>
      </table>
    </div>
    <div id="list-pagination"></div>
  </div>
</div>

</div><!-- /main -->
<div class="footer">高麗海運ジャパン株式会社 マーケティング部 ｜ BUSAN PORT SERVICE DASHBOARD ｜ CONFIDENTIAL — 社内限定資料 ｜ BPA Container Services (As at 1 May 2026)</div>
</div><!-- /dashboard -->
"""

JS = r"""
const ALLOWED='ekmtc.com';
const GID='350154605838-45pq8e4l2thucrq79hjp1o8pdqiefquq.apps.googleusercontent.com';

window.onload=function(){
  const u=sessionStorage.getItem('bpa_u');
  if(u){showDB(u);return;}
  const t=setInterval(()=>{if(window.google){clearInterval(t);initGSI();}},300);
  setTimeout(()=>clearInterval(t),8000);
};
function initGSI(){
  google.accounts.id.initialize({client_id:GID,callback:onCred,auto_select:false});
  google.accounts.id.renderButton(document.getElementById('g_id_signin'),{theme:'outline',size:'large',text:'signin_with',shape:'rectangular',width:300,locale:'ja'});
  google.accounts.id.prompt();
}
function onCred(r){
  try{
    const p=JSON.parse(atob(r.credential.split('.')[1]));
    if((p.email||'').endsWith('@'+ALLOWED)){
      sessionStorage.setItem('bpa_u',p.email);
      sessionStorage.setItem('bpa_n',p.name||p.email);
      document.getElementById('login-error').style.display='none';
      showDB(p.email);
    }else{document.getElementById('login-error').style.display='block';}
  }catch(e){document.getElementById('login-error').style.display='block';}
}
function showDB(email){
  document.getElementById('login-screen').style.display='none';
  document.getElementById('dashboard').style.display='block';
  document.getElementById('hdr-user').textContent=(sessionStorage.getItem('bpa_n')||email)+' — JP TYO';
  initDB();
}
function signOut(){sessionStorage.removeItem('bpa_u');sessionStorage.removeItem('bpa_n');if(window.google)google.accounts.id.disableAutoSelect();location.reload();}

/* DATA */
const DATA=__DATA__;

const TL={China:'中国',Japan:'日本','SE Asia':'東南アジア',USWC:'北米西岸',USEC:'北米東岸',WCSA:'南米西岸',ECSA:'南米東岸','Russia Far East':'ロシア極東',Oceania:'オセアニア',ISC:'インド亜大陸',Med:'地中海','N. Europe':'北欧州',ME:'中近東','E Africa':'東アフリカ','West Africa':'西アフリカ'};
const TC={China:'#3B82F6',Japan:'#1D4ED8','SE Asia':'#0F766E',USWC:'#D97706',USEC:'#F59E0B',WCSA:'#DC2626',ECSA:'#B91C1C','Russia Far East':'#7C3AED',Oceania:'#0891B2',ISC:'#DB2777',Med:'#059669','N. Europe':'#065F46',ME:'#92400E','E Africa':'#374151','West Africa':'#6B7280'};

let aReg='',tSC=0,tSA=true,lSC=0,lSA=true,tPage=0,lPage=0,tFiltered=[],lFiltered=[];
const PAGE=50;
const tabInit={};
let leafletMap=null,routeLayer=null,portMarkers={};
let PIDX={};   // port -> [services]
let destPort='';

/* PORT COORDINATES */
const PORT_COORDS={
  'Shanghai':[31.23,121.47],'Ningbo':[29.87,121.55],'Qingdao':[36.07,120.37],
  'Xingang':[39.00,117.72],'Tianjin':[39.00,117.72],'Shekou':[22.49,113.91],
  'Yantian':[22.58,114.27],'Chiwan':[22.47,113.88],'Xiamen':[24.48,118.09],
  'Dalian':[38.91,121.64],'Nansha':[22.74,113.59],'Guangzhou':[23.13,113.26],
  'Lianyungang':[34.73,119.22],'Rizhao':[35.38,119.52],'Taicang':[31.45,121.10],
  'Nantong':[32.02,120.87],'Huangpu':[23.10,113.43],'Zhongshan':[22.52,113.39],
  'Zhuhai':[22.27,113.57],'Shenzhen':[22.54,114.06],'Zhoushan':[30.00,122.11],
  'Fuzhou':[26.06,119.31],'Quanzhou':[24.88,118.68],'Fangchenggang':[21.61,108.35],
  'Beihai':[21.48,109.12],'Qinzhou':[21.95,108.60],'Zhanjiang':[21.27,110.40],
  'Lanshan':[35.07,119.35],'Weihai':[37.51,122.12],'Yantai':[37.55,121.39],
  'Jinzhou':[41.11,121.12],'Yingkou':[40.67,122.22],'Huizhou':[22.71,114.42],
  'Zhangzhou':[24.51,117.65],'Nanjing':[32.06,118.79],'Wuhan':[30.59,114.30],
  'Kwangyang':[34.93,127.68],'Incheon':[37.46,126.71],'Ulsan':[35.54,129.39],
  'Busan':[35.10,129.04],'Masan':[35.19,128.57],'Pyeongtaek':[36.96,127.06],
  'Gunsan':[35.98,126.71],'Pohang':[36.01,129.36],'Onsan':[35.45,129.35],
  'Tokyo':[35.63,139.80],'Yokohama':[35.44,139.64],'Nagoya':[35.08,136.88],
  'Osaka':[34.65,135.43],'Kobe':[34.68,135.19],'Hakata':[33.60,130.37],
  'Shimizu':[35.01,138.52],'Moji':[33.94,130.97],'Niigata':[37.94,139.04],
  'Sendai':[38.27,141.02],'Naha':[26.21,127.67],'Kitakyushu':[33.88,130.88],
  'Tomakomai':[42.63,141.61],'Kanazawa':[36.62,136.63],'Takamatsu':[34.35,134.04],
  'Tokushima':[34.07,134.56],'Matsuyama':[33.84,132.77],'Hiroshima':[34.36,132.44],
  'Muroran':[42.32,140.99],'Sakai':[34.58,135.47],'Ube':[33.94,131.25],
  'Karatsu':[33.44,129.97],'Sakaide':[34.32,133.84],'Fukuyama':[34.47,133.37],
  'Oita':[33.24,131.61],'Kagoshima':[31.56,130.56],'Osaka/Kobe':[34.65,135.35],
  'Iwakuni':[34.17,132.17],'Nachikatsuura':[33.63,135.93],'Anan':[33.90,134.66],
  'Singapore':[1.29,103.85],'Port Klang':[3.00,101.40],'Penang':[5.42,100.34],
  'Laem Chabang':[13.09,100.89],'Bangkok':[13.75,100.52],
  'Ho Chi Minh City':[10.77,106.69],'HCMC':[10.77,106.69],
  'Haiphong':[20.86,106.68],'Hai Phong':[20.86,106.68],
  'Cai Mep':[10.53,107.00],'Cat Lai':[10.77,106.73],
  'Da Nang':[16.07,108.22],'Danang':[16.07,108.22],'Quy Nhon':[13.78,109.22],
  'Cai Lan':[20.97,107.07],'Cam Pha':[21.01,107.34],
  'Manila':[14.59,120.97],'Subic Bay':[14.80,120.27],'Cebu':[10.31,123.89],
  'Davao':[7.07,125.61],'Batangas':[13.75,121.05],'Iloilo':[10.70,122.56],
  'Jakarta':[-6.11,106.88],'Tanjung Priok':[-6.11,106.88],
  'Surabaya':[-7.26,112.74],'Belawan':[3.78,98.69],'Semarang':[-7.00,110.42],
  'Makassar':[-5.15,119.43],'Bitung':[1.45,125.19],'Banjarmasin':[-3.33,114.59],
  'Port Dickson':[2.52,101.80],'Johor':[1.46,103.70],'Pasir Gudang':[1.47,103.89],
  'Tanjung Pelepas':[1.36,103.55],'Klang':[3.00,101.40],'Kelang':[3.00,101.40],
  'Yangon':[16.77,96.16],'Thilawa':[16.62,96.23],'Sihanoukville':[10.63,103.50],
  'Long Beach':[33.77,-118.22],'Los Angeles':[33.73,-118.26],
  'Seattle':[47.60,-122.34],'Tacoma':[47.27,-122.41],'Oakland':[37.80,-122.27],
  'Vancouver':[49.29,-123.11],'Prince Rupert':[54.31,-130.32],
  'Savannah':[32.08,-81.10],'Norfolk':[36.85,-76.30],'New York':[40.66,-74.00],
  'Baltimore':[39.27,-76.61],'Charleston':[32.78,-79.94],'Jacksonville':[30.33,-81.66],
  'Houston':[29.73,-95.27],'New Orleans':[29.94,-90.09],'Miami':[25.77,-80.19],
  'Philadelphia':[39.95,-75.14],'Boston':[42.35,-71.05],'Montreal':[45.51,-73.55],
  'Manzanillo':[19.05,-104.32],
  'Callao':[-12.05,-77.14],'Buenaventura':[3.88,-77.00],'Guayaquil':[-2.24,-79.88],
  'Iquique':[-20.21,-70.15],'Valparaiso':[-33.04,-71.63],'San Antonio':[-33.60,-71.61],
  'Arica':[-18.48,-70.33],'Paita':[-5.09,-81.11],
  'Santos':[-23.94,-46.33],'Buenos Aires':[-34.61,-58.37],
  'Paranagua':[-25.52,-48.51],'Rio de Janeiro':[-22.90,-43.18],
  'Itajai':[-26.91,-48.66],'Montevideo':[-34.91,-56.21],
  'Navegantes':[-26.90,-48.65],'Itaguai':[-22.87,-43.79],
  'Manaus':[-3.10,-60.03],'Belem':[-1.46,-48.50],'Fortaleza':[-3.72,-38.52],
  'Pecem':[-3.53,-38.82],'Suape':[-8.41,-34.96],'Rio Grande':[-32.04,-52.10],
  'Rotterdam':[51.95,4.14],'Hamburg':[53.54,9.99],'Antwerp':[51.22,4.40],
  'Felixstowe':[51.96,1.34],'Le Havre':[49.49,0.11],'Bremerhaven':[53.55,8.58],
  'Gothenburg':[57.69,11.97],'Gdansk':[54.37,18.66],'Gdynia':[54.53,18.55],
  'Aarhus':[56.16,10.20],'Southampton':[50.90,-1.39],'Zeebrugge':[51.34,3.20],
  'Koper':[45.55,13.73],'Genoa':[44.41,8.93],'Barcelona':[41.38,2.18],
  'Valencia':[39.45,-0.33],'Algeciras':[36.14,-5.45],'Piraeus':[37.95,23.62],
  'Istanbul':[41.01,28.96],'Constanta':[44.18,28.65],'Ust-Luga':[59.67,28.45],
  'Klaipeda':[55.71,21.13],'Tallinn':[59.44,24.75],'Riga':[56.95,24.11],
  'Oslo':[59.91,10.75],'Helsinki':[60.17,24.94],'Copenhagen':[55.68,12.57],
  'Dunkirk':[51.04,2.36],'Amsterdam':[52.39,4.91],
  'Marseille':[43.30,5.37],'Fos':[43.44,4.89],'Naples':[40.85,14.27],
  'Taranto':[40.47,17.24],'Gioia Tauro':[38.43,15.90],'Livorno':[43.55,10.31],
  'Leghorn':[43.55,10.31],'Venice':[45.44,12.32],'Ravenna':[44.41,12.20],
  'Thessaloniki':[40.64,22.94],'Damietta':[31.41,31.81],'Port Said':[31.26,32.30],
  'Alexandria':[31.20,29.92],'Malta':[35.90,14.51],'Limassol':[34.67,33.05],
  'Mersin':[36.79,34.63],'Gemlik':[40.43,29.17],'Izmir':[38.43,27.14],
  'Ambarli':[40.97,28.70],'Lattakia':[35.52,35.78],'Haifa':[32.82,34.99],
  'Ashdod':[31.80,34.64],'Beirut':[33.88,35.50],'Aqaba':[29.52,35.00],
  'Jeddah':[21.49,39.17],'Salalah':[17.02,54.07],'Colombo':[6.95,79.85],
  'Dubai':[25.27,55.30],'Abu Dhabi':[24.47,54.37],'Sharjah':[25.36,55.38],
  'Muscat':[23.61,58.59],'Kuwait':[29.37,47.97],'Bahrain':[26.22,50.59],
  'Dammam':[26.43,50.10],'Jubail':[27.01,49.66],'Bandar Abbas':[27.18,56.28],
  'Sohar':[24.36,56.69],'Khorfakkan':[25.34,56.36],'Khor Fakkan':[25.34,56.36],
  'Hamad':[24.98,51.59],'Doha':[25.29,51.53],'Oman':[23.61,58.59],
  'Um Qasr':[30.00,47.93],'Basra':[30.52,47.81],'Bushehr':[28.99,50.83],
  'Nhava Sheva':[18.95,72.95],'Mumbai':[18.95,72.82],'Chennai':[13.10,80.29],
  'Tuticorin':[8.77,78.14],'Cochin':[9.97,76.26],'Kolkata':[22.56,88.34],
  'Haldia':[22.03,88.06],'Visakhapatnam':[17.69,83.28],'Hazira':[21.09,72.64],
  'Pipavav':[20.91,71.53],'Krishnapatnam':[14.26,80.12],'Kandla':[23.00,70.22],
  'Mangalore':[12.87,74.84],'Mundra':[22.84,69.72],'Port Qasim':[24.82,67.32],
  'Karachi':[24.86,66.99],'Chittagong':[22.34,91.83],'Mongla':[22.47,89.60],
  'Kaohsiung':[22.62,120.30],'Keelung':[25.13,121.74],'Taichung':[24.27,120.52],
  'Hong Kong':[22.31,114.17],'Kwai Chung':[22.37,114.12],
  'Sydney':[-33.87,151.21],'Melbourne':[-37.82,144.93],'Brisbane':[-27.47,153.03],
  'Fremantle':[-32.05,115.74],'Adelaide':[-34.85,138.60],
  'Auckland':[-36.84,174.77],'Port Kembla':[-34.47,150.90],
  'Lyttelton':[-43.60,172.72],'Wellington':[-41.28,174.78],'Tauranga':[-37.66,176.17],
  'Mombasa':[-4.05,39.66],'Dar es Salaam':[-6.82,39.29],'Djibouti':[11.60,43.14],
  'Aden':[12.78,45.03],'Port Sudan':[19.62,37.22],
  'Lagos':[6.45,3.41],'Abidjan':[5.35,-4.00],'Tema':[5.63,-0.02],
  'Dakar':[14.69,-17.44],'Lome':[6.14,1.22],'Cotonou':[6.36,2.43],
  'Douala':[4.05,9.70],'Luanda':[-8.83,13.23],'Pointe Noire':[-4.77,11.86],
  'Durban':[-29.87,31.03],'Toamasina':[-18.15,49.40],
  'Nacala':[-14.54,40.67],'Beira':[-19.83,34.84],
  'Vladivostok':[43.12,131.89],'Vostochny':[42.77,133.08],'Vostochy':[42.77,133.08],
  'Nakhodka':[42.82,132.89],'Zarubino':[42.65,130.77],
  'Kingston':[17.99,-76.79],'Caucedo':[18.44,-69.61],'Cartagena':[10.40,-75.52],
  'Panama':[8.99,-79.52],'Colon':[9.36,-79.90],'Balboa':[8.96,-79.57],
  'Puerto Cortes':[15.84,-87.95],'Altamira':[22.40,-97.92],
  'Veracruz':[19.19,-96.14],'Lazaro Cardenas':[17.91,-102.17],
  'Ensenada':[31.86,-116.61],'Port of Spain':[10.65,-61.52],
  'Imbituba':[-28.24,-48.67],'Itaguai':[-22.87,-43.79],
  'San Vicente':[-36.76,-73.13],'Coronel':[-37.02,-73.14],
  'Antofagasta':[-23.65,-70.40],'Mejillones':[-23.10,-70.46],
  'Matarani':[-17.00,-72.11]
};

function getCoords(p){
  if(PORT_COORDS[p])return PORT_COORDS[p];
  const lo=p.toLowerCase();
  for(const[k,v]of Object.entries(PORT_COORDS)){if(k.toLowerCase()===lo)return v;}
  return null;
}

const BUSAN_SET=new Set(['Busan','Busan New Port','Busan North Port','BUSAN','Busan (New Port)','Busan (North Port)','BNCT','Gamman','Sinseondae','Hutchison','PNC','HPNT','BPTS','BCE']);

function buildPortIndex(){
  PIDX={};
  DATA.forEach(d=>{
    if(!d.rotation)return;
    d.rotation.split(',').forEach(p=>{
      p=p.trim();
      if(!p)return;
      const isB=BUSAN_SET.has(p)||p.toLowerCase().startsWith('busan');
      if(isB)return;
      if(!PIDX[p])PIDX[p]=[];
      PIDX[p].push(d);
    });
  });
}

function initDB(){
  if(tabInit._b)return; tabInit._b=true;
  buildPortIndex();
  buildFilters();
  applyFilters();
}

function buildFilters(){
  const trades=[...new Set(DATA.map(d=>d.trade))].sort();
  const rp=document.getElementById('region-pills');
  const ap=mkBtn('全地域','',true); ap.onclick=()=>setReg('',ap); rp.appendChild(ap);
  trades.forEach(t=>{
    const b=mkBtn((TL[t]||t)+'('+DATA.filter(d=>d.trade===t).length+')',t,false);
    b.onclick=()=>setReg(t,b); rp.appendChild(b);
  });
  const ops=[...new Set(DATA.map(d=>d.operators))].filter(Boolean).sort();
  const sc=document.getElementById('sel-carrier'),lo=document.getElementById('list-op');
  ops.forEach(o=>{addO(sc,o,o);addO(lo,o,o);});
  const terms=[...new Set(DATA.map(d=>d.terminal))].filter(Boolean).sort();
  terms.forEach(t=>addO(document.getElementById('sel-terminal'),t,t));
  const lt=document.getElementById('list-trade');
  trades.forEach(t=>addO(lt,t,TL[t]||t));
}
function mkBtn(label,val,active){
  const b=document.createElement('button');
  b.className='pill'+(active?' on':''); b.textContent=label; b.dataset.val=val; return b;
}
function addO(sel,val,txt){const o=document.createElement('option');o.value=val;o.textContent=txt;sel.appendChild(o);}

function setReg(val,btn){
  aReg=val;
  document.querySelectorAll('#region-pills .pill').forEach(b=>b.className='pill'+(b.dataset.val===val?' on':''));
  applyFilters();
}
function resetFilters(){
  aReg='';
  document.querySelectorAll('#region-pills .pill').forEach(b=>b.className='pill'+(b.dataset.val===''?' on':''));
  ['sel-carrier','sel-terminal','sel-teu'].forEach(id=>document.getElementById(id).value='');
  document.getElementById('chk-kmtc').checked=false;
  applyFilters();
}

function getF(){
  const carrier=document.getElementById('sel-carrier').value;
  const terminal=document.getElementById('sel-terminal').value;
  const teu=document.getElementById('sel-teu').value;
  const kmtc=document.getElementById('chk-kmtc').checked;
  return DATA.filter(d=>{
    if(aReg&&d.trade!==aReg)return false;
    if(carrier&&d.operators!==carrier)return false;
    if(terminal&&!d.terminal.includes(terminal))return false;
    if(kmtc&&!d.is_kmtc)return false;
    if(teu){const t=d.teu_size;
      if(teu==='s'&&t>1000)return false;
      if(teu==='m'&&(t<1001||t>2000))return false;
      if(teu==='l'&&(t<2001||t>5000))return false;
      if(teu==='xl'&&(t<5001||t>10000))return false;
      if(teu==='xxl'&&t<10001)return false;}
    return true;
  });
}

function applyFilters(){
  const f=getF();
  const ships=f.reduce((s,d)=>s+d.num_ships,0);
  const kn=f.filter(d=>d.is_kmtc).length;
  const rg=new Set(f.map(d=>d.trade)).size;
  const mx=f.length?Math.max(...f.map(d=>d.teu_size)):0;
  $('kv-total').textContent=f.length.toLocaleString();
  $('kv-ships').textContent=ships.toLocaleString();
  $('kv-kmtc').textContent=kn;
  $('kv-regions').textContent=rg;
  $('kv-maxteu').textContent=mx.toLocaleString();
  $('result-count').innerHTML='表示中: <strong>'+f.length+'</strong> サービス（全263件中）';
  renderTopRegionTable(f);
  tPage=0; renderTopTable(f);
}
function $(id){return document.getElementById(id);}

/* TOP region table */
function renderTopRegionTable(data){
  const trc={},trsh={},trk={},tral={};
  const maxC=Math.max(...[...new Set(data.map(d=>d.trade))].map(t=>data.filter(d2=>d2.trade===t).length),1);
  data.forEach(d=>{
    trc[d.trade]=(trc[d.trade]||0)+1;
    trsh[d.trade]=(trsh[d.trade]||0)+d.num_ships;
    if(d.is_kmtc)trk[d.trade]=(trk[d.trade]||0)+1;
    if(!tral[d.trade])tral[d.trade]={};
    if(d.alliance)tral[d.trade][d.alliance]=(tral[d.trade][d.alliance]||0)+1;
  });
  const K=Object.keys(trc).sort((a,b)=>trc[b]-trc[a]);
  const mx=Math.max(...Object.values(trc),1);
  $('top-region-tbody').innerHTML=K.map(tr=>{
    const topAl=Object.entries(tral[tr]||{}).sort((a,b)=>b[1]-a[1]).slice(0,3).map(([k])=>k).join(', ');
    const pct=Math.round(trc[tr]/mx*100);
    return`<tr>
      <td><span class="trade-tag" style="background:${TC[tr]||'#94A3B8'}22;color:${TC[tr]||'#334155'}">${TL[tr]||tr}</span></td>
      <td style="font-weight:700;color:#0D2D5C">${trc[tr]}</td>
      <td><div class="prog-wrap"><div class="prog-bg"><div class="prog-fill" style="width:${pct}%"></div></div><span class="prog-val">${trc[tr]}</span></div></td>
      <td>${trsh[tr]||0}</td>
      <td>${trk[tr]?`<span style="color:#15803D;font-weight:700">${trk[tr]}</span>`:'-'}</td>
      <td style="font-size:10px;color:#64748B">${topAl||'-'}</td>
    </tr>`;
  }).join('');
}

/* TOP TABLE */
function ttag(trade){return'<span class="trade-tag" style="background:'+(TC[trade]||'#94A3B8')+'22;color:'+(TC[trade]||'#334155')+'">'+(TL[trade]||trade)+'</span>';}
function makeRot(rot){if(!rot)return'';return rot.split(',').map(p=>{p=p.trim();const b=p.toLowerCase().includes('busan');return'<span class="rot-port'+(b?' busan':'')+'">'+p+'</span>';}).join('');}
function progBar(val,max,cls=''){const pct=max>0?Math.round(val/max*100):0;return'<div class="prog-wrap"><div class="prog-bg"><div class="prog-fill'+cls+'" style="width:'+pct+'%"></div></div><span class="prog-val">'+val+'</span></div>';}

function sortTop(c){if(tSC===c)tSA=!tSA;else{tSC=c;tSA=true;}tPage=0;renderTopTable(getF());}
function renderTopTable(data){
  const K=['no','trade','sector','alliance','service','ships_raw','terminal','rotation','ship_details'];
  tFiltered=[...data].sort((a,b)=>{let va=a[K[tSC]]||'',vb=b[K[tSC]]||'';return typeof va==='number'?(tSA?va-vb:vb-va):(tSA?String(va).localeCompare(String(vb)):String(vb).localeCompare(String(va)));});
  renderTopPage();
}
function renderTopPage(){
  const s=tPage*PAGE,e=Math.min(s+PAGE,tFiltered.length),sl=tFiltered.slice(s,e);
  $('top-tbody').innerHTML=sl.map(d=>`<tr class="${d.is_kmtc?'r-kmtc':''}">
    <td style="color:#CBD5E1;font-size:9px">${d.no}</td>
    <td>${ttag(d.trade)}</td>
    <td style="font-size:10px;color:#64748B">${d.sector}</td>
    <td style="font-weight:${d.is_kmtc?700:400};font-size:11px">${d.operators}${d.is_kmtc?'<span class="kmtc-mk">KMTC</span>':''}</td>
    <td style="font-size:11px">${d.service}</td>
    <td style="font-weight:700;color:#0D2D5C;white-space:nowrap">${d.ships_raw}</td>
    <td style="font-size:10px;font-weight:600">${d.terminal}</td>
    <td style="font-size:10px;color:#475569">${d.rotation||''}</td>
    <td style="font-size:9px;color:#94A3B8">${d.ship_details||''}</td>
  </tr>`).join('');
  const total=tFiltered.length,pages=Math.ceil(total/PAGE);
  $('top-pagination').innerHTML=pages<=1?'':
    `<div class="pagination">
      <button class="pill${tPage===0?' on':''}" onclick="goTP(0)">最初</button>
      <button class="pill" onclick="goTP(Math.max(0,tPage-1))"${tPage===0?' disabled':''}>◀</button>
      <span><strong>${s+1}〜${e}</strong> / ${total}件</span>
      <button class="pill" onclick="goTP(Math.min(${pages-1},tPage+1))"${tPage>=pages-1?' disabled':''}>▶</button>
      <button class="pill${tPage===pages-1?' on':''}" onclick="goTP(${pages-1})">最後</button>
    </div>`;
}
function goTP(p){tPage=p;renderTopPage();}

/* DEST TAB */
function renderDest(){
  const portsSorted=Object.entries(PIDX).sort((a,b)=>b[1].length-a[1].length);
  const chips=$('dest-chips');
  chips.innerHTML='';
  portsSorted.forEach(([port,svcs])=>{
    const c=document.createElement('button');
    c.className='dest-chip'+(destPort===port?' active':'');
    c.dataset.port=port;
    c.innerHTML=port+'<span class="cnt">'+svcs.length+'</span>';
    c.onclick=()=>selectDestPort(port);
    chips.appendChild(c);
  });
  if(destPort)renderDestResult(destPort);
}

function filterDestChips(){
  const q=($('dest-search').value||'').toLowerCase().trim();
  document.querySelectorAll('.dest-chip').forEach(c=>{
    const port=c.dataset.port||'';
    c.style.display=(!q||port.toLowerCase().includes(q))?'':'none';
  });
}

function selectDestPort(port){
  destPort=port;
  document.querySelectorAll('.dest-chip').forEach(c=>{
    c.className='dest-chip'+(c.dataset.port===port?' active':'');
  });
  renderDestResult(port);
}

let dSC=0,dSA=true;
function sortDest(c){if(dSC===c)dSA=!dSA;else{dSC=c;dSA=true;}renderDestResult(destPort);}

function renderDestResult(port){
  const svcs=PIDX[port]||[];
  if(!svcs.length){$('dest-result').innerHTML='<div style="color:#94A3B8;padding:20px">データなし</div>';return;}
  const K=['trade','operators','alliance','service','ships_raw','num_ships','rotation','terminal'];
  const sorted=[...svcs].sort((a,b)=>{
    let va=a[K[dSC]]||'',vb=b[K[dSC]]||'';
    return typeof va==='number'?(dSA?va-vb:vb-va):(dSA?String(va).localeCompare(String(vb)):String(vb).localeCompare(String(va)));
  });
  const kmtcN=svcs.filter(d=>d.is_kmtc).length;
  const html=`
    <div class="dest-selected-header">
      <div>
        <div class="dest-selected-port">${port}</div>
        <div class="dest-selected-meta">週 <strong>${svcs.length}</strong> 便 ｜ ${kmtcN?`うちKMTC <strong>${kmtcN}</strong> 便 ｜`:''} 船社 <strong>${new Set(svcs.map(d=>d.operators)).size}</strong> 社</div>
      </div>
      <button class="pill" onclick="showPortOnMap('${port.replace(/'/g,"\\'")}')">🗺 地図で見る</button>
    </div>
    <div class="tbl-wrap">
      <table>
        <thead><tr>
          <th onclick="sortDest(0)">地域</th>
          <th onclick="sortDest(1)">船社</th>
          <th onclick="sortDest(2)">Alliance</th>
          <th onclick="sortDest(3)">サービス名</th>
          <th onclick="sortDest(4)">隻数×TEU</th>
          <th>週便数</th>
          <th onclick="sortDest(6)">Port Rotation</th>
          <th onclick="sortDest(7)">BUSANターミナル</th>
        </tr></thead>
        <tbody>
          ${sorted.map(d=>`<tr class="${d.is_kmtc?'r-kmtc':''}">
            <td>${ttag(d.trade)}</td>
            <td style="font-weight:${d.is_kmtc?700:400};font-size:11px">${d.operators}${d.is_kmtc?'<span class="kmtc-mk">KMTC</span>':''}</td>
            <td style="font-size:10px">${d.alliance}</td>
            <td style="font-size:11px">${d.service}</td>
            <td style="font-weight:700;color:#0D2D5C;white-space:nowrap">${d.ships_raw}</td>
            <td style="font-weight:700;color:#0F766E">週1便</td>
            <td>${makeRot(d.rotation)}</td>
            <td style="font-size:10px;font-weight:600">${d.terminal}</td>
          </tr>`).join('')}
        </tbody>
      </table>
    </div>`;
  $('dest-result').innerHTML=html;
}

function showPortOnMap(port){
  const btn=document.querySelector('.top-tab.tab-map');
  sw('pmap',btn);
  setTimeout(()=>{
    if(portMarkers[port]){
      portMarkers[port].fire('click');
      leafletMap.setView(portMarkers[port].getLatLng(),5);
    }
  },400);
}

/* REGION TAB */
function renderRegion(){
  const trc={};
  DATA.forEach(d=>{trc[d.trade]=(trc[d.trade]||0)+1;});
  const K=Object.keys(trc).sort((a,b)=>trc[b]-trc[a]);
  const maxS=Math.max(...K.map(k=>trc[k]));
  let html='';
  K.forEach(tr=>{
    const svcs=DATA.filter(d=>d.trade===tr);
    const ks=svcs.filter(d=>d.is_kmtc);
    html+=`<div style="margin-bottom:16px">
      <div class="sec-ttl" style="margin-bottom:8px">
        <span style="padding:3px 12px;border-radius:3px;font-size:11px;font-weight:700;color:#fff;background:${TC[tr]||'#334155'}">${TL[tr]||tr}</span>
        ${progBar(svcs.length,maxS)}
        <span style="font-size:10px;color:#64748B">投入${svcs.reduce((s,d)=>s+d.num_ships,0)}隻</span>
        ${ks.length?`<span class="kmtc-mk">KMTC ${ks.length}</span>`:''}
      </div>
      <div class="tbl-wrap"><table>
        <thead><tr><th>Alliance</th><th>Operators</th><th>サービス名</th><th>隻数×TEU</th><th>ターミナル</th><th>Port Rotation</th></tr></thead>
        <tbody>${svcs.map(d=>`<tr class="${d.is_kmtc?'r-kmtc':''}">
          <td style="font-size:10px">${d.alliance}</td>
          <td style="font-weight:${d.is_kmtc?700:400};font-size:11px">${d.operators}${d.is_kmtc?'<span class="kmtc-mk">KMTC</span>':''}</td>
          <td style="font-size:11px">${d.service}</td>
          <td style="font-weight:700;color:#0D2D5C;white-space:nowrap">${d.ships_raw}</td>
          <td style="font-size:10px;font-weight:600">${d.terminal}</td>
          <td>${makeRot(d.rotation)}</td>
        </tr>`).join('')}</tbody>
      </table></div></div>`;
  });
  $('region-tables').innerHTML=html;
}

/* CARRIER TAB */
function renderCarrier(){
  const oc={},ac={};
  DATA.forEach(d=>{if(d.operators)oc[d.operators]=(oc[d.operators]||0)+1;if(d.alliance)ac[d.alliance]=(ac[d.alliance]||0)+1;});
  const maxC=Math.max(...Object.values(oc),1);
  const maxA=Math.max(...Object.values(ac),1);

  // Summary cards
  const topOps=Object.entries(oc).sort((a,b)=>b[1]-a[1]).slice(0,5);
  const topAl=Object.entries(ac).sort((a,b)=>b[1]-a[1]).slice(0,5);
  $('carrier-summary').innerHTML=`
    <div class="card" style="margin-bottom:0">
      <div class="card-title"><span class="badge">Operators Top5</span></div>
      ${topOps.map(([k,v])=>`<div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">
        <span style="font-size:11px;font-weight:600;min-width:140px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${k}${k.includes('KMTC')?'<span class="kmtc-mk">KMTC</span>':''}</span>
        ${progBar(v,maxC,k.includes('KMTC')?' g':'')}
      </div>`).join('')}
    </div>
    <div class="card" style="margin-bottom:0">
      <div class="card-title"><span class="badge">Alliance Top5</span></div>
      ${topAl.map(([k,v])=>`<div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">
        <span style="font-size:11px;font-weight:600;min-width:140px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${k}</span>
        ${progBar(v,maxA)}
      </div>`).join('')}
    </div>`;

  // Full table
  let html=`<div class="tbl-wrap"><table><thead><tr><th>Operators</th><th>サービス数</th><th style="min-width:120px">割合</th><th>投入隻数</th><th>展開地域</th></tr></thead><tbody>`;
  Object.entries(oc).sort((a,b)=>b[1]-a[1]).forEach(([op,cnt])=>{
    const svcs=DATA.filter(d=>d.operators===op);
    const ships=svcs.reduce((s,d)=>s+d.num_ships,0);
    const trs=[...new Set(svcs.map(d=>TL[d.trade]||d.trade))].join(', ');
    const ik=op.includes('KMTC');
    html+=`<tr class="${ik?'r-kmtc':''}"><td>${op}${ik?'<span class="kmtc-mk">KMTC</span>':''}</td>
      <td style="font-weight:700;color:#0D2D5C">${cnt}</td>
      <td>${progBar(cnt,maxC)}</td><td>${ships}</td>
      <td style="font-size:10px;color:#64748B">${trs}</td></tr>`;
  });
  html+='</tbody></table></div>';
  $('carrier-tbl').innerHTML=html;
}

/* TERMINAL TAB */
function renderTerminal(){
  const ts={},tsh={};
  DATA.forEach(d=>{d.terminal.split('/').forEach(t=>{t=t.trim();if(!t)return;ts[t]=(ts[t]||0)+1;tsh[t]=(tsh[t]||0)+d.num_ships;});});
  const K=Object.keys(ts).sort((a,b)=>ts[b]-ts[a]);
  const maxT=Math.max(...K.map(k=>ts[k]),1);

  const pc={},psh={};
  DATA.forEach(d=>{pc[d.port]=(pc[d.port]||0)+1;psh[d.port]=(psh[d.port]||0)+d.num_ships;});

  let html=`
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px">
      <div class="card" style="margin-bottom:0">
        <div class="card-title"><span class="badge">ターミナル別サービス数</span></div>
        ${K.map(t=>`<div style="display:flex;align-items:center;gap:8px;margin-bottom:5px">
          <span style="font-size:11px;font-weight:600;min-width:100px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${t}</span>
          ${progBar(ts[t],maxT)}
        </div>`).join('')}
      </div>
      <div class="card" style="margin-bottom:0">
        <div class="card-title"><span class="badge">北港 vs 新港</span></div>
        ${Object.entries(pc).map(([p,c])=>`<div style="display:flex;align-items:center;gap:8px;margin-bottom:5px">
          <span style="font-size:11px;font-weight:600;min-width:120px">${p}</span>
          <span style="font-weight:700;color:#0D2D5C">${c}件</span>
          <span style="font-size:10px;color:#64748B">${psh[p]}隻</span>
        </div>`).join('')}
      </div>
    </div>
    <div class="tbl-wrap"><table>
      <thead><tr><th>ターミナル</th><th>サービス数</th><th style="min-width:110px">割合</th><th>投入隻数</th><th>主要地域</th></tr></thead>
      <tbody>`;
  K.forEach(term=>{
    const svcs=DATA.filter(d=>d.terminal.includes(term));
    const ships=svcs.reduce((s,d)=>s+d.num_ships,0);
    const trs=[...new Set(svcs.map(d=>TL[d.trade]||d.trade))].slice(0,4).join(', ');
    html+=`<tr><td style="font-weight:700">${term}</td><td style="font-weight:700;color:#0D2D5C">${ts[term]}</td><td>${progBar(ts[term],maxT)}</td><td>${ships}</td><td style="font-size:10px;color:#64748B">${trs}</td></tr>`;
  });
  html+='</tbody></table></div>';
  $('terminal-tbl').innerHTML=html;
}

/* KMTC TAB */
function renderKmtc(){
  const kd=DATA.filter(d=>d.is_kmtc);
  const ships=kd.reduce((s,d)=>s+d.num_ships,0);
  const regions=new Set(kd.map(d=>d.trade)).size;
  const maxT=kd.length?Math.max(...kd.map(d=>d.teu_size)):0;
  $('kk-total').textContent=kd.length;
  $('kk-ships').textContent=ships.toLocaleString();
  $('kk-regions').textContent=regions;
  $('kk-maxteu').textContent=maxT.toLocaleString();
  $('kmtc-count-label').textContent=kd.length+'件';

  // Region breakdown
  const kr={},krsh={};
  kd.forEach(d=>{kr[d.trade]=(kr[d.trade]||0)+1;krsh[d.trade]=(krsh[d.trade]||0)+d.num_ships;});
  const maxK=Math.max(...Object.values(kr),1);
  $('kmtc-region-tbody').innerHTML=Object.entries(kr).sort((a,b)=>b[1]-a[1]).map(([tr,cnt])=>{
    const svcs=kd.filter(d=>d.trade===tr).slice(0,3).map(d=>d.service).join(', ');
    return`<tr>
      <td><span class="trade-tag" style="background:${TC[tr]||'#94A3B8'}22;color:${TC[tr]||'#334155'}">${TL[tr]||tr}</span></td>
      <td style="font-weight:700;color:#15803D">${cnt}</td>
      <td>${progBar(cnt,maxK,' g')}</td>
      <td>${krsh[tr]||0}</td>
      <td style="font-size:10px;color:#64748B">${svcs}</td>
    </tr>`;
  }).join('');

  $('kmtc-tbody').innerHTML=kd.map(d=>`<tr class="r-kmtc">
    <td>${ttag(d.trade)}</td>
    <td style="font-size:10px;color:#64748B">${d.sector}</td>
    <td style="font-size:10px">${d.alliance}</td>
    <td style="font-size:11px">${d.service}</td>
    <td style="font-weight:700;color:#15803D;white-space:nowrap">${d.ships_raw}</td>
    <td style="font-size:10px">${d.port}</td>
    <td style="font-size:10px;font-weight:600">${d.terminal}</td>
    <td>${makeRot(d.rotation)}</td>
    <td style="font-size:9px;color:#064E3B">${d.ship_details||''}</td>
  </tr>`).join('');
}

/* LIST */
function sortList(c){if(lSC===c)lSA=!lSA;else{lSC=c;lSA=true;}lPage=0;renderList();}
function goLP(p){lPage=p;renderListPage();}
function renderList(){
  const q=($('list-search').value||'').toLowerCase();
  const trade=$('list-trade').value;
  const op=$('list-op').value;
  const kmtc=$('list-kmtc').checked;
  const K=['no','trade','sector','alliance','operators','service','ships_raw','terminal','rotation','ship_details','code'];
  lFiltered=DATA.filter(d=>{
    if(trade&&d.trade!==trade)return false;
    if(op&&d.operators!==op)return false;
    if(kmtc&&!d.is_kmtc)return false;
    if(q){const h=[d.service,d.operators,d.alliance,d.rotation,d.ship_details,d.code].join(' ').toLowerCase();if(!h.includes(q))return false;}
    return true;
  });
  lFiltered.sort((a,b)=>{let va=a[K[lSC]]||'',vb=b[K[lSC]]||'';return typeof va==='number'?(lSA?va-vb:vb-va):(lSA?String(va).localeCompare(String(vb)):String(vb).localeCompare(String(va)));});
  lPage=0;
  renderListPage();
}
function renderListPage(){
  const f=lFiltered,s=lPage*PAGE,e=Math.min(s+PAGE,f.length),sl=f.slice(s,e);
  $('list-count').innerHTML='表示中: <strong>'+f.length+'</strong> サービス（全263件中）';
  $('list-tbody').innerHTML=sl.map(d=>`<tr class="${d.is_kmtc?'r-kmtc':''}">
    <td style="color:#CBD5E1;font-size:9px">${d.no}</td>
    <td>${ttag(d.trade)}</td>
    <td style="font-size:9px;color:#64748B">${d.sector}</td>
    <td style="font-size:10px">${d.alliance}</td>
    <td style="font-weight:${d.is_kmtc?700:400};font-size:11px">${d.operators}${d.is_kmtc?'<span class="kmtc-mk">KMTC</span>':''}</td>
    <td style="font-size:11px">${d.service}</td>
    <td style="font-weight:700;color:#0D2D5C;white-space:nowrap">${d.ships_raw}</td>
    <td style="font-size:10px;font-weight:600">${d.terminal}</td>
    <td style="font-size:10px;color:#475569">${d.rotation||''}</td>
    <td style="font-size:9px;color:#94A3B8">${d.ship_details||''}</td>
    <td style="font-size:9px;color:#CBD5E1">${d.code}</td>
  </tr>`).join('');
  const total=f.length,pages=Math.ceil(total/PAGE);
  $('list-pagination').innerHTML=pages<=1?'':
    `<div class="pagination">
      <button class="pill${lPage===0?' on':''}" onclick="goLP(0)">最初</button>
      <button class="pill" onclick="goLP(Math.max(0,lPage-1))"${lPage===0?' disabled':''}>◀</button>
      <span><strong>${s+1}〜${e}</strong> / ${total}件</span>
      <button class="pill" onclick="goLP(Math.min(${pages-1},lPage+1))"${lPage>=pages-1?' disabled':''}>▶</button>
      <button class="pill${lPage===pages-1?' on':''}" onclick="goLP(${pages-1})">最後</button>
    </div>`;
}

/* MAP */
function initLeaflet(){
  if(leafletMap)return;
  leafletMap=L.map('leaflet-map',{center:[25,115],zoom:3,zoomControl:true});
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution:'© OpenStreetMap contributors',maxZoom:18
  }).addTo(leafletMap);

  // Build port service counts
  const portCounts={};
  Object.entries(PIDX).forEach(([port,svcs])=>{portCounts[port]=svcs.length;});

  // Add Busan marker (special)
  const busanMk=L.circleMarker([35.10,129.04],{radius:14,fillColor:'#F0A500',color:'#0D2D5C',weight:2,fillOpacity:0.95}).addTo(leafletMap);
  busanMk.bindTooltip('<strong>BUSAN</strong><br>出発港（263サービス）',{permanent:false,className:'leaflet-tooltip'});

  // Add destination port markers
  portMarkers={};
  Object.entries(portCounts).forEach(([port,cnt])=>{
    const coords=getCoords(port);
    if(!coords)return;
    const r=Math.max(5,Math.min(18,4+Math.sqrt(cnt)*1.8));
    const svcs=PIDX[port]||[];
    const hasKmtc=svcs.some(d=>d.is_kmtc);
    const mk=L.circleMarker(coords,{
      radius:r,
      fillColor:hasKmtc?'#15803D':'#1D4ED8',
      color:'#fff',weight:1.5,fillOpacity:0.75
    }).addTo(leafletMap);
    mk.bindTooltip(`<strong>${port}</strong><br>週${cnt}便${hasKmtc?' ★KMTC':''}`,{permanent:false});
    mk.on('click',()=>showMapPortSidebar(port));
    portMarkers[port]=mk;
  });
}

let activeMapSvc=null;
function showMapPortSidebar(port){
  const svcs=PIDX[port]||[];
  $('map-sidebar-title').textContent=port;
  $('map-sidebar-sub').textContent=`週${svcs.length}便 ｜ ${new Set(svcs.map(d=>d.operators)).size}船社`;

  $('map-sidebar-body').innerHTML=svcs.map((d,i)=>`
    <div class="map-svc-item" id="msvc${i}" onclick="selectMapSvc(${i},'${port.replace(/'/g,"\\'")}')">
      <div class="map-svc-name">${d.service}</div>
      <div class="map-svc-op">${d.operators}${d.is_kmtc?'<span class="kmtc-mk" style="margin-left:4px">KMTC</span>':''}</div>
      <div class="map-svc-ships">${d.ships_raw}</div>
    </div>`).join('');
  activeMapSvc=null;
}

function selectMapSvc(idx,port){
  document.querySelectorAll('.map-svc-item').forEach(el=>el.classList.remove('active'));
  const el=document.getElementById('msvc'+idx);
  if(el)el.classList.add('active');

  const svc=(PIDX[port]||[])[idx];
  if(!svc)return;
  drawRoute(svc);
}

function drawRoute(svc){
  if(routeLayer){leafletMap.removeLayer(routeLayer);routeLayer=null;}
  if(!svc.rotation)return;
  const ports=svc.rotation.split(',').map(p=>p.trim()).filter(Boolean);
  const coords=[];
  ports.forEach(p=>{const c=getCoords(p);if(c)coords.push(c);});
  if(coords.length<2)return;
  routeLayer=L.polyline(coords,{color:'#F0A500',weight:2.5,opacity:0.85,dashArray:'6,4'}).addTo(leafletMap);
  leafletMap.fitBounds(routeLayer.getBounds(),{padding:[30,30]});
}

/* TAB SWITCH */
function sw(id,btn){
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  $(id).classList.add('active');
  document.querySelectorAll('.top-tab').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  // Hide filter bar for map tab
  const fb=$('filter-bar');
  if(fb)fb.style.display=(id==='pmap')?'none':'';
  if(id==='pdest'&&!tabInit.d){tabInit.d=true;renderDest();}
  if(id==='pregion'&&!tabInit.r){tabInit.r=true;renderRegion();}
  if(id==='pcarrier'&&!tabInit.c){tabInit.c=true;renderCarrier();}
  if(id==='pterminal'&&!tabInit.t){tabInit.t=true;renderTerminal();}
  if(id==='pkmtc'&&!tabInit.k){tabInit.k=true;renderKmtc();}
  if(id==='pmap'&&!tabInit.m){tabInit.m=true;setTimeout(initLeaflet,100);}
  if(id==='plist'&&!tabInit.l){tabInit.l=true;renderList();}
}

/* SIZE */
function setSz(sz,btn){
  document.body.className=sz==='m'?'':('sz-'+sz);
  document.querySelectorAll('.sz-btn').forEach(b=>b.classList.remove('on'));
  btn.classList.add('on');
}
"""

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>BUSAN PORT SERVICE DASHBOARD — 高麗海運ジャパン</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://accounts.google.com/gsi/client" async defer></script>
<style>{CSS}</style>
</head>
<body>
{HTML_BODY}
<script>
{JS.replace('__DATA__', data_json)}
</script>
</body>
</html>"""

with open('Busan_Port_Service_Dashboard.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

import os
sz = os.path.getsize('Busan_Port_Service_Dashboard.html')
print(f'完成: {sz:,} bytes ({sz//1024} KB)')
