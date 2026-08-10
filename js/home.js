// Home Page Interactive Logic
document.addEventListener('DOMContentLoaded', () => {
  initGreeting();
  initTypingEffect();
  initStatCounters();
  initSkillsTabs();
  initCopyEmail();
  initContactForm();
  initBackToTop();
  initMobileMenu();
  renderHomeFeaturedProjects();
  renderHomeFeaturedCertificates();
});

// Time-based greeting
function initGreeting() {
  const greetingEl = document.getElementById('time-greeting');
  if (!greetingEl) return;
  const hour = new Date().getHours();
  let text = "Good evening";
  if (hour >= 5 && hour < 12) text = "Good morning";
  else if (hour >= 12 && hour < 17) text = "Good afternoon";

  greetingEl.innerHTML = `<i class="fa-regular fa-clock"></i> ${text}, Tech Visionary!`;
}

// Typed Role Animation
function initTypingEffect() {
  const roleEl = document.getElementById('typed-role');
  if (!roleEl) return;

  const roles = [
    "Full Stack Developer",
    "AI Agent Engineer",
    "Cybersecurity Explorer",
    "Cloud & Docker Enthusiast",
    "BCA Student @ PES IAMS"
  ];

  let roleIdx = 0;
  let charIdx = 0;
  let isDeleting = false;

  function type() {
    const current = roles[roleIdx];
    if (isDeleting) {
      roleEl.textContent = current.substring(0, charIdx - 1);
      charIdx--;
    } else {
      roleEl.textContent = current.substring(0, charIdx + 1);
      charIdx++;
    }

    let speed = isDeleting ? 40 : 80;

    if (!isDeleting && charIdx === current.length) {
      speed = 2000;
      isDeleting = true;
    } else if (isDeleting && charIdx === 0) {
      isDeleting = false;
      roleIdx = (roleIdx + 1) % roles.length;
      speed = 500;
    }

    setTimeout(type, speed);
  }
  type();
}

// Animated Statistics Counters
function initStatCounters() {
  const counters = document.querySelectorAll('[data-count]');
  if (!counters.length) return;

  fetch('/api/stats')
    .then(res => res.json())
    .then(stats => {
      counters.forEach(el => {
        const text = el.parentElement.querySelector('div:last-child').textContent.toLowerCase();
        if (text.includes('featured')) {
          el.setAttribute('data-count', stats.featured_projects);
        } else if (text.includes('ai project')) {
          el.setAttribute('data-count', stats.ai_projects);
        } else if (text.includes('project')) {
          el.setAttribute('data-count', stats.projects);
        } else if (text.includes('certificate')) {
          el.setAttribute('data-count', stats.certificates);
        } else if (text.includes('technologies')) {
          el.setAttribute('data-count', stats.technologies);
        }
      });
      const visitorEl = document.getElementById('visitor-count-num');
      if (visitorEl && stats.visits) {
        visitorEl.textContent = stats.visits.toLocaleString();
      }
      startObserver();
    })
    .catch(err => {
      console.warn("Stats API error, fallback to HTML data-attributes:", err);
      startObserver();
    });

  function startObserver() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-count')) || 0;
          const suffix = el.getAttribute('data-suffix') || '';
          let current = 0;
          const step = Math.max(1, Math.ceil(target / 40));

          const timer = setInterval(() => {
            current += step;
            if (current >= target) {
              el.textContent = target + suffix;
              clearInterval(timer);
            } else {
              el.textContent = current + suffix;
            }
          }, 30);
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(c => observer.observe(c));
  }
}

// Skills Filter & Progress Bars
function initSkillsTabs() {
  const tabs = document.querySelectorAll('.skills-category-tabs .tab-btn');
  const cards = document.querySelectorAll('.skill-card-item');

  function animateProgress() {
    cards.forEach(card => {
      if (card.style.display !== 'none') {
        const circle = card.querySelector('.fg-circle');
        if (circle) {
          const level = circle.getAttribute('data-level');
          const offset = 251.2 - (251.2 * level) / 100;
          setTimeout(() => {
            circle.style.strokeDashoffset = offset;
          }, 80);
        }
      }
    });
  }

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const cat = tab.getAttribute('data-cat');
      cards.forEach(card => {
        if (cat === 'all' || card.getAttribute('data-cat') === cat) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
      animateProgress();
    });
  });

  // Trigger progress fill on scroll
  const fillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const circle = entry.target;
        const level = circle.getAttribute('data-level');
        const offset = 251.2 - (251.2 * level) / 100;
        circle.style.strokeDashoffset = offset;
        fillObserver.unobserve(circle);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fg-circle').forEach(circle => fillObserver.observe(circle));
}

