// Three.js & Canvas 3D Floating Tech Objects Engine
(function () {
  let canvas, ctx, animationFrame;
  let width, height;
  let particles = [];
  let mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };

  const TECH_OBJECTS = [
    { label: "HTML", color: "#e34f26", size: 24, type: "icon", shape: "<HTML/>" },
    { label: "CSS", color: "#1572b6", size: 24, type: "icon", shape: "{CSS}" },
    { label: "JS", color: "#f7df1e", size: 22, type: "icon", shape: "JS" },
    { label: "TS", color: "#3178c6", size: 22, type: "icon", shape: "TS" },
    { label: "React", color: "#61dafb", size: 26, type: "icon", shape: "⚛ React" },
    { label: "Python", color: "#3776ab", size: 24, type: "icon", shape: "🐍 Python" },
    { label: "Docker", color: "#0db7ed", size: 24, type: "icon", shape: "🐳 Docker" },
    { label: "Git", color: "#f05032", size: 20, type: "icon", shape: "Git" },
    { label: "GitHub", color: "#10b981", size: 22, type: "icon", shape: "GitHub" },
    { label: "Linux", color: "#f59e0b", size: 22, type: "icon", shape: "🐧 Linux" },
    { label: "Cloud", color: "#8b5cf6", size: 24, type: "icon", shape: "☁ Cloud" },
    { label: "DB", color: "#ec4899", size: 22, type: "icon", shape: "🛢 Database" },
    { label: "Server", color: "#10b981", size: 22, type: "icon", shape: "🖥 Server" },
    { label: "Terminal", color: "#10b981", size: 20, type: "icon", shape: ">_ Terminal" },
    { label: "AI Chip", color: "#f59e0b", size: 26, type: "icon", shape: "🧠 AI Chip" },
    { label: "Globe", color: "#38bdf8", size: 24, type: "icon", shape: "🌐 Network" },
    { label: "Binary", color: "#64748b", size: 16, type: "code", shape: "01101001" },
    { label: "Brackets", color: "#8b5cf6", size: 20, type: "code", shape: "[...code]" }
  ];

  class Particle3D {
    constructor() {
      this.reset(true);
    }

    reset(initial = false) {
      this.x = (Math.random() - 0.5) * width * 1.5;
      this.y = (Math.random() - 0.5) * height * 1.5;
      this.z = initial ? Math.random() * 1000 : 1000;
      
      const tech = TECH_OBJECTS[Math.floor(Math.random() * TECH_OBJECTS.length)];
      this.shape = tech.shape;
      this.color = tech.color;
      this.baseSize = tech.size;
      
      this.vx = (Math.random() - 0.5) * 0.4;
      this.vy = (Math.random() - 0.5) * 0.4;
      this.vz = -0.6 - Math.random() * 0.8;
      this.rotation = Math.random() * Math.PI * 2;
      this.vRot = (Math.random() - 0.5) * 0.015;
    }

    update() {
      this.x += this.vx + (mouse.x * 0.05);
      this.y += this.vy + (mouse.y * 0.05);
      this.z += this.vz;
      this.rotation += this.vRot;

      if (this.z < 10) {
        this.reset(false);
      }
    }

    draw() {
      const fov = 400;
      const scale = fov / (fov + this.z);
      const projX = width / 2 + this.x * scale;
      const projY = height / 2 + this.y * scale;

      if (projX < -100 || projX > width + 100 || projY < -100 || projY > height + 100) return;

      const size = this.baseSize * scale * 1.3;
      const opacity = Math.min(0.8, Math.max(0.15, (1000 - this.z) / 1000));

      ctx.save();
      ctx.translate(projX, projY);
      ctx.rotate(this.rotation);
      ctx.globalAlpha = opacity;

      ctx.font = `600 ${size}px 'Fira Code', monospace`;
      ctx.fillStyle = this.color;
      ctx.fillText(this.shape, -size / 2, size / 4);

      ctx.restore();
    }
  }

  function init() {
    canvas = document.getElementById('canvas-3d');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'canvas-3d';
      document.body.prepend(canvas);
    }
    ctx = canvas.getContext('2d');

    resize();
    window.addEventListener('resize', resize, { passive: true });

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

    // 25 lightweight floating tech particles for ultra-smooth 60+ FPS
    particles = Array.from({ length: 25 }, () => new Particle3D());
    loop();
  }

  function resize() {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
  }

  function loop() {
    mouse.x += (mouse.targetX - mouse.x) * 0.05;
    mouse.y += (mouse.targetY - mouse.y) * 0.05;

    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
      particles[i].draw();
    }

    animationFrame = requestAnimationFrame(loop);
  }

  document.addEventListener('DOMContentLoaded', init);
})();
