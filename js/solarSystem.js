// Developer Solar System 3D Orbit Engine
(function () {
  const ICONS_DATA = [
    // Ring 0 (Inner): 5 icons
    { name: "HTML5", iconClass: "fa-brands fa-html5", ring: 0, speed: 0.006, color: "#e34f26", glow: "rgba(227,79,38,0.4)" },
    { name: "CSS3", iconClass: "fa-brands fa-css3-alt", ring: 0, speed: 0.006, color: "#10b981", glow: "rgba(16,185,129,0.4)" }, // Styled in theme green
    { name: "JavaScript", iconClass: "fa-brands fa-js", ring: 0, speed: 0.006, color: "#f7df1e", glow: "rgba(247,223,30,0.4)" },
    { name: "Git", iconClass: "fa-brands fa-git-alt", ring: 0, speed: 0.006, color: "#f05032", glow: "rgba(240,80,50,0.4)" },
    { name: "VS Code", iconClass: "fa-solid fa-code", ring: 0, speed: 0.006, color: "#8b5cf6", glow: "rgba(139,92,246,0.4)" }, // Styled in theme purple

    // Ring 1 (Middle): 5 icons
    { name: "React", iconClass: "fa-brands fa-react", ring: 1, speed: -0.004, color: "#61dafb", glow: "rgba(97,218,251,0.4)" },
    { name: "Python", iconClass: "fa-brands fa-python", ring: 1, speed: -0.004, color: "#10b981", glow: "rgba(16,185,129,0.4)" }, // nature green
    { name: "SQL", iconClass: "fa-solid fa-database", ring: 1, speed: -0.004, color: "#ec4899", glow: "rgba(236,72,153,0.4)" },
    { name: "Terminal", iconClass: "fa-solid fa-terminal", ring: 1, speed: -0.004, color: "#10b981", glow: "rgba(16,185,129,0.4)" },
    { name: "GitHub", iconClass: "fa-brands fa-github", ring: 1, speed: -0.004, color: "#ffffff", glow: "rgba(255,255,255,0.4)" },

    // Ring 2 (Outer): 5 icons
    { name: "Docker", iconClass: "fa-brands fa-docker", ring: 2, speed: 0.002, color: "#ec4899", glow: "rgba(236,72,153,0.4)" }, // pink glow
    { name: "Kali Linux", iconClass: "fa-solid fa-shield-halved", ring: 2, speed: 0.002, color: "#8b5cf6", glow: "rgba(139,92,246,0.4)" },
    { name: "AI Chip", iconClass: "fa-solid fa-microchip", ring: 2, speed: 0.002, color: "#f59e0b", glow: "rgba(245,158,11,0.4)" },
    { name: "Database", iconClass: "fa-solid fa-server", ring: 2, speed: 0.002, color: "#ec4899", glow: "rgba(236,72,153,0.4)" },
    { name: "TypeScript", iconClass: "fa-solid fa-code", ring: 2, speed: 0.002, color: "#3178c6", glow: "rgba(49,120,198,0.4)" }
  ];

  let container;
  let icons = [];
  let mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
  let animationFrame;
  let lastFrameTime = 0;
  let isVisible = true;
  const FRAME_INTERVAL = 1000 / 30;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Orbit Dimensions config
  const BASE_RADII = [160, 240, 320]; // Inner, Middle, Outer
  const TILT_X = 55 * Math.PI / 180; // 55 degree orbit tilt

  class OrbitingIcon {
    constructor(data, index, ringCount) {
      this.data = data;
      this.ring = data.ring;
      // Even spacing on the ring initially
      this.angle = (index / ringCount) * 2 * Math.PI;
      this.speed = data.speed;
      
      // Create DOM element
      this.el = document.createElement("div");
      this.el.className = "solar-icon magnetic";
      this.el.title = data.name;
      this.el.style.color = data.color;
      this.el.style.setProperty("--glow-color", data.glow);
      
      const icon = document.createElement("i");
      icon.className = data.iconClass;
      this.el.appendChild(icon);
      
      container.appendChild(this.el);
    }

    update(radiusScale, mouseX, mouseY) {
      // Rotate angle
      this.angle += this.speed;

      // Base radius of current ring
      const baseRadius = BASE_RADII[this.ring] * radiusScale;

      // 3D coordinates on orbit plane
      let x = baseRadius * Math.cos(this.angle);
      let y = baseRadius * Math.sin(this.angle);

      // Apply 3D tilt (rotate around X axis)
      let z = y * Math.sin(TILT_X);
      let yProjected = y * Math.cos(TILT_X);

      // Mouse Parallax Influence
      // Deeper particles shift less, closer particles shift more
      const parallaxFactor = (z + baseRadius) / (2 * baseRadius); // 0 to 1
      const dx = x + mouseX * 25 * parallaxFactor;
      const dy = yProjected + mouseY * 20 * parallaxFactor;

      // 3D Visual Factors based on Z depth
      const minScale = 0.7;
      const maxScale = 1.15;
      const scale = minScale + (maxScale - minScale) * parallaxFactor;
      
      const minOpacity = 0.35;
      const maxOpacity = 1.0;
      const opacity = minOpacity + (maxOpacity - minOpacity) * parallaxFactor;

      // Max blur 3px for farthest icons
      const blur = Math.max(0, 3 * (1 - parallaxFactor));

      // Positioning: container (0, 0) is the center of orbit
      this.el.style.transform = `translate(-50%, -50%) translate3d(${dx}px, ${dy}px, 0px) scale(${scale})`;
      this.el.style.opacity = opacity;
      this.el.style.filter = blur > 0.5 ? `blur(${blur}px)` : "none";
      
      // z-index threshold relative to profile picture (z-index 10)
      // When z is negative, it's behind profile frame (z-index 5). When positive, in front (z-index 25)
      this.el.style.zIndex = z < 0 ? 5 : 25;
    }
  }

  function init() {
    container = document.getElementById("solar-system-container");
    if (!container) return;
    if (reduceMotion || window.matchMedia('(pointer: coarse)').matches) {
      container.replaceChildren();
      return;
    }

    // Reset container contents
    container.innerHTML = "";
    icons = [];

    // Group icons by ring to determine counts
    const ringCounts = [0, 0, 0];
    ICONS_DATA.forEach(data => ringCounts[data.ring]++);

    // Track index within each ring
    const ringIndices = [0, 0, 0];
    ICONS_DATA.forEach(data => {
      const ringIdx = ringIndices[data.ring]++;
      const totalInRing = ringCounts[data.ring];
      icons.push(new OrbitingIcon(data, ringIdx, totalInRing));
    });

    // Cursor coordinates listener
    document.addEventListener("mousemove", (e) => {
      const cx = window.innerWidth / 2;
      const cy = window.innerHeight / 2;
      mouse.targetX = (e.clientX - cx) / cx;
      mouse.targetY = (e.clientY - cy) / cy;
    }, { passive: true });

    const observer = new IntersectionObserver(([entry]) => {
      isVisible = entry.isIntersecting;
      if (isVisible && !animationFrame && !document.hidden) loop(performance.now());
    }, { threshold: 0.05 });
    observer.observe(container.closest('.hero-section') || container);
    document.addEventListener('visibilitychange', () => {
      if (!document.hidden && isVisible && !animationFrame) loop(performance.now());
    });
    loop(performance.now());
  }

  function loop(timestamp) {
    animationFrame = null;
    if (!isVisible || document.hidden) return;
    if (timestamp - lastFrameTime < FRAME_INTERVAL) {
      animationFrame = requestAnimationFrame(loop);
      return;
    }
    lastFrameTime = timestamp;
    // Smooth mouse coordinates interpolation
    mouse.x += (mouse.targetX - mouse.x) * 0.05;
    mouse.y += (mouse.targetY - mouse.y) * 0.05;

    // Scale orbits down on mobile screens to prevent layout overflow
    const radiusScale = window.innerWidth < 768 ? 0.55 : 1.0;

    // Update all icons
    icons.forEach(icon => icon.update(radiusScale, mouse.x, mouse.y));

    animationFrame = requestAnimationFrame(loop);
  }

  // Handle reload on DOM content or custom events
  document.addEventListener("DOMContentLoaded", init);
  window.addEventListener("resize", () => {
    // Parallax update
  }, { passive: true });
})();