// Copy Email Button
function initCopyEmail() {
  const btn = document.getElementById('copyEmailBtn');
  if (!btn) return;

  btn.addEventListener('click', () => {
    const email = 'sanjaygl2006@gmail.com';
    navigator.clipboard.writeText(email).then(() => {
      if (window.ToastManager) {
        window.ToastManager.show('Email copied to clipboard! (sanjaygl2006@gmail.com)', 'success', 'fa-copy');
      }
    });
  });
}

// Contact Form Handler
function initContactForm() {
  const form = document.getElementById('contactFormMain');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Honeypot spam check
    const honeypot = form.querySelector('input[name="botcheck"]');
    if (honeypot && honeypot.value) {
      console.warn("Spam submission blocked via honeypot.");
      if (window.ToastManager) {
        window.ToastManager.show("Spam detected and blocked successfully.", "error", "fa-shield-halved");
      }
      return;
    }

    const nameInput = document.getElementById('contactName');
    const emailInput = document.getElementById('contactEmail');
    const subjectInput = document.getElementById('contactSubject');
    const messageInput = document.getElementById('contactMessage');
    
    const name = nameInput ? nameInput.value.trim() : '';
    const email = emailInput ? emailInput.value.trim() : '';
    const subject = subjectInput ? subjectInput.value : '';
    const message = messageInput ? messageInput.value.trim() : '';
    
    // Front-end Validations
    if (name.length < 2) {
      if (window.ToastManager) window.ToastManager.show("Please enter a valid name (at least 2 letters).", "error", "fa-circle-xmark");
      return;
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      if (window.ToastManager) window.ToastManager.show("Please enter a valid email address.", "error", "fa-circle-xmark");
      return;
    }
    if (!subject) {
      if (window.ToastManager) window.ToastManager.show("Please select a contact subject topic.", "error", "fa-circle-xmark");
      return;
    }
    if (message.length < 10) {
      if (window.ToastManager) window.ToastManager.show("Please write a descriptive message (at least 10 letters).", "error", "fa-circle-xmark");
      return;
    }

    // Disable submit button during send
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalBtnHTML = submitBtn ? submitBtn.innerHTML : 'Send Message';
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending message...';
    }
    
    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, subject, message })
      });
      
      const result = await response.json();
      
      if (response.ok && result.status === 'success') {
        if (window.ToastManager) {
          window.ToastManager.show(result.message || `Thank you, ${name}! Your message has been sent successfully.`, 'success', 'fa-paper-plane');
        }
        form.reset();
      } else {
        throw new Error(result.message || 'Server error occurred.');
      }
    } catch (err) {
      console.error('Contact submit error:', err);
      if (window.ToastManager) {
        window.ToastManager.show('Failed to send message. Please check connection and try again.', 'error', 'fa-circle-xmark');
      }
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnHTML;
      }
    }
  });
}

// Back to top button & Scroll progress
function initBackToTop() {
  const backBtn = document.createElement('button');
  backBtn.className = 'icon-btn back-top-btn';
  backBtn.setAttribute('aria-label', 'Back to top');
  backBtn.innerHTML = '<i class="fa-solid fa-arrow-up"></i>';
  document.body.appendChild(backBtn);

  backBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  let scrollTicking = false;
  window.addEventListener('scroll', () => {
    if (!scrollTicking) {
      scrollTicking = true;
      requestAnimationFrame(() => {
        const scrollPos = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = docHeight > 0 ? (scrollPos / docHeight) * 100 : 0;

        const progressEl = document.getElementById('scroll-progress');
        if (progressEl) progressEl.style.width = `${scrollPercent}%`;

        const navbar = document.querySelector('.navbar');
        if (navbar) navbar.classList.toggle('scrolled', scrollPos > 50);

        if (scrollPos > 400) {
          backBtn.classList.add('visible');
        } else {
          backBtn.classList.remove('visible');
        }
        scrollTicking = false;
      });
    }
  }, { passive: true });
}

// Mobile Menu
function initMobileMenu() {
  const hamburger = document.getElementById('hamburger');
  const menu = document.getElementById('navMenu');
  if (!hamburger || !menu) return;

  hamburger.addEventListener('click', () => {
    menu.classList.toggle('active');
    hamburger.classList.toggle('active');
  });
}

// Global Certificate Lightbox Modal functions
window.openCertModal = function (certId) {
  if (typeof CERTIFICATES_DATA === 'undefined') return;
  const cert = CERTIFICATES_DATA.find(c => c.id === certId) || (typeof certId === 'number' ? CERTIFICATES_DATA[certId] : null);
  if (!cert) return;

  let modal = document.getElementById('certModal');
  if (!modal) {
    modal = document.createElement('div');
    modal.className = 'premium-modal-overlay';
    modal.id = 'certModal';
    document.body.appendChild(modal);
  }

  const day = cert.day || (cert.date && /^\d+/.test(cert.date) ? cert.date.match(/^\d+/)[0] : "—");
  const month = cert.month || "—";
  const year = cert.year || "—";
  const skillsList = (cert.skillsLearned || []).map(s => `<span class="cert-skill-tag" style="font-size:0.75rem;">${s}</span>`).join('');

  modal.innerHTML = `
    <div class="premium-modal-box" style="max-width: 760px;">
      <div class="premium-modal-header">
        <div style="display:flex;align-items:center;gap:12px;">
          <div style="font-size:1.8rem;">${cert.emoji || '📜'}</div>
          <div>
            <div class="cert-org-name" style="font-size:0.8rem; font-weight:700; color:var(--golden-yellow); text-transform:uppercase;">${cert.org}</div>
            <h2 style="font-size:1.15rem;font-weight:800; color:var(--text-main); margin-top:2px;">${cert.title}</h2>
          </div>
        </div>
        <button class="premium-modal-close" onclick="closeCertModal()"><i class="fa-solid fa-xmark"></i></button>
      </div>

      <div class="premium-modal-body" style="grid-template-columns: 1fr; padding: 24px; gap: 20px;">
        <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="width:100%; height:320px; overflow:hidden; border-radius:12px; border:1px solid var(--border-glass); background:#02060d; position:relative;">
            <img src="${cert.image || 'assets/logo.svg'}" alt="${cert.title}" style="width:100%; height:100%; object-fit:contain;" onerror="this.src='assets/logo.svg'">
          </div>

          <div style="background:var(--bg-main);border-radius:12px;padding:16px;border:1px solid var(--border-glass)">
            <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:8px;">
              <strong>Date Earned:</strong> ${day} ${month} ${year}
            </div>
            <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:8px;">
              <strong>Credential ID:</strong> <span style="font-family:var(--ff-code);color:var(--emerald-primary);">${cert.credentialId}</span>
            </div>
            <div style="font-size:0.85rem;color:var(--text-muted); display:flex; flex-wrap:wrap; align-items:center; gap:8px;">
              <strong>Skills Certified:</strong> 
              <div class="cert-skills-list" style="margin-top:0;">
                ${skillsList}
              </div>
            </div>
          </div>

          <p style="font-size:0.92rem;color:var(--text-muted);line-height:1.6;margin-bottom:12px;">${cert.desc}</p>

          <div style="display:flex;gap:16px;flex-wrap:wrap;">
            <a href="${cert.verifyLink}" target="_blank" rel="noopener" class="btn btn-primary ripple-btn" style="flex:1; text-align:center; display:flex; align-items:center; justify-content:center; gap:8px;">
              <i class="fa-solid fa-arrow-up-right-from-square"></i> Verify Official Credential
            </a>
            <button class="btn btn-outline ripple-btn" onclick="closeCertModal()">Close Preview</button>
          </div>
        </div>
      </div>
    </div>
  `;

  setTimeout(() => {
    modal.classList.add('active');
    document.body.classList.add('no-scroll');
  }, 10);
};

window.closeCertModal = function () {
  const modal = document.getElementById('certModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.classList.remove('no-scroll');
  }
};

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && window.closeCertModal) {
    window.closeCertModal();
  }
});

