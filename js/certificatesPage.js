// Certificates Page Gallery, Timeline, Lightbox Modal, and Search Filtering
document.addEventListener('DOMContentLoaded', () => {
  if (typeof CERTIFICATES_DATA === 'undefined') return;

  const grid = document.getElementById('certsGrid');
  const timelineContainer = document.getElementById('certsTimeline');
  const searchInput = document.getElementById('certSearch');
  const categoryContainer = document.getElementById('certCategories');
  const sortSelect = document.getElementById('certSortSelect');
  const visibleCountEl = document.getElementById('visibleCount');
  const viewGalleryBtn = document.getElementById('viewGalleryBtn');
  const viewTimelineBtn = document.getElementById('viewTimelineBtn');

  let currentCategory = 'all';
  let currentSearch = '';
  let currentSort = 'newest';
  let currentView = 'gallery'; // 'gallery' | 'timeline'

  // Setup View Toggle
  if (viewGalleryBtn && viewTimelineBtn) {
    viewGalleryBtn.addEventListener('click', () => {
      currentView = 'gallery';
      viewGalleryBtn.classList.add('active');
      viewTimelineBtn.classList.remove('active');
      grid.style.display = 'grid';
      if (timelineContainer) timelineContainer.style.display = 'none';
      render();
    });

    viewTimelineBtn.addEventListener('click', () => {
      currentView = 'timeline';
      viewTimelineBtn.classList.add('active');
      viewGalleryBtn.classList.remove('active');
      grid.style.display = 'none';
      if (timelineContainer) timelineContainer.style.display = 'block';
      render();
    });
  }

  // Categories list
  const categories = ['all', 'named', 'tech', 'government', 'internship', 'hackerrank'];
  const categoryLabels = {
    all: 'All Certificates (102+)',
    named: '🏆 Featured Highlights',
    tech: '💻 Technical & Cloud',
    government: '🛡️ Government & Civic',
    internship: '💼 Internships',
    hackerrank: '⚡ HackerRank Skills'
  };

  if (categoryContainer) {
    categoryContainer.innerHTML = categories.map(cat => `
      <button class="tab-btn ${cat === 'all' ? 'active' : ''}" data-cat="${cat}">
        ${categoryLabels[cat] || cat}
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
    let list = [...CERTIFICATES_DATA];

    // Filter Category
    if (currentCategory !== 'all') {
      if (currentCategory === 'named') {
        list = list.filter(c => c.type === 'named');
      } else {
        list = list.filter(c => (c.category || '').toLowerCase().includes(currentCategory));
      }
    }

    // Filter Search
    if (currentSearch) {
      list = list.filter(c =>
        (c.title && c.title.toLowerCase().includes(currentSearch)) ||
        (c.org && c.org.toLowerCase().includes(currentSearch)) ||
        (c.credentialId && c.credentialId.toLowerCase().includes(currentSearch)) ||
        (c.tags && c.tags.some(t => t.toLowerCase().includes(currentSearch)))
      );
    }

    // Sort
    if (currentSort === 'newest') {
      list.sort((a, b) => (b.year || 0) - (a.year || 0));
    } else if (currentSort === 'oldest') {
      list.sort((a, b) => (a.year || 0) - (b.year || 0));
    } else if (currentSort === 'name-asc') {
      list.sort((a, b) => (a.title || '').localeCompare(b.title || ''));
    }

    if (visibleCountEl) visibleCountEl.textContent = list.length;

    if (currentView === 'gallery') {
      renderGallery(list);
    } else {
      renderTimeline(list);
    }
  }

  function renderGallery(list) {
    if (!grid) return;
    if (list.length === 0) {
      grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:60px;" class="glass">No certificates matching filter</div>`;
      return;
    }

    grid.innerHTML = list.map((c, i) => {
      const catText = (c.category || 'tech').toUpperCase();
      const cardEmoji = c.emoji || '📜';
      const skillsList = (c.skillsLearned || []).slice(0, 3).map(s => `<span class="cert-skill-tag" style="font-size:0.7rem; padding:2px 6px;">${s}</span>`).join('');
      
      const month = c.month || "—";
      const year = c.year || "—";

      return `
        <a href="${c.verifyLink || '#'}" target="_blank" rel="noopener" class="cert-card-anchor" style="text-decoration:none; color:inherit; display:block; height:100%;">
          <div class="glass cert-card scroll-reveal revealed" id="cert-card-${c.id || i}" style="transition:transform 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease; overflow:hidden; border:1px solid var(--border-glass); border-radius:var(--radius-lg); display:flex; flex-direction:column; height:100%; padding:20px; cursor:pointer;">
            ${c.image && !c.image.includes('logo.svg') ? `
            <div style="width:100%; height:160px; overflow:hidden; position:relative; background:#02060d; border-radius:8px; margin-bottom:12px;">
              <img src="${c.image}" alt="${c.title}" style="width:100%; height:100%; object-fit:cover; transition:transform 0.5s ease;" onerror="this.parentNode.style.display='none'">
            </div>` : `
            <div style="width:100%; height:100px; display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,0.03); border-radius:8px; margin-bottom:12px; border:1px dashed var(--border-glass)">
              <span style="font-size:2.2rem;">${cardEmoji}</span>
            </div>`}
            
            <div style="display:flex; flex-direction:column; justify-content:space-between; flex:1;">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                  <span class="tech-pill" style="font-size:0.7rem;">${catText}</span>
                  <span style="font-size:1.3rem;">${cardEmoji}</span>
                </div>
                <div style="font-size:0.75rem; color:var(--golden-yellow); font-weight:700; margin-bottom:2px;">${c.org}</div>
                <h3 style="font-size:0.98rem; font-weight:800; color:var(--text-main); margin-bottom:8px; line-height:1.3; overflow:hidden; text-overflow:ellipsis; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical;">${c.title}</h3>
                
                <div class="cert-skills-list" style="margin-top:0; margin-bottom:12px;">
                  ${skillsList}
                </div>
              </div>
              
              <div style="display:flex; justify-content:space-between; align-items:center; margin-top:auto; font-size:0.75rem; color:var(--text-muted);">
                <span><i class="fa-regular fa-calendar"></i> ${month} ${year}</span>
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

  function renderTimeline(list) {
    if (!timelineContainer) return;
    if (list.length === 0) {
      timelineContainer.innerHTML = `<div style="text-align:center;padding:60px;" class="glass">No certificates found</div>`;
      return;
    }

    timelineContainer.innerHTML = `
      <div class="timeline-vertical">
        ${list.map((c, i) => {
          const descText = c.desc || `Professional certification in ${c.title || 'Software Development'} awarded by ${c.org || 'Verified Issuer'}.`;
          const day = c.day || (c.date && /^\d+/.test(c.date) ? c.date.match(/^\d+/)[0] : "—");
          const month = c.month || "—";
          const year = c.year || "—";
          const credId = c.credentialId || "Verified Credential";

          return `
            <div class="timeline-step ${i === 0 ? 'active' : ''}">
              <div class="timeline-dot-node"></div>
              <div class="glass timeline-content-card" style="display:flex; gap:20px; flex-wrap:wrap;">
                <img src="${c.image || 'assets/logo.svg'}" alt="${c.title}" style="width:120px; height:90px; object-fit:cover; border-radius:8px; border:1px solid var(--border-glass);" onerror="this.src='assets/logo.svg'">
                <div style="flex:1; min-width:240px;">
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px; flex-wrap:wrap; gap:8px;">
                    <span class="timeline-tag-badge">${c.org || 'Verified Issuer'}</span>
                    <span style="font-size:0.8rem;color:var(--golden-yellow); font-family:var(--ff-code);">${day} ${month} ${year}</span>
                  </div>
                  <h3 class="timeline-title" style="margin-top:0;">${c.title || 'Certificate'}</h3>
                  <p style="font-size:0.9rem;color:var(--text-muted);margin-bottom:12px">${descText}</p>
                  
                  <div style="font-size:0.78rem; color:var(--text-dim); margin-bottom:12px; font-family:var(--ff-code);">
                    Credential ID: <span style="color:var(--emerald-primary);">${credId}</span>
                  </div>

                  <div class="cert-skills-list" style="margin-bottom:16px;">
                    ${(c.skillsLearned || []).map(s => `<span class="cert-skill-tag">${s}</span>`).join('')}
                  </div>

                  <a href="${c.verifyLink || '#'}" target="_blank" rel="noopener" class="btn btn-outline btn-sm ripple-btn" style="display:inline-flex; align-items:center; gap:6px; font-weight:700;">
                    <i class="fa-solid fa-arrow-up-right-from-square"></i> Open Drive Link
                  </a>
                </div>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }

  // Certificate Lightbox Modal
  window.openCertModal = function (certId) {
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
            <!-- Certificate Image Preview in Modal -->
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
                  ${(cert.skillsLearned || []).map(s => `<span class="cert-skill-tag" style="font-size:0.75rem;">${s}</span>`).join('')}
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

  render();
});
