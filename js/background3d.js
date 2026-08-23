// Section-Aware Canvas 3D Floating Particles & Constellations Engine
(function () {
  let canvas, ctx, animationFrame;
  let width, height;
  let particles = [];
  let mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
  let activeSection = "home";
  let isVisible = true;
  let lastFrameTime = 0;
  const FRAME_INTERVAL = 1000 / 30;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Section specific shapes config
  const SECTION_SHAPES = {
    home: [
      { shape: "🐍 Python", color: "#10b981", size: 22, type: "icon" },
      { shape: "🌶️ Flask", color: "#ec4899", size: 22, type: "icon" },
      { shape: "🤖 ML", color: "#10b981", size: 22, type: "icon" },
      { shape: "🧠 AI", color: "#f59e0b", size: 24, type: "icon" },
      { shape: "✨ Gemini", color: "#8b5cf6", size: 23, type: "icon" },
      { shape: "⚛️ React", color: "#8b5cf6", size: 24, type: "icon" },
      { shape: "🐳 Docker", color: "#ec4899", size: 22, type: "icon" },
      { shape: "✦", color: "rgba(255, 255, 255, 0.4)", size: 8, type: "star" },
      { shape: "✧", color: "rgba(16, 185, 129, 0.3)", size: 10, type: "star" },
      { shape: "✨", color: "rgba(139, 92, 246, 0.3)", size: 8, type: "star" }
    ],
    about: [
      { shape: "const", color: "#8b5cf6", size: 18, type: "code" },
      { shape: "let", color: "#ec4899", size: 18, type: "code" },
      { shape: "function()", color: "#10b981", size: 20, type: "code" },
      { shape: "import", color: "#f97316", size: 18, type: "code" },
      { shape: "=>", color: "#f59e0b", size: 22, type: "code" },
      { shape: "{}", color: "#10b981", size: 22, type: "code" },
      { shape: "[]", color: "#8b5cf6", size: 20, type: "code" },
      { shape: "console.log", color: "#f59e0b", size: 18, type: "code" },
      { shape: "&&", color: "#ec4899", size: 20, type: "code" },
      { shape: "||", color: "#f97316", size: 20, type: "code" }
    ],
    skills: [
      { shape: "0", color: "#10b981", size: 16, type: "binary" },
      { shape: "1", color: "#047857", size: 16, type: "binary" },
      { shape: "0101", color: "#10b981", size: 18, type: "binary" },
      { shape: "1001", color: "#047857", size: 18, type: "binary" },
      { shape: "1100", color: "#8b5cf6", size: 18, type: "binary" },
      { shape: "0110", color: "#10b981", size: 18, type: "binary" },
      { shape: "%", color: "#f59e0b", size: 20, type: "binary" }
    ],
    projects: [
      { shape: "$ git push", color: "#8b5cf6", size: 18, type: "project" },
      { shape: "npm run dev", color: "#10b981", size: 18, type: "project" },
      { shape: "docker run", color: "#ec4899", size: 18, type: "project" },
      { shape: "pip install", color: "#f59e0b", size: 18, type: "project" },
      { shape: ">_ terminal", color: "#10b981", size: 20, type: "project" },
      { shape: "status: 200", color: "#10b981", size: 18, type: "project" },
      { shape: "GET /api", color: "#8b5cf6", size: 18, type: "project" }
    ],
    certificates: [
      { shape: "🏆", color: "#f59e0b", size: 26, type: "cert" },
      { shape: "📜", color: "#8b5cf6", size: 24, type: "cert" },
      { shape: "★", color: "#f59e0b", size: 18, type: "cert" },
      { shape: "✓", color: "#10b981", size: 22, type: "cert" },
      { shape: "Star", color: "#ec4899", size: 18, type: "cert" },
      { shape: "Award", color: "#f59e0b", size: 18, type: "cert" }
    ],
    timeline: [
      { shape: "→", color: "#8b5cf6", size: 22, type: "journey" },
      { shape: "●", color: "#ec4899", size: 14, type: "journey" },
      { shape: "🚀", color: "#f59e0b", size: 26, type: "journey" },
      { shape: "Q1", color: "#10b981", size: 18, type: "journey" },
      { shape: "2026", color: "#f97316", size: 20, type: "journey" },
      { shape: "Journey", color: "#8b5cf6", size: 18, type: "journey" }
    ],
    contact: [
      { shape: "✉", color: "#ec4899", size: 24, type: "contact" },
      { shape: "✈", color: "#10b981", size: 24, type: "contact" },
      { shape: "💬", color: "#f59e0b", size: 24, type: "contact" },
      { shape: "@", color: "#8b5cf6", size: 22, type: "contact" },
      { shape: "send", color: "#ec4899", size: 18, type: "contact" },
      { shape: "mail", color: "#10b981", size: 18, type: "contact" }
    ]
  };

  class Particle3D {
    constructor() {
      this.reset(true);
    }

    reset(initial = false) {
      this.x = (Math.random() - 0.5) * width * 1.5;
      this.y = (Math.random() - 0.5) * height * 1.5;
      this.z = initial ? Math.random() * 1000 : 1000;
      
      // Select shape based on the currently active section
      const shapes = SECTION_SHAPES[activeSection] || SECTION_SHAPES.home;
      const target = shapes[Math.floor(Math.random() * shapes.length)];
      
      this.shape = target.shape;
      this.color = target.color;
      this.baseSize = target.size;
      this.type = target.type;
      
      this.vx = (Math.random() - 0.5) * 0.4;
      this.vy = (Math.random() - 0.5) * 0.4;
      this.vz = -0.6 - Math.random() * 0.8;
      this.rotation = Math.random() * Math.PI * 2;
      this.vRot = (Math.random() - 0.5) * 0.015;
    }

    update() {
      // Float slowly and react to mouse movement
      this.x += this.vx + (mouse.x * 0.12);
      this.y += this.vy + (mouse.y * 0.12);
      this.z += this.vz;
      this.rotation += this.vRot;

      // If particle gets too close to screen, wrap around back
      if (this.z < 10) {
        this.reset(false);
      }
    }

    draw() {
      const fov = 400;
      const scale = fov / (fov + this.z);
      const projX = width / 2 + this.x * scale;
      const projY = height / 2 + this.y * scale;

      // Skip drawing if outside viewport bounds
      if (projX < -150 || projX > width + 150 || projY < -150 || projY > height + 150) return;

      const size = this.baseSize * scale * 1.3;
      const opacity = Math.min(0.65, Math.max(0.08, (1000 - this.z) / 1000));

      ctx.save();
      ctx.translate(projX, projY);
      ctx.rotate(this.rotation);
      ctx.globalAlpha = opacity;

      // Set Font style based on type
      if (this.type === "star" || this.type === "cert" || this.type === "contact") {
        ctx.font = `${size}px 'Fira Code', monospace`;
      } else {
        ctx.font = `600 ${size}px 'Fira Code', monospace`;
      }

      ctx.fillStyle = this.color;
      ctx.fillText(this.shape, -size / 2, size / 4);
      ctx.restore();
    }
  }

  function init() {
    // A full-screen canvas is expensive on low-power and touch devices. The
    // rest of the page remains fully usable without this decorative effect.
    if (reduceMotion || window.matchMedia("(pointer: coarse)").matches) {
      canvas = document.getElementById('canvas-3d');
      if (canvas) canvas.remove();
      return;
    }

    canvas = document.getElementById('canvas-3d');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'canvas-3d';
      document.body.prepend(canvas);
    }
    ctx = canvas.getContext('2d');

    resize();
    window.addEventListener('resize', resize, { passive: true });
    document.addEventListener('visibilitychange', () => {
      isVisible = !document.hidden;
      if (isVisible && !animationFrame) loop(performance.now());
    });

    // Mouse Parallax movement
    let mouseThrottle = false;
    document.addEventListener('mousemove', (e) => {
      if (!mouseThrottle) {
        mouseThrottle = true;
        requestAnimationFrame(() => {
          mouse.targetX = (e.clientX - width / 2) / (width / 2);
          mouse.targetY = (e.clientY - height / 2) / (height / 2);
          mouseThrottle = false;
        });
      }
    }, { passive: true });

    // Setup Section Observer to morph canvas particles
    setupSectionObserver();

    // Keep the background subtle enough for smooth scrolling on laptops.
    particles = Array.from({ length: 24 }, () => new Particle3D());
    loop(performance.now());
  }

  function setupSectionObserver() {
    const observerOptions = {
      root: null,
      rootMargin: "-20% 0px -40% 0px", // Detect section when middle of screen crosses it
      threshold: 0.1
    };

    const sectionObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const targetId = entry.target.id;
          if (SECTION_SHAPES[targetId] && activeSection !== targetId) {
            activeSection = targetId;
            // Slowly morph particles to the new section's theme by resetting them
            morphParticles();
          }
        }
      });
    }, observerOptions);

    // Observe all main sections
    const ids = ["home", "about", "skills", "projects", "certificates", "timeline", "contact"];
    ids.forEach(id => {
      const el = document.getElementById(id);
      if (el) sectionObserver.observe(el);
    });
  }

  function morphParticles() {
    // Morph about half the particles immediately, and allow the rest to recycle naturally
    particles.forEach((p, idx) => {
      if (idx % 2 === 0) {
        // Recycle depth to back of field
        p.z = 800 + Math.random() * 200;
        const shapes = SECTION_SHAPES[activeSection] || SECTION_SHAPES.home;
        const target = shapes[Math.floor(Math.random() * shapes.length)];
        p.shape = target.shape;
        p.color = target.color;
        p.baseSize = target.size;
        p.type = target.type;
      }
    });
  }

  function resize() {
    width = window.innerWidth;
    height = window.innerHeight;
    const pixelRatio = Math.min(window.devicePixelRatio || 1, 1.25);
    canvas.width = Math.floor(width * pixelRatio);
    canvas.height = Math.floor(height * pixelRatio);
    canvas.style.width = `${width}px`;
    canvas.style.height = `${height}px`;
    ctx.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
  }

  function loop(timestamp) {
    animationFrame = null;
    if (!isVisible) return;
    if (timestamp - lastFrameTime < FRAME_INTERVAL) {
      animationFrame = requestAnimationFrame(loop);
      return;
    }
    lastFrameTime = timestamp;
    // Interpolate mouse coordinates smoothly
    mouse.x += (mouse.targetX - mouse.x) * 0.05;
    mouse.y += (mouse.targetY - mouse.y) * 0.05;

    ctx.clearRect(0, 0, width, height);

    // Render faint constellation lines between particles that are close
    for (let i = 0; i < particles.length; i++) {
      const p1 = particles[i];
      const scale1 = 400 / (400 + p1.z);
      const x1 = width / 2 + p1.x * scale1;
      const y1 = height / 2 + p1.y * scale1;

      for (let j = i + 1; j < particles.length; j++) {
        const p2 = particles[j];
        const scale2 = 400 / (400 + p2.z);
        const x2 = width / 2 + p2.x * scale2;
        const y2 = height / 2 + p2.y * scale2;

        const dist = Math.hypot(x1 - x2, y1 - y2);
        if (dist < 150) {
          ctx.beginPath();
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
          const opacity = (1 - (dist / 150)) * 0.12 * Math.min(scale1, scale2);
          ctx.strokeStyle = activeSection === "skills" 
            ? `rgba(4, 120, 87, ${opacity})` 
            : activeSection === "about"
            ? `rgba(139, 92, 246, ${opacity})`
            : `rgba(16, 185, 129, ${opacity})`;
          ctx.lineWidth = 0.7 * scale1;
          ctx.stroke();
        }
      }
    }

    // Update and draw all particles
    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
      particles[i].draw();
    }

    animationFrame = requestAnimationFrame(loop);
  }

  document.addEventListener('DOMContentLoaded', init);
})();
