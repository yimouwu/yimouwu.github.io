/* ═══════════════════════════════════════════════════════════
   CANVAS — drifting particle constellation background
═══════════════════════════════════════════════════════════ */
(function initCanvas() {
  const canvas = document.getElementById('bg-canvas');
  const ctx    = canvas.getContext('2d');
  let W, H, particles;

  const PARTICLE_COUNT = 55;
  const GOLD = '180,155,100'; // soft warm tone on white

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  function randomParticle() {
    return {
      x:    Math.random() * W,
      y:    Math.random() * H,
      r:    Math.random() * 1.2 + 0.3,
      vx:   (Math.random() - 0.5) * 0.18,
      vy:   (Math.random() - 0.5) * 0.18,
      alpha: Math.random() * 0.5 + 0.1,
    };
  }

  function init() {
    resize();
    particles = Array.from({ length: PARTICLE_COUNT }, randomParticle);
  }

  function drawConnections() {
    const LINK_DIST = 120;
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx   = particles[i].x - particles[j].x;
        const dy   = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist > LINK_DIST) continue;
        const alpha = (1 - dist / LINK_DIST) * 0.12;
        ctx.beginPath();
        ctx.strokeStyle = `rgba(${GOLD},${alpha})`;
        ctx.lineWidth   = 0.5;
        ctx.moveTo(particles[i].x, particles[i].y);
        ctx.lineTo(particles[j].x, particles[j].y);
        ctx.stroke();
      }
    }
  }

  function tick() {
    ctx.clearRect(0, 0, W, H);
    drawConnections();

    for (const p of particles) {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0) p.x = W;
      if (p.x > W) p.x = 0;
      if (p.y < 0) p.y = H;
      if (p.y > H) p.y = 0;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${GOLD},${p.alpha * 0.35})`;
      ctx.fill();
    }
    requestAnimationFrame(tick);
  }

  window.addEventListener('resize', resize);
  init();
  tick();
})();


/* ═══════════════════════════════════════════════════════════
   SCROLL REVEAL — IntersectionObserver for .reveal elements
═══════════════════════════════════════════════════════════ */
(function initReveal() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
})();


/* dot-nav removed */


/* ═══════════════════════════════════════════════════════════
   ABSTRACT TOGGLE — expand / collapse paper abstracts
═══════════════════════════════════════════════════════════ */
function toggleAbstract(btn) {
  const abstract = btn.nextElementSibling;
  const isHidden = abstract.classList.contains('hidden');
  abstract.classList.toggle('hidden', !isHidden);
  btn.classList.toggle('open', isHidden);
}


/* parallax removed — photo is static */
/* ═══════════════════════════════════════════════════════════
   DARK MODE TOGGLE
═══════════════════════════════════════════════════════════ */
(function initTheme() {
  const btn  = document.getElementById('theme-toggle');
  const html = document.documentElement;
  const icon = btn ? btn.querySelector('.theme-icon') : null;

  /* restore saved preference */
  const saved = localStorage.getItem('theme');
  if (saved) {
    html.setAttribute('data-theme', saved);
    if (icon) icon.innerHTML = saved === 'dark' ? '&#9728;' : '&#9790;';
  }

  if (!btn) return;

  btn.addEventListener('click', () => {
    const isDark = html.getAttribute('data-theme') === 'dark';
    const next   = isDark ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    /* sun = light mode, moon = dark mode */
    if (icon) icon.innerHTML = next === 'dark' ? '&#9728;' : '&#9790;';
  });
})();
