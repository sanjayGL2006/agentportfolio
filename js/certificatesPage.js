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
      const descText = (c.desc || `Professional certification in ${c.title || 'Software Development'} awarded by ${c.org || 'Verified Issuer'}.`).substring(0, 120);
      return `
        <div class="glass cert-card" id="cert-card-${i}">
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
          return `
            <div class="timeline-step ${i === 0 ? 'active' : ''}">
              <div class="timeline-dot-node"></div>
              <div class="glass timeline-content-card">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
                  <span class="timeline-tag-badge">${c.org || 'Verified Issuer'}</span>
                  <span style="font-size:0.8rem;color:var(--golden-yellow)">${c.date || c.year || 'Verified'}</span>
                </div>
                <h3 class="timeline-title">${c.title || 'Certificate'}</h3>
                <p style="font-size:0.9rem;color:var(--text-muted);margin-bottom:12px">${descText}</p>
                <button class="btn btn-outline btn-sm" onclick="openCertModal('${c.id}')">
                  <i class="fa-solid fa-expand"></i> Inspect Certificate Details
                </button>
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

  render();
});