// Render Featured Projects Preview on Home Page
function renderHomeFeaturedProjects() {
  const grid = document.getElementById('homeFeaturedProjectsGrid');
  if (!grid || typeof PROJECTS_DATA === 'undefined') return;

  // Filter to show exactly our top 5 featured projects
  const featured = PROJECTS_DATA.filter(p => p.featured === true).slice(0, 5);

  grid.innerHTML = featured.map(p => `
    <div class="featured-project-card scroll-reveal revealed" id="project-card-${p.id}" data-id="${p.id}" style="grid-column: span 1; display:flex; flex-direction:column; height:100%;">
      <div class="featured-card-glow"></div>
      <div style="position:relative; z-index: 5; display:flex; flex-direction:column; height:100%; flex:1;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span class="project-featured-tag">★ Featured Project</span>
          <span class="tech-pill" style="background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.4); color: var(--emerald-primary); font-weight:700;">
            <i class="fa-solid fa-microchip"></i> ${(p.category || 'AI').toUpperCase()}
          </span>
        </div>
        
        <div style="margin:16px 0; border-radius:var(--radius-md); overflow:hidden; position:relative; height:160px; border:1px solid var(--border-glass); background:#03070c;">
          ${p.image && !p.image.includes('logo.svg') ? `
            <img src="${p.image}" alt="${p.title}" style="width:100%; height:100%; object-fit:cover; transition: transform 0.5s ease;" onerror="this.style.display='none'">
          ` : `
            <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,0.03);">
              <i class="fa-solid ${p.icon || 'fa-laptop-code'}" style="font-size:3rem; color:var(--emerald-primary)"></i>
            </div>
          `}
        </div>

        <h3 class="project-title" style="margin-top:0; font-size:1.3rem;">${p.title}</h3>
        <p class="project-tagline" style="margin-bottom:16px; font-size:0.9rem; color:var(--text-muted); flex:1;">${p.tagline}</p>
        
        <!-- Statistics Row -->
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; margin-bottom:16px;">
          ${Object.entries(p.stats || {}).slice(0, 3).map(([lbl, val]) => `
            <div style="background:var(--bg-main); border:1px solid var(--border-glass); border-radius:var(--radius-sm); padding:6px; text-align:center;">
              <div style="font-size:0.58rem; color:var(--text-muted); text-transform:uppercase;">${lbl}</div>
              <div style="font-size:0.75rem; font-weight:700; color:var(--emerald-primary); margin-top:2px;">${val}</div>
            </div>
          `).join('')}
        </div>

        <div class="project-tech-pills" style="margin-bottom:20px; gap:6px;">
          ${p.tech.slice(0, 4).map(t => `<span class="tech-pill" style="font-size:0.72rem; padding:3px 8px;">${t}</span>`).join('')}
          ${p.tech.length > 4 ? `<span class="tech-pill" style="font-size:0.72rem; padding:3px 8px;">+${p.tech.length - 4}</span>` : ''}
        </div>

        <div style="display:flex; gap:10px; margin-top:auto;">
          <a href="projects.html?id=${p.id}" class="btn btn-primary btn-sm ripple-btn" style="flex:1; font-weight:700; height:38px; display:flex; align-items:center; justify-content:center; gap:6px;">
            <i class="fa-solid fa-book-open"></i> Read More
          </a>
          ${p.live ? `<a href="${p.live}" target="_blank" rel="noopener" class="btn btn-outline btn-sm ripple-btn" style="width:38px; height:38px; display:flex; align-items:center; justify-content:center;"><i class="fa-solid fa-arrow-up-right-from-square"></i></a>` : ''}
          <a href="${p.github}" target="_blank" rel="noopener" class="btn btn-outline btn-sm ripple-btn" style="width:38px; height:38px; display:flex; align-items:center; justify-content:center;"><i class="fa-brands fa-github"></i></a>
        </div>
      </div>
    </div>
  `).join('');

  initHomeTiltEffects();
}

