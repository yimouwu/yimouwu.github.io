html = open('/Users/yimouwu/Desktop/yimou/yimouwu.github.io/proj/vppt/index.html', 'w')
html.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>VPPT: Deep Prior Learning for Embodied Scene Reconstruction and Tracking</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <style>
    :root {
      --max-w: 900px;
      --accent: #2563eb;
      --accent-light: #eff6ff;
      --text: #0f172a;
      --text-dim: #475569;
      --text-muted: #94a3b8;
      --border: rgba(0,0,0,0.08);
      --bg: #ffffff;
      --bg-2: #f8fafc;
      --radius: 10px;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: "Inter", system-ui, sans-serif;
      font-size: 16px;
      line-height: 1.75;
      color: var(--text);
      background: var(--bg);
      -webkit-font-smoothing: antialiased;
    }
    a { color: var(--accent); text-decoration: none; }
    a:hover { text-decoration: underline; }
    img, video { max-width: 100%; display: block; }

    /* ── NAV ── */
    #topbar {
      position: sticky; top: 0; z-index: 100;
      background: rgba(255,255,255,0.92);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
    }
    .topbar-inner {
      max-width: var(--max-w); margin: 0 auto;
      height: 48px; display: flex; align-items: center; gap: 20px;
    }
    .topbar-title {
      font-size: 0.85rem; font-weight: 700;
      letter-spacing: -0.01em; margin-right: auto;
      color: var(--text);
    }
    .topbar-links { display: flex; gap: 18px; }
    .topbar-links a {
      font-size: 0.82rem; color: var(--text-dim); font-weight: 500;
    }
    .topbar-links a:hover { color: var(--text); text-decoration: none; }

    /* ── HERO ── */
    #hero {
      padding: 72px 24px 52px;
      text-align: center;
      border-bottom: 1px solid var(--border);
    }
    .hero-inner { max-width: var(--max-w); margin: 0 auto; }

    .venue-badge {
      display: inline-block;
      font-family: "JetBrains Mono", monospace;
      font-size: 0.72rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--accent);
      background: var(--accent-light);
      border: 1px solid rgba(37,99,235,0.2);
      border-radius: 100px;
      padding: 4px 14px;
      margin-bottom: 20px;
    }

    h1.paper-title {
      font-size: clamp(1.6rem, 4vw, 2.4rem);
      font-weight: 700;
      line-height: 1.2;
      letter-spacing: -0.03em;
      color: var(--text);
      margin-bottom: 8px;
    }
    h1.paper-title span { color: var(--accent); }

    .paper-subtitle {
      font-size: 1rem;
      color: var(--text-dim);
      margin-bottom: 32px;
      font-weight: 300;
    }

    /* authors */
    .authors {
      font-size: 0.95rem;
      color: var(--text-dim);
      margin-bottom: 8px;
      line-height: 2;
    }
    .authors a { color: var(--text); font-weight: 500; }
    .authors a:hover { color: var(--accent); text-decoration: none; }
    .author-me { color: var(--text); font-weight: 600; }
    sup { font-size: 0.6em; }

    .affiliations {
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-bottom: 32px;
    }

    /* buttons */
    .btn-row {
      display: flex; flex-wrap: wrap;
      gap: 10px; justify-content: center;
      margin-bottom: 36px;
    }
    .btn {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 8px 20px;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 500;
      transition: all 0.2s;
      border: 1.5px solid transparent;
    }
    .btn-primary {
      background: var(--text); color: #fff;
      border-color: var(--text);
    }
    .btn-primary:hover {
      background: #1e293b; text-decoration: none;
    }
    .btn-secondary {
      background: var(--bg); color: var(--text);
      border-color: var(--border);
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .btn-secondary:hover {
      border-color: var(--text); text-decoration: none;
    }

    /* teaser */
    .teaser-wrap {
      border-radius: var(--radius);
      overflow: hidden;
      background: var(--bg-2);
      border: 1px solid var(--border);
      max-width: 820px;
      margin: 0 auto;
    }
    .teaser-wrap video,
    .teaser-wrap img {
      width: 100%; display: block;
    }
    .teaser-caption {
      font-size: 0.8rem;
      color: var(--text-muted);
      padding: 10px 16px;
      text-align: left;
      border-top: 1px solid var(--border);
    }

    /* ── SECTIONS ── */
    .section {
      padding: 64px 24px;
      border-bottom: 1px solid var(--border);
    }
    .section:last-of-type { border-bottom: none; }
    .section-inner {
      max-width: var(--max-w); margin: 0 auto;
    }
    .section-alt { background: var(--bg-2); }

    h2.section-heading {
      font-size: 1.35rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-bottom: 20px;
      color: var(--text);
    }

    /* abstract */
    .abstract-text {
      font-size: 0.97rem;
      color: var(--text-dim);
      line-height: 1.8;
      max-width: 780px;
    }

    /* TL;DR */
    .tldr {
      display: flex; gap: 12px; align-items: flex-start;
      background: var(--accent-light);
      border: 1px solid rgba(37,99,235,0.15);
      border-radius: var(--radius);
      padding: 16px 20px;
      margin-bottom: 28px;
      max-width: 780px;
    }
    .tldr-label {
      font-family: "JetBrains Mono", monospace;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      white-space: nowrap;
      margin-top: 2px;
    }
    .tldr-text {
      font-size: 0.92rem;
      color: var(--text);
      line-height: 1.65;
    }

    /* method figure */
    .method-fig {
      border-radius: var(--radius);
      overflow: hidden;
      border: 1px solid var(--border);
      margin: 24px 0;
    }
    .method-fig img { width: 100%; display: block; }
    .fig-caption {
      font-size: 0.8rem;
      color: var(--text-muted);
      padding: 10px 16px;
      border-top: 1px solid var(--border);
      background: var(--bg-2);
    }

    /* video grid */
    .video-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 24px;
    }
    .video-card {
      border-radius: var(--radius);
      overflow: hidden;
      border: 1px solid var(--border);
      background: var(--bg-2);
    }
    .video-card video,
    .video-card img {
      width: 100%; display: block;
      aspect-ratio: 16/9;
      object-fit: cover;
    }
    .video-card-caption {
      font-size: 0.78rem;
      color: var(--text-muted);
      padding: 8px 12px;
    }

    /* comparison slider placeholder */
    .comparison-note {
      font-size: 0.88rem;
      color: var(--text-muted);
      font-style: italic;
      margin-top: 8px;
    }

    /* citation */
    .citation-block {
      background: var(--bg-2);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px 24px;
      font-family: "JetBrains Mono", monospace;
      font-size: 0.78rem;
      line-height: 1.7;
      color: var(--text-dim);
      white-space: pre-wrap;
      word-break: break-all;
      position: relative;
    }
    .copy-btn {
      position: absolute; top: 12px; right: 12px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.75rem;
      cursor: pointer;
      color: var(--text-dim);
      font-family: "Inter", sans-serif;
      transition: all 0.2s;
    }
    .copy-btn:hover { border-color: var(--accent); color: var(--accent); }

    /* footer */
    #footer {
      padding: 28px 24px;
      text-align: center;
      font-size: 0.75rem;
      color: var(--text-muted);
      border-top: 1px solid var(--border);
    }
    #footer a { color: var(--text-muted); }
    #footer a:hover { color: var(--accent); }

    /* responsive */
    @media (max-width: 640px) {
      h1.paper-title { font-size: 1.5rem; }
      .btn-row { gap: 8px; }
      .btn { padding: 7px 14px; font-size: 0.82rem; }
      .video-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- NAV -->
  <header id="topbar">
    <div class="topbar-inner">
      <span class="topbar-title">VPPT</span>
      <nav class="topbar-links">
        <a href="#abstract">Abstract</a>
        <a href="#method">Method</a>
        <a href="#results">Results</a>
        <a href="#citation">Citation</a>
        <a href="/">&#8592; Home</a>
      </nav>
    </div>
  </header>

  <!-- HERO -->
  <section id="hero">
    <div class="hero-inner">

      <div class="venue-badge">arXiv 2026</div>

      <h1 class="paper-title">
        <span>VPPT</span>: Deep Prior Learning for<br>
        Embodied Scene Reconstruction and Tracking
      </h1>
      <p class="paper-subtitle">Visual Perception with Predictive Priors &amp; Tracking</p>

      <p class="authors">
        <span class="author-me">Yimou Wu</span><sup>1</sup>,
        <a href="#" target="_blank">Jiaxin Guo</a><sup>1</sup>,
        <a href="#" target="_blank">Yun-hui Liu</a><sup>1&#8224;</sup>,
        <a href="https://www.surgery.cuhk.edu.hk/profile.asp?alias=lizheng" target="_blank">Zheng Li</a><sup>1&#8224;</sup>
      </p>
      <p class="affiliations">
        <sup>1</sup>The Chinese University of Hong Kong &nbsp;&nbsp;
        <sup>&#8224;</sup>Corresponding authors
      </p>

      <div class="btn-row">
        <a href="https://github.com/yimouwu/vppt" target="_blank" class="btn btn-primary">&#128196; Paper</a>
        <a href="https://github.com/yimouwu/vppt" target="_blank" class="btn btn-secondary">&#128279; GitHub</a>
        <a href="#" class="btn btn-secondary" onclick="document.getElementById(\'teaser-vid\').play(); document.getElementById(\'teaser-vid\').scrollIntoView(); return false;">&#9654; Video</a>
        <a href="#results" class="btn btn-secondary">&#128248; Results</a>
      </div>

      <!-- teaser video / image -->
      <div class="teaser-wrap">
        <!--
          Replace with your teaser video:
          <video id="teaser-vid" autoplay muted loop playsinline>
            <source src="static/videos/teaser.mp4" type="video/mp4" />
          </video>
        -->
        <img src="static/images/teaser.png"
             alt="VPPT teaser"
             onerror="this.src=\'\'; this.alt=\'[Teaser image — place static/images/teaser.png]\';" />
        <div class="teaser-caption">
          VPPT reconstructs and tracks embodied scenes from monocular video using deep visual priors.
          <!-- Edit this caption -->
        </div>
      </div>

    </div>
  </section>

  <!-- ABSTRACT -->
  <section id="abstract" class="section">
    <div class="section-inner">
      <h2 class="section-heading">Abstract</h2>

      <div class="tldr">
        <span class="tldr-label">TL;DR</span>
        <span class="tldr-text">
          VPPT introduces deep visual priors into embodied scene reconstruction and tracking,
          achieving robust 3D understanding from monocular video in challenging real-world environments.
          <!-- Edit this TL;DR -->
        </span>
      </div>

      <p class="abstract-text">
        [Replace this with your paper abstract. Describe the problem, your approach,
        and the key contributions and results. 3&ndash;5 sentences is ideal for a project page.]
      </p>
    </div>
  </section>

  <!-- METHOD -->
  <section id="method" class="section section-alt">
    <div class="section-inner">
      <h2 class="section-heading">Method</h2>

      <p style="font-size:0.95rem;color:var(--text-dim);max-width:780px;margin-bottom:20px;">
        [Describe your method here. Explain the key components and how they work together.
        Replace the figure below with your pipeline diagram.]
      </p>

      <div class="method-fig">
        <img src="static/images/pipeline.png"
             alt="VPPT pipeline"
             onerror="this.parentElement.style.display=\'none\'" />
        <div class="fig-caption">
          Overview of the VPPT pipeline. [Edit this caption to describe your figure.]
        </div>
      </div>
    </div>
  </section>

  <!-- RESULTS -->
  <section id="results" class="section">
    <div class="section-inner">
      <h2 class="section-heading">Results</h2>

      <p style="font-size:0.95rem;color:var(--text-dim);max-width:780px;margin-bottom:8px;">
        Qualitative results on [your dataset/benchmark].
        <!-- Edit this description -->
      </p>
      <p class="comparison-note">Replace the placeholders below with your result videos or images.</p>

      <div class="video-grid">

        <div class="video-card">
          <video autoplay muted loop playsinline
                 onerror="this.parentElement.style.background=\'#f1f5f9\'">
            <source src="static/videos/result1.mp4" type="video/mp4" />
          </video>
          <div class="video-card-caption">Scene 1 &mdash; [description]</div>
        </div>

        <div class="video-card">
          <video autoplay muted loop playsinline
                 onerror="this.parentElement.style.background=\'#f1f5f9\'">
            <source src="static/videos/result2.mp4" type="video/mp4" />
          </video>
          <div class="video-card-caption">Scene 2 &mdash; [description]</div>
        </div>

        <div class="video-card">
          <video autoplay muted loop playsinline
                 onerror="this.parentElement.style.background=\'#f1f5f9\'">
            <source src="static/videos/result3.mp4" type="video/mp4" />
          </video>
          <div class="video-card-caption">Scene 3 &mdash; [description]</div>
        </div>

        <div class="video-card">
          <video autoplay muted loop playsinline
                 onerror="this.parentElement.style.background=\'#f1f5f9\'">
            <source src="static/videos/result4.mp4" type="video/mp4" />
          </video>
          <div class="video-card-caption">Scene 4 &mdash; [description]</div>
        </div>

      </div>
    </div>
  </section>

  <!-- CITATION -->
  <section id="citation" class="section section-alt">
    <div class="section-inner">
      <h2 class="section-heading">Citation</h2>
      <div class="citation-block" id="cite-block">@article{wu2026vppt,
  title     = {VPPT: Deep Prior Learning for Embodied Scene Reconstruction and Tracking},
  author    = {Wu, Yimou and Guo, Jiaxin and Liu, Yun-hui and Li, Zheng},
  journal   = {arXiv preprint},
  year      = {2026}
}<button class="copy-btn" onclick="copyCitation()">Copy</button></div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer id="footer">
    <p>
      VPPT &nbsp;&#183;&nbsp;
      <a href="https://www.cuhk.edu.hk" target="_blank">CUHK</a>
      &nbsp;&#183;&nbsp;
      <a href="/">Yimou Wu</a>
      &nbsp;&#183;&nbsp;
      Page template inspired by
      <a href="https://vggt-omega.github.io/" target="_blank">VGGT-&#937;</a>
    </p>
  </footer>

  <script>
    function copyCitation() {
      const text = document.getElementById("cite-block").innerText.replace("Copy", "").trim();
      navigator.clipboard.writeText(text).then(() => {
        const btn = document.querySelector(".copy-btn");
        btn.textContent = "Copied!";
        setTimeout(() => btn.textContent = "Copy", 2000);
      });
    }
  </script>

</body>
</html>''')
html.close()
print('done')