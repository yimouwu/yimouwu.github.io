css = open('/Users/yimouwu/Desktop/yimou/yimouwu.github.io/assets/css/style.css', 'w')
css.write("""/* ═══════════════════════════════════════════════════
   RESET & TOKENS
═══════════════════════════════════════════════════ */
:root {
  --max-w:      800px;
  --brown:      #8a6a2e;
  --brown-dim:  rgba(138,106,46,0.10);
  --gold-bg:    rgba(212,170,50,0.07);
  --gold-bdr:   rgba(212,170,50,0.22);
  --transition: 0.25s ease;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html {
  font-size: 17px;
  scroll-behavior: smooth;
  scroll-padding-top: 60px;
}

body {
  font-family: 'DM Sans', system-ui, sans-serif;
  font-size: 1rem;
  line-height: 1.72;
  color: #111;
  background: #fff;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

img { max-width: 100%; display: block; }
a   { color: inherit; text-decoration: none; }
ul  { list-style: none; }

/* ═══════════════════════════════════════════════════
   CANVAS
═══════════════════════════════════════════════════ */
#bg-canvas {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  opacity: 0.15;
}

/* ═══════════════════════════════════════════════════
   TOP NAV
═══════════════════════════════════════════════════ */
#topnav {
  position: sticky;
  top: 0;
  z-index: 200;
  background: rgba(255,255,255,0.93);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0,0,0,0.07);
  padding: 0 24px;
}

.nav-inner {
  max-width: var(--max-w);
  margin: 0 auto;
  height: 54px;
  display: flex;
  align-items: center;
  gap: 28px;
}

.nav-identity {
  display: flex;
  flex-direction: column;
  line-height: 1.25;
  margin-right: auto;
}

.nav-name {
  font-size: 0.9rem;
  font-weight: 700;
  color: #000;
  white-space: nowrap;
  letter-spacing: -0.01em;
}

.nav-sub {
  font-size: 0.65rem;
  color: #999;
  white-space: nowrap;
}

.nav-links {
  display: flex;
  gap: 22px;
}

.nav-links a {
  font-size: 0.82rem;
  font-weight: 500;
  color: #333;
  transition: color var(--transition);
}
.nav-links a:hover { color: #000; }

#theme-toggle {
  background: none;
  border: 1px solid rgba(0,0,0,0.18);
  border-radius: 20px;
  padding: 3px 10px;
  cursor: pointer;
  font-size: 0.82rem;
  color: #555;
  transition: all var(--transition);
  line-height: 1.4;
}
#theme-toggle:hover { border-color: rgba(0,0,0,0.4); color: #000; }

/* ═══════════════════════════════════════════════════
   HERO / BIO
═══════════════════════════════════════════════════ */
#bio {
  position: relative;
  z-index: 1;
  padding: 56px 24px 48px;
}

.hero-inner {
  max-width: var(--max-w);
  margin: 0 auto;
  display: flex;
  align-items: flex-start;
  gap: 44px;
}

.hero-text { flex: 1; }

.hero-intro {
  font-size: 1rem;
  color: #111;
  font-weight: 400;
  line-height: 1.75;
  margin-bottom: 14px;
}

.hero-prof-link {
  color: #1a6fc4;
  text-decoration: underline;
  text-underline-offset: 2px;
}
.hero-prof-link:hover { color: #0d4f9e; }

.hero-links {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0;
  margin-top: 20px;
}

.link-txt {
  font-size: 0.88rem;
  font-weight: 500;
  color: #1a6fc4;
  text-decoration: underline;
  text-underline-offset: 2px;
  transition: color var(--transition);
}
.link-txt:hover { color: #0d4f9e; }

.link-sep {
  font-size: 0.75rem;
  color: #bbb;
  padding: 0 6px;
  user-select: none;
  text-decoration: none;
}

/* photo */
.hero-photo-wrap {
  flex-shrink: 0;
  width: 110px;
  height: 148px;
  border-radius: 5px;
  overflow: hidden;
  border: 1px solid rgba(0,0,0,0.08);
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  margin-top: 4px;
}

.hero-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  pointer-events: none;
  transition: none;
}
.hero-photo:hover { filter: none; }
.hero-photo-wrap:hover .hero-photo { filter: none; transform: none; }

.hero-photo-placeholder {
  display: none;
  width: 100%;
  height: 100%;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: 300;
  color: #8a6a2e;
  background: #f5f0e8;
}

/* ═══════════════════════════════════════════════════
   SECTIONS
═══════════════════════════════════════════════════ */
.section {
  position: relative;
  z-index: 1;
  padding: 48px 24px;
  border-top: none;
}

.section-inner {
  max-width: var(--max-w);
  margin: 0 auto;
}

.section-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #000;
  letter-spacing: -0.01em;
  margin-bottom: 6px;
}

.misc-sub-title { margin-top: 36px; }

.section-sub {
  font-size: 0.78rem;
  color: #999;
  margin-bottom: 28px;
  line-height: 1.6;
}

.highlight-word {
  color: #b8860b;
  font-weight: 500;
  background: rgba(212,170,50,0.12);
  padding: 0 3px;
  border-radius: 3px;
}

/* ═══════════════════════════════════════════════════
   PUBLICATIONS
═══════════════════════════════════════════════════ */
.pub-list {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.pub-item {
  display: flex;
  gap: 20px;
  padding: 16px 12px;
  margin: 0 -12px;
  border-top: 1px solid rgba(0,0,0,0.06);
  background: transparent;
}
.pub-item:first-child { border-top: none; }

.pub-featured {
  background: var(--gold-bg);
  border-radius: 8px;
  border: 1px solid var(--gold-bdr) !important;
  margin: 6px -12px;
}

.pub-media {
  flex-shrink: 0;
  width: 190px;
  height: 115px;
  border-radius: 6px;
  overflow: hidden;
  background: #f0ede8;
}
.pub-media.no-media { background: #f0ede8; }
.pub-media img,
.pub-media video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.pub-info { flex: 1; min-width: 0; }

.pub-title {
  font-size: 0.9rem;
  font-weight: 600;
  color: #000;
  line-height: 1.4;
  margin-bottom: 4px;
}

.pub-authors {
  font-size: 0.82rem;
  color: #999;
  font-weight: 300;
  margin-bottom: 3px;
  line-height: 1.5;
}

.pub-me {
  color: #000;
  font-weight: 600;
}

.pub-star {
  font-size: 0.6em;
  vertical-align: super;
  color: #b8860b;
  font-weight: 600;
  margin-left: 1px;
}

.pub-corr {
  font-size: 0.6em;
  vertical-align: super;
  color: #999;
  margin-left: 1px;
}

.pub-venue {
  font-size: 0.8rem;
  color: #555;
  margin-bottom: 8px;
}

.pub-award {
  display: inline-block;
  font-size: 0.6rem;
  font-family: 'DM Mono', monospace;
  color: #b8860b;
  background: rgba(212,170,50,0.15);
  border: 1px solid rgba(212,170,50,0.3);
  border-radius: 4px;
  padding: 1px 6px;
  vertical-align: middle;
  margin-left: 4px;
}

.pub-links {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-bottom: 6px;
}

.pub-link {
  font-size: 0.8rem;
  color: #1a6fc4;
  text-decoration: underline;
  text-underline-offset: 2px;
  transition: color var(--transition);
}
.pub-link:hover { color: #0d4f9e; }

.pub-links a + a::before {
  content: " / ";
  color: #ccc;
  text-decoration: none;
  display: inline-block;
  margin-right: 4px;
}

.pub-note {
  font-size: 0.72rem;
  color: #aaa;
  line-height: 1.55;
  margin-top: 6px;
  font-style: italic;
}
.pub-note::before {
  content: "* ";
  font-style: normal;
  color: #bbb;
}

/* ═══════════════════════════════════════════════════
   MISC
═══════════════════════════════════════════════════ */
.misc-list {
  list-style: disc;
  padding-left: 18px;
  margin-top: 8px;
}

.misc-list li {
  font-size: 0.9rem;
  color: #222;
  padding: 2px 0;
  line-height: 1.65;
}

.misc-placeholder {
  font-size: 0.88rem;
  color: #bbb;
  font-style: italic;
}

/* ═══════════════════════════════════════════════════
   FOOTER
═══════════════════════════════════════════════════ */
#footer {
  position: relative;
  z-index: 1;
  border-top: 1px solid rgba(0,0,0,0.07);
  padding: 24px;
}

.footer-inner {
  max-width: var(--max-w);
  margin: 0 auto;
  text-align: center;
}

.footer-inner p {
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  color: #bbb;
}

/* ═══════════════════════════════════════════════════
   DARK MODE
═══════════════════════════════════════════════════ */
[data-theme="dark"] body         { background: #111 !important; color: #ddd !important; }
[data-theme="dark"] #topnav      { background: rgba(17,17,17,0.93) !important; border-bottom-color: rgba(255,255,255,0.07) !important; }
[data-theme="dark"] .nav-name    { color: #eee !important; }
[data-theme="dark"] .nav-links a { color: #bbb !important; }
[data-theme="dark"] .nav-links a:hover { color: #fff !important; }
[data-theme="dark"] #theme-toggle { color: #aaa !important; border-color: rgba(255,255,255,0.2) !important; }
[data-theme="dark"] .hero-intro  { color: #ccc !important; }
[data-theme="dark"] .link-txt    { color: #7aaddf !important; }
[data-theme="dark"] .hero-prof-link { color: #7aaddf !important; }
[data-theme="dark"] .section-title { color: #eee !important; }
[data-theme="dark"] .section-sub { color: #555 !important; }
[data-theme="dark"] .pub-item    { border-top-color: rgba(255,255,255,0.06) !important; }
[data-theme="dark"] .pub-featured { background: rgba(212,170,50,0.06) !important; border-color: rgba(212,170,50,0.18) !important; }
[data-theme="dark"] .pub-title   { color: #eee !important; }
[data-theme="dark"] .pub-authors { color: #666 !important; }
[data-theme="dark"] .pub-me      { color: #eee !important; }
[data-theme="dark"] .pub-venue   { color: #888 !important; }
[data-theme="dark"] .pub-link    { color: #7aaddf !important; }
[data-theme="dark"] .pub-media   { background: #222 !important; }
[data-theme="dark"] .pub-note    { color: #555 !important; }
[data-theme="dark"] .misc-list li { color: #ccc !important; }
[data-theme="dark"] #footer      { border-top-color: rgba(255,255,255,0.07) !important; }
[data-theme="dark"] .footer-inner p { color: #444 !important; }

/* ═══════════════════════════════════════════════════
   RESPONSIVE
═══════════════════════════════════════════════════ */
@media (max-width: 640px) {
  html { font-size: 15px; }
  .hero-inner      { flex-direction: column-reverse; align-items: center; gap: 24px; text-align: center; }
  .hero-links      { justify-content: center; }
  .hero-photo-wrap { width: 96px; height: 128px; }
  .pub-item        { flex-direction: column; margin: 0; padding: 16px 0; }
  .pub-media       { width: 100%; height: 140px; }
  .nav-links       { display: none; }
  .nav-sub         { display: none; }
}
""")
css.close()
print("done")