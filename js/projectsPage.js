
// Projects Page Interactive Filtering & 3D Flip Cards
document.addEventListener('DOMContentLoaded', () => {
  if (typeof PROJECTS_DATA === 'undefined') return;

  const grid = document.getElementById('projectsGrid');
  const searchInput = document.getElementById('projectSearch');
  const categoryContainer = document.getElementById('categoryFilters');
  const techSelect = document.getElementById('techFilter');
  const sortSelect = document.getElementById('sortSelect');
  const visibleCountEl = document.getElementById('visibleCount');

  let currentCategory = 'all';
  let currentTech = 'all';
  let currentSearch = '';
  let currentSort = 'year-desc';

  // Categories list
  const categories = ['all', ...new Set(PROJECTS_DATA.map(p => p.category))];
  // Technologies list
  const allTechs = ['all', ...new Set(PROJECTS_DATA.flatMap(p => p.tech))];

  // Render category buttons
  if (categoryContainer) {
    categoryContainer.innerHTML = categories.map(cat => `
      <button class="tab-btn ${cat === 'all' ? 'active' : ''}" data-cat="${cat}">
        ${cat === 'all' ? 'All Projects' : cat}
      </button>
    `).join('');

    categoryContainer.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        categoryContainer.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentCategory = btn.getAttribute('data-cat');
        render();
      });
    });
  }

  // Populate tech select
  if (techSelect) {
    techSelect.innerHTML = allTechs.map(t => `<option value="${t}">${t === 'all' ? 'All Technologies' : t}</option>`).join('');
    techSelect.addEventListener('change', (e) => {
      currentTech = e.target.value;
      render();
    });
  }

  // Search Input
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      currentSearch = e.target.value.trim().toLowerCase();
      render();
    });
  }

  // Sort Select
  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      currentSort = e.target.value;
      render();
    });
  }

  function render() {
    let list = [...PROJECTS_DATA];

    // Filter Category
    if (currentCategory !== 'all') {
      list = list.filter(p => p.category.toLowerCase().includes(currentCategory.toLowerCase()));
    }

    // Filter Tech
    if (currentTech !== 'all') {
      list = list.filter(p => p.tech.some(t => t.toLowerCase() === currentTech.toLowerCase()));
    }

    // Search Query
    if (currentSearch) {
      list = list.filter(p =>
        p.title.toLowerCase().includes(currentSearch) ||
        p.tagline.toLowerCase().includes(currentSearch) ||
        p.desc.toLowerCase().includes(currentSearch) ||
        p.tech.some(t => t.toLowerCase().includes(currentSearch)) ||
        p.category.toLowerCase().includes(currentSearch)
      );
    }

    // Sort
    if (currentSort === 'year-desc') {
      list.sort((a, b) => b.year - a.year);
    } else if (currentSort === 'year-asc') {
      list.sort((a, b) => a.year - b.year);
    } else if (currentSort === 'name-asc') {
      list.sort((a, b) => a.title.localeCompare(b.title));
    }

    if (visibleCountEl) visibleCountEl.textContent = list.length;

    if (!grid) return;

    if (list.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align:center; padding: 60px 20px;" class="glass">
          <i class="fa-solid fa-folder-open" style="font-size: 3rem; color: var(--emerald-primary); margin-bottom: 16px;"></i>
          <h3>No matching projects found</h3>
          <p style="color: var(--text-muted); margin-top: 8px;">Try clearing your search query or selecting a different category filter.</p>
        </div>
      `;
      return;
    }
    // Separate Featured projects dynamically to the top (only those with cover images)
    const showcaseMatches = list.filter(p => p.featured === true && p.image);
    const regularMatches = list.filter(p => !(p.featured === true && p.image));

    let html = '';

    // Render Showcase Projects
    showcaseMatches.forEach(p => {
      html += `
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
                  <i class="fa-solid ${p.icon || 'fa-laptop-code'}" style="font-size:3.5rem; color:var(--emerald-primary)"></i>
                </div>
              `}
            </div>

            <h3 class="project-title" style="margin-top:0; font-size:1.4rem;">${p.title}</h3>
            <p class="project-tagline" style="margin-bottom:16px; font-size:0.92rem; color:var(--text-muted); flex:1;">${p.tagline}</p>
            
            <!-- Statistics Row -->
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:8px; margin-bottom:16px;">
              ${Object.entries(p.stats || {}).slice(0, 3).map(([lbl, val]) => `
                <div style="background:var(--bg-main); border:1px solid var(--border-glass); border-radius:var(--radius-sm); padding:6px; text-align:center;">
                  <div style="font-size:0.6rem; color:var(--text-muted); text-transform:uppercase;">${lbl}</div>
                  <div style="font-size:0.8rem; font-weight:700; color:var(--emerald-primary); margin-top:2px;">${val}</div>
                </div>
              `).join('')}
            </div>

            <div class="project-tech-pills" style="margin-bottom:20px; gap:6px;">
              ${p.tech.slice(0, 5).map(t => `<span class="tech-pill" style="font-size:0.75rem;">${t}</span>`).join('')}
              ${p.tech.length > 5 ? `<span class="tech-pill" style="font-size:0.75rem;">+${p.tech.length - 5}</span>` : ''}
            </div>

            <div style="display:flex; gap:10px; margin-top:auto;">
              <button class="btn btn-primary btn-sm ripple-btn" onclick="openPremiumProjectModal(${p.id})" style="flex:1; font-weight:700; height:38px;">
                <i class="fa-solid fa-book-open"></i> Read More
              </button>
              ${p.live ? `<a href="${p.live}" target="_blank" rel="noopener" class="btn btn-outline btn-sm ripple-btn" style="width:38px; height:38px; display:flex; align-items:center; justify-content:center;"><i class="fa-solid fa-arrow-up-right-from-square"></i></a>` : ''}
              <a href="${p.github}" target="_blank" rel="noopener" class="btn btn-outline btn-sm ripple-btn" style="width:38px; height:38px; display:flex; align-items:center; justify-content:center;"><i class="fa-brands fa-github"></i></a>
            </div>
          </div>
        </div>
      `;
    });

    // Render Regular Projects
    regularMatches.forEach(p => {
      html += `
        <div class="glass flip-card" id="project-card-${p.id}">
          <div class="flip-card-inner">
            <!-- CARD FRONT -->
            <div class="flip-card-front">
              <div>
                <div class="project-card-header">
                  <div class="project-icon-box"><i class="fa-solid ${p.icon}"></i></div>
                  ${p.featured ? '<span class="project-featured-tag">★ Featured</span>' : `<span class="tech-pill">${p.category}</span>`}
                </div>
                <h3 class="project-title">${p.title}</h3>
                <p class="project-tagline">${p.tagline}</p>
                <div class="project-tech-pills">
                  ${p.tech.map(t => `<span class="tech-pill">${t}</span>`).join('')}
                </div>
              </div>
              <div style="font-size:0.82rem;color:var(--text-muted);display:flex;justify-content:space-between;align-items:center">
                <span>Status: <strong style="color:var(--emerald-primary)">${p.status}</strong></span>
                <span>Year: <strong>${p.year}</strong></span>
              </div>
            </div>

            <!-- CARD BACK -->
            <div class="flip-card-back">
              <div>
                <div style="display:flex;justify-content:space-between;align-items:center">
                  <span class="project-featured-tag">${p.category}</span>
                  <span style="font-size:0.8rem;color:var(--golden-yellow)">Year ${p.year}</span>
                </div>
                <h3 class="project-title" style="margin-top:10px">${p.title}</h3>
                <p style="font-size:0.9rem;color:var(--text-muted);margin-bottom:16px;line-height:1.5">${p.desc}</p>
                <div class="project-tech-pills" style="margin-bottom:20px">
                  ${p.tech.map(t => `<span class="tech-pill">${t}</span>`).join('')}
                </div>
              </div>
              <div class="project-links-row">
                ${p.live ? `<a href="${p.live}" target="_blank" rel="noopener" class="btn btn-primary btn-sm" style="flex:1"><i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo</a>` : ''}
                <a href="${p.github}" target="_blank" rel="noopener" class="btn btn-outline btn-sm" style="flex:1"><i class="fa-brands fa-github"></i> GitHub</a>
              </div>
            </div>
          </div>
        </div>
      `;
    });

    grid.innerHTML = html;
    initTiltEffects();
    initRipples();
  }

  // 3D Tilt Effect on Featured Cards
  function initTiltEffects() {
    const cards = document.querySelectorAll('.featured-project-card');
    cards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const xc = rect.width / 2;
        const yc = rect.height / 2;
        // Sensitivity control
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

  // Ripple click effect for buttons
  function initRipples() {
    const btns = document.querySelectorAll('.ripple-btn');
    btns.forEach(btn => {
      btn.addEventListener('click', function(e) {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const ripple = document.createElement('span');
        ripple.className = 'click-ripple';
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        
        btn.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);
      });
    });
  }

  // Premium Project Detailed Modal Controls
  window.openPremiumProjectModal = function(id) {
    const p = PROJECTS_DATA.find(item => item.id === id);
    if (!p) return;

    let modal = document.getElementById('premiumProjectModal');
    if (!modal) {
      modal = document.createElement('div');
      modal.className = 'premium-modal-overlay';
      modal.id = 'premiumProjectModal';
      document.body.appendChild(modal);
    }

    modal.innerHTML = `
      <div class="premium-modal-box">
        <div class="premium-modal-header">
          <div style="display:flex; align-items:center; gap:12px;">
            <div class="project-icon-box" style="width:40px; height:40px; font-size:1.1rem; border-radius:10px;"><i class="fa-solid ${p.icon}"></i></div>
            <div>
              <h2 style="font-size:1.3rem; font-weight:800; color: var(--text-main); margin-bottom: 2px;">${p.title}</h2>
              <span style="font-size:0.75rem; color:var(--text-muted);">${p.category} &bull; Year ${p.year} &bull; Status: <strong style="color:var(--emerald-primary);">${p.status}</strong></span>
            </div>
          </div>
          <button class="premium-modal-close" onclick="closePremiumProjectModal()"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div class="premium-modal-body">
          <!-- Left Side: Image & Stats -->
          <div class="premium-modal-left">
            <img class="modal-project-img" src="${p.image}" alt="${p.title}">
            <div class="modal-project-stats">
              ${Object.entries(p.stats || {}).map(([lbl, val]) => `
                <div class="modal-stat-card">
                  <div class="modal-stat-label">${lbl}</div>
                  <div class="modal-stat-val">${val}</div>
                </div>
              `).join('')}
            </div>
            <div style="display:flex; gap:12px; margin-top:12px;">
              ${p.live ? `<a href="${p.live}" target="_blank" rel="noopener" class="btn btn-primary ripple-btn" style="flex:1; text-align:center; display:flex; align-items:center; justify-content:center; gap:6px;"><i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo</a>` : ''}
              <a href="${p.github}" target="_blank" rel="noopener" class="btn btn-outline ripple-btn" style="flex:1; text-align:center; display:flex; align-items:center; justify-content:center; gap:6px;"><i class="fa-brands fa-github"></i> GitHub</a>
            </div>
          </div>
          
          <!-- Right Side: Details Tabs -->
          <div>
            <div class="modal-tabs-nav">
              <button class="modal-tab-btn active" onclick="switchModalTab(event, 'overview-tab')">Overview</button>
              <button class="modal-tab-btn" onclick="switchModalTab(event, 'architecture-tab')">Architecture</button>
              <button class="modal-tab-btn" onclick="switchModalTab(event, 'features-tab')">Features</button>
              <button class="modal-tab-btn" onclick="switchModalTab(event, 'structure-tab')">Structure</button>
              <button class="modal-tab-btn" onclick="switchModalTab(event, 'roadmap-tab')">Future Scope</button>
            </div>
            
            <!-- Tab Contents -->
            <div id="overview-tab" class="modal-tab-content active">
              <h4 style="margin-bottom:8px; color:var(--emerald-primary); font-weight:700;">Project Overview</h4>
              <p style="color:var(--text-muted); font-size:0.95rem;">${p.overview || p.desc}</p>
              <h4 style="margin-top:16px; margin-bottom:8px; color:var(--purple-accent); font-weight:700;">Development Timeline</h4>
              <ul class="modal-bullets-list">
                ${(p.timeline || []).map(t => `<li style="font-size:0.9rem;">${t}</li>`).join('')}
              </ul>
            </div>
            
            <div id="architecture-tab" class="modal-tab-content">
              <h4 style="margin-bottom:8px; color:var(--emerald-primary); font-weight:700;">Architecture & Design Pattern</h4>
              <p style="color:var(--text-muted); font-size:0.95rem;">${p.architecture || 'Built using high-performance components and design systems.'}</p>
              <h4 style="margin-top:16px; margin-bottom:8px; color:var(--golden-yellow); font-weight:700;">Tech Stack Used</h4>
              <div class="project-tech-pills">
                ${p.tech.map(t => `<span class="tech-pill">${t}</span>`).join('')}
              </div>
            </div>
            
            <div id="features-tab" class="modal-tab-content">
              <h4 style="margin-bottom:8px; color:var(--emerald-primary); font-weight:700;">Core Features Included</h4>
              <ul class="modal-bullets-list" style="list-style:none; padding-left:0;">
                ${(p.features || []).map(f => `<li style="margin-bottom:8px; font-size:0.9rem; color:var(--text-muted);"><i class="fa-solid fa-circle-check" style="color:var(--emerald-primary); margin-right:8px;"></i> ${f}</li>`).join('')}
              </ul>
            </div>
            
            <div id="structure-tab" class="modal-tab-content">
              <h4 style="margin-bottom:8px; color:var(--emerald-primary); font-weight:700;">Project Structure & File Modules</h4>
              <ul class="modal-bullets-list" style="font-family:var(--ff-code); font-size:0.82rem; list-style:none; padding-left:0;">
                ${(p.structure || []).map(s => `<li style="margin-bottom:6px; color:var(--text-muted);"><i class="fa-solid fa-file-code" style="color:var(--purple-accent); margin-right:8px;"></i> ${s}</li>`).join('')}
              </ul>
            </div>
            
            <div id="roadmap-tab" class="modal-tab-content">
              <h4 style="margin-bottom:8px; color:var(--emerald-primary); font-weight:700;">Future Roadmap & Scope</h4>
              <ul class="modal-bullets-list" style="list-style:none; padding-left:0;">
                ${(p.futureScope || p.futureImprovements || []).map(item => `<li style="margin-bottom:8px; font-size:0.9rem; color:var(--text-muted);"><i class="fa-solid fa-rocket" style="color:var(--golden-yellow); margin-right:8px;"></i> ${item}</li>`).join('')}
              </ul>
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

  window.closePremiumProjectModal = function() {
    const modal = document.getElementById('premiumProjectModal');
    if (modal) {
      modal.classList.remove('active');
      document.body.classList.remove('no-scroll');
    }
  };

  window.switchModalTab = function(e, tabId) {
    const container = e.target.closest('.premium-modal-box');
    container.querySelectorAll('.modal-tab-btn').forEach(btn => btn.classList.remove('active'));
    container.querySelectorAll('.modal-tab-content').forEach(tab => tab.classList.remove('active'));
    
    e.target.classList.add('active');
    document.getElementById(tabId).classList.add('active');
  };

  // Auto-open modal if project ID is in URL query parameters
  const urlParams = new URLSearchParams(window.location.search);
  const projectIdParam = urlParams.get('id');
  if (projectIdParam) {
    const projId = parseInt(projectIdParam);
    if (!isNaN(projId)) {
      setTimeout(() => {
        openPremiumProjectModal(projId);
      }, 350);
    }
  }

  render();
});