// 3D Tilt Effect on Featured Cards
function initHomeTiltEffects() {
  const cards = document.querySelectorAll('.featured-project-card');
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const xc = rect.width / 2;
      const yc = rect.height / 2;
      const angleX = (yc - y) / 8;
      const angleY = (x - xc) / 8;
      card.style.setProperty('--rx', `${angleX}deg`);
      card.style.setProperty('--ry', `${angleY}deg`);
      card.style.setProperty('--mx', `${x}px`);
      card.style.setProperty('--my', `${y}px`);
    });

    card.addEventListener('mouseleave', () => {
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
}

// Render Featured Certificates Preview on Home Page
function renderHomeFeaturedCertificates() {
  const grid = document.getElementById('homeFeaturedCertsGrid');
  if (!grid || typeof CERTIFICATES_DATA === 'undefined') return;

  // Explicitly select the top 5 certificates
  const selectedCerts = [];
  
  // 1. PRAVIDHI
  let c1 = CERTIFICATES_DATA.find(c => c.id === "cert-named-1");
  if (c1) selectedCerts.push(c1);
  // 2. Star Performer
  let c2 = CERTIFICATES_DATA.find(c => c.id === "cert-named-5");
  if (c2) selectedCerts.push(c2);
  // 3. Web Tech Internship
  let c3 = CERTIFICATES_DATA.find(c => c.id === "cert-named-4");
  if (c3) selectedCerts.push(c3);
  // 4. AI & Generative AI Basics
  let c4 = CERTIFICATES_DATA.find(c => (c.title || '').includes("Learn AI and Gen AI Basics") || (c.title || '').includes("AI & Generative AI Basics"));
  if (c4) selectedCerts.push(c4);
  // 5. Online Quiz on Safe & Responsible Use of AI
  let c5 = CERTIFICATES_DATA.find(c => c.id === "cert-named-3");
  if (c5) selectedCerts.push(c5);

  // If match fails, fallback to first 5
  if (selectedCerts.length < 5) {
    const list = CERTIFICATES_DATA.slice(0, 5);
    selectedCerts.length = 0;
    selectedCerts.push(...list);
  }

  grid.innerHTML = selectedCerts.slice(0, 5).map((c, i) => {
    const skillsList = (c.skillsLearned || []).slice(0, 3).map(s => `<span class="cert-skill-tag" style="font-size:0.7rem; padding:2px 6px;">${s}</span>`).join('');
    return `
      <a href="${c.verifyLink || '#'}" target="_blank" rel="noopener" class="cert-card-anchor" style="text-decoration:none; color:inherit; display:block; height:100%;">
        <div class="glass cert-card scroll-reveal revealed" id="home-cert-card-${i}" style="transition:transform 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease; overflow:hidden; border:1px solid var(--border-glass); border-radius:var(--radius-lg); display:flex; flex-direction:column; height:100%; padding:16px; cursor:pointer;">
          ${c.image && !c.image.includes('logo.svg') ? `
          <div style="width:100%; height:160px; overflow:hidden; position:relative; background:#02060d; border-radius:8px; margin-bottom:12px;">
            <img src="${c.image}" alt="${c.title}" style="width:100%; height:100%; object-fit:cover; transition:transform 0.5s ease;" onerror="this.parentNode.style.display='none'">
          </div>` : `
          <div style="width:100%; height:100px; display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,0.03); border-radius:8px; margin-bottom:12px; border:1px dashed var(--border-glass)">
            <span style="font-size:2.2rem;">${c.emoji || '📜'}</span>
          </div>`}
          <div style="display:flex; flex-direction:column; justify-content:space-between; flex:1;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="tech-pill" style="font-size:0.7rem;">${(c.category || 'tech').toUpperCase()}</span>
                <span style="font-size:1.3rem;">${c.emoji || '📜'}</span>
              </div>
              <div style="font-size:0.75rem; color:var(--golden-yellow); font-weight:700; margin-bottom:2px;">${c.org}</div>
              <h3 style="font-size:0.98rem; font-weight:800; color:var(--text-main); margin-bottom:8px; line-height:1.3; overflow:hidden; text-overflow:ellipsis; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical;">${c.title}</h3>
              
              <div class="cert-skills-list" style="margin-top:0; margin-bottom:12px;">
                ${skillsList}
              </div>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:auto; font-size:0.75rem; color:var(--text-muted);">
              <span><i class="fa-regular fa-calendar"></i> ${c.date || c.year}</span>
              <span style="color:var(--emerald-primary); font-weight:600; display:flex; align-items:center; gap:4px;">
                Open Link <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:0.65rem;"></i>
              </span>
            </div>
          </div>
        </div>
      </a>
    `;
  }).join('');
}
