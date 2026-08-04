// Magical Cursor with Stars, Sparkles & Efficient Performance
(function () {
  let dot, ring;
  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let ringX = mouseX;
  let ringY = mouseY;
  let lastSparkleTime = 0;
  let activeSparkles = 0;

  document.addEventListener('DOMContentLoaded', () => {
    // Create cursor elements if not present
    dot = document.createElement('div');
    dot.className = 'cursor-dot';
    ring = document.createElement('div');
    ring.className = 'cursor-ring';

    document.body.appendChild(dot);
    document.body.appendChild(ring);

    // Track Mouse with passive listener and GPU transform
    document.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      dot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;

      // Throttle sparkle creation (at most 1 per 150ms, max 10 active)
      const now = Date.now();
      if (now - lastSparkleTime > 150 && activeSparkles < 10) {
        lastSparkleTime = now;
        spawnSparkle(mouseX, mouseY);
      }
    }, { passive: true });

    // Ring smooth lerp animation loop using GPU translate3d
    function animateRing() {
      ringX += (mouseX - ringX) * 0.2;
      ringY += (mouseY - ringY) * 0.2;
      ring.style.transform = `translate3d(${ringX}px, ${ringY}px, 0) translate(-50%, -50%)`;
      requestAnimationFrame(animateRing);
    }
    animateRing();

    // Click Particle Explosion
    document.addEventListener('click', (e) => {
      ring.classList.add('active');
      setTimeout(() => ring.classList.remove('active'), 250);

      for (let i = 0; i < 6; i++) {
        spawnExplosionParticle(e.clientX, e.clientY);
      }
    });

    // Efficient Magnetic Effect using MouseEnter/MouseMove on .magnetic elements only
    document.addEventListener('mousemove', (e) => {
      const magneticTarget = e.target.closest('.magnetic');
      if (!magneticTarget) return;

      const rect = magneticTarget.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dist = Math.hypot(e.clientX - cx, e.clientY - cy);

      if (dist < 60) {
        const pullX = (e.clientX - cx) * 0.25;
        const pullY = (e.clientY - cy) * 0.25;
        magneticTarget.style.transform = `translate3d(${pullX}px, ${pullY}px, 0)`;
      } else {
        magneticTarget.style.transform = '';
      }
    }, { passive: true });
  });

  function spawnSparkle(x, y) {
    activeSparkles++;
    const star = document.createElement('div');
    star.className = 'star-particle';
    const symbols = ['✦', '✧', '★', '⚡', '✨'];
    star.textContent = symbols[Math.floor(Math.random() * symbols.length)];
    star.style.left = `${x}px`;
    star.style.top = `${y}px`;

    const angle = Math.random() * Math.PI * 2;
    const distance = 15 + Math.random() * 25;
    const dx = Math.cos(angle) * distance;
    const dy = Math.sin(angle) * distance;

    star.style.setProperty('--dx', `${dx}px`);
    star.style.setProperty('--dy', `${dy}px`);

    document.body.appendChild(star);
    setTimeout(() => {
      star.remove();
      activeSparkles = Math.max(0, activeSparkles - 1);
    }, 600);
  }

  function spawnExplosionParticle(x, y) {
    const star = document.createElement('div');
    star.className = 'star-particle';
    star.textContent = '★';
    star.style.left = `${x}px`;
    star.style.top = `${y}px`;

    const angle = Math.random() * Math.PI * 2;
    const distance = 30 + Math.random() * 50;
    const dx = Math.cos(angle) * distance;
    const dy = Math.sin(angle) * distance;

    star.style.setProperty('--dx', `${dx}px`);
    star.style.setProperty('--dy', `${dy}px`);

    document.body.appendChild(star);
    setTimeout(() => star.remove(), 700);
  }
})();
