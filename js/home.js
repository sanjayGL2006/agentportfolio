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

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.getAttribute('data-count'));
        const suffix = el.getAttribute('data-suffix') || '';
        let current = 0;
        const step = Math.ceil(target / 40);

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

// Skills Filter & Progress Bars
function initSkillsTabs() {
  const tabs = document.querySelectorAll('.tab-btn');
  const cards = document.querySelectorAll('.skill-card-item');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const cat = tab.getAttribute('data-cat');
      cards.forEach(card => {
        if (cat === 'all' || card.getAttribute('data-cat') === cat) {
          card.style.display = 'flex';
          setTimeout(() => {
            const fill = card.querySelector('.progress-fill');
            if (fill) fill.style.width = fill.getAttribute('data-level') + '%';
          }, 50);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Trigger progress fill on scroll
  const fillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const fill = entry.target;
        fill.style.width = fill.getAttribute('data-level') + '%';
      }
    });
  }, { threshold: 0.2 });

  document.querySelectorAll('.progress-fill').forEach(fill => fillObserver.observe(fill));
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

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const nameInput = document.getElementById('contactName');
    const name = nameInput ? nameInput.value.trim() : 'Visitor';
    
    if (window.ToastManager) {
      window.ToastManager.show(`Thank you, ${name}! Your message has been sent successfully.`, 'success', 'fa-paper-plane');
    }
    form.reset();
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
    modal.className = 'modal-overlay';
    modal.id = 'certModal';
    document.body.appendChild(modal);
  }

  modal.innerHTML = `
    <div class="modal-box">
      <button class="modal-close-btn" onclick="closeCertModal()"><i class="fa-solid fa-xmark"></i></button>
      <div style="display:flex;align-items:center;gap:16px;margin-bottom:20px">
        <div style="font-size:2.5rem">${cert.emoji || '📜'}</div>
        <div>
          <div class="cert-org-name">${cert.org}</div>
          <h2 style="font-size:1.4rem;font-weight:800">${cert.title}</h2>
        </div>
      </div>

      <div style="background:var(--bg-main);border-radius:12px;padding:16px;margin-bottom:20px;border:1px solid var(--border-glass)">
        <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:8px"><strong>Date Issued:</strong> ${cert.date}</div>
        <div style="font-size:0.85rem;color:var(--text-muted);margin-bottom:8px"><strong>Credential ID:</strong> <span style="font-family:var(--ff-code);color:var(--emerald-primary)">${cert.credentialId}</span></div>
        <div style="font-size:0.85rem;color:var(--text-muted)"><strong>Skills Certified:</strong> ${cert.skillsLearned ? cert.skillsLearned.join(', ') : 'Software Development'}</div>
      </div>

      <p style="font-size:0.95rem;color:var(--text-muted);line-height:1.6;margin-bottom:24px">${cert.desc}</p>

      <div style="display:flex;gap:16px;flex-wrap:wrap">
        <a href="${cert.verifyLink}" target="_blank" rel="noopener" class="btn btn-primary" style="flex:1">
          <i class="fa-solid fa-arrow-up-right-from-square"></i> Verify Official Credential
        </a>
        <button class="btn btn-outline" onclick="closeCertModal()">Close Window</button>
      </div>
    </div>
  `;

  setTimeout(() => modal.classList.add('active'), 10);
};

window.closeCertModal = function () {
  const modal = document.getElementById('certModal');
  if (modal) {
    modal.classList.remove('active');
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

  const featured = PROJECTS_DATA.filter(p => p.featured).slice(0, 6);
  grid.innerHTML = featured.map(p => `
    <div class="glass flip-card" data-aos="fade-up">
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <div>
            <div class="project-card-header">
              <div class="project-icon-box"><i class="fa-solid ${p.icon}"></i></div>
              <span class="project-featured-tag">★ Featured</span>
            </div>
            <h3 class="project-title">${p.title}</h3>
            <p class="project-tagline">${p.tagline}</p>
            <div class="project-tech-pills">
              ${p.tech.map(t => `<span class="tech-pill">${t}</span>`).join('')}
            </div>
          </div>
          <div style="font-size:0.8rem;color:var(--text-muted);display:flex;justify-content:space-between">
            <span>Category: ${p.category}</span>
            <span>Year: ${p.year}</span>
          </div>
        </div>
        <div class="flip-card-back">
          <div>
            <span class="project-featured-tag">${p.category}</span>
            <h3 class="project-title" style="margin-top:10px">${p.title}</h3>
            <p style="font-size:0.9rem;color:var(--text-muted);margin-bottom:16px;line-height:1.5">${p.desc}</p>
            <div class="project-tech-pills">
              ${p.tech.map(t => `<span class="tech-pill">${t}</span>`).join('')}
            </div>
          </div>
          <div class="project-links-row">
            ${p.live ? `<a href="${p.live}" target="_blank" class="btn btn-primary btn-sm" style="flex:1"><i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo</a>` : ''}
            <a href="${p.github}" target="_blank" class="btn btn-outline btn-sm" style="flex:1"><i class="fa-brands fa-github"></i> GitHub</a>
          </div>
        </div>
      </div>
    </div>
  `).join('');
}

// Render Featured Certificates Preview on Home Page
function renderHomeFeaturedCertificates() {
  const grid = document.getElementById('homeFeaturedCertsGrid');
  if (!grid || typeof CERTIFICATES_DATA === 'undefined') return;

  const featured = CERTIFICATES_DATA.filter(c => c.featured || c.type === 'named').slice(0, 6);
  grid.innerHTML = featured.map((c, i) => {
    const catText = (c.category || 'tech').toUpperCase();
    const descText = (c.desc || `Professional certification in ${c.title || 'Software Development'} awarded by ${c.org || 'Verified Issuer'}.`).substring(0, 110);
    return `
      <div class="glass cert-card" id="home-cert-card-${i}">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:flex-start">
            <div class="cert-badge-icon">${c.emoji || '📜'}</div>
            <span class="tech-pill">${catText}</span>
          </div>
          <div class="cert-org-name">${c.org || 'Verified Issuer'}</div>
          <h3 class="cert-title-name">${c.title || 'Certificate'}</h3>
          <div class="cert-date-text"><i class="fa-regular fa-calendar"></i> ${c.date || c.year || 'Verified'}</div>
          <p style="font-size:0.85rem;color:var(--text-muted);margin-bottom:16px;line-height:1.5">${descText}...</p>
        </div>

        <div style="display:flex;gap:10px;margin-top:16px">
          <button class="btn btn-primary btn-sm" style="flex:1" onclick="openCertModal('${c.id}')">
            <i class="fa-solid fa-eye"></i> View Credential
          </button>
          <a href="${c.verifyLink || '#'}" target="_blank" rel="noopener" class="icon-btn" style="width:36px;height:36px" title="Verify Online">
            <i class="fa-solid fa-arrow-up-right-from-square"></i>
          </a>
        </div>
      </div>
    `;
  }).join('');
}
