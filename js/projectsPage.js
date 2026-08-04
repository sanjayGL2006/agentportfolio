
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
      list = list.filter(p => p.category.toLowerCase() === currentCategory.toLowerCase());
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

    grid.innerHTML = list.map(p => `
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
    `).join('');
  }

  render();
});
