// Command Palette (Ctrl + K / Cmd + K)
(function () {
  let modal, input, list;
  let isOpen = false;

  const COMMANDS = [
    { title: "Home Page", desc: "Navigate to portfolio home", action: () => window.location.href = "index.html#home", icon: "fa-house" },
    { title: "All Projects (23)", desc: "Explore all 23 software projects", action: () => window.location.href = "projects.html", icon: "fa-diagram-project" },
    { title: "Certificates (102+)", desc: "View all technical & government certificates", action: () => window.location.href = "certificates.html", icon: "fa-certificate" },
    { title: "Docker Roadmap", desc: "View Docker containerization learning status", action: () => window.location.href = "index.html#docker", icon: "fa-box" },
    { title: "Technical Skills", desc: "Check skills in Python, React, JS, MySQL, Cloud", action: () => window.location.href = "index.html#skills", icon: "fa-code" },
    { title: "Download Resume", desc: "Download Sanjay G. L. Resume PDF", action: () => window.open("assets/Sanjay_GL_Resume.pdf", "_blank"), icon: "fa-file-pdf" },
    { title: "GitHub Profile", desc: "Visit github.com/sanjayGL2006", action: () => window.open("https://github.com/sanjayGL2006", "_blank"), icon: "fa-brands fa-github" },
    { title: "LinkedIn Profile", desc: "Connect on LinkedIn", action: () => window.open("https://linkedin.com/in/sanjaygl2006", "_blank"), icon: "fa-brands fa-linkedin" },
    { title: "Toggle Dark/Light Mode", desc: "Switch color theme palette", action: () => window.toggleTheme(), icon: "fa-circle-half-stroke" },
    { title: "Contact Sanjay", desc: "Send email or get contact info", action: () => window.location.href = "index.html#contact", icon: "fa-envelope" }
  ];

  document.addEventListener('DOMContentLoaded', () => {
    initCmdPalette();
  });

  function initCmdPalette() {
    modal = document.createElement('div');
    modal.className = 'cmd-palette-modal';
    modal.id = 'cmd-palette';
    modal.innerHTML = `
      <div class="cmd-palette-box">
        <div class="cmd-input-row">
          <i class="fa-solid fa-terminal"></i>
          <input type="text" class="cmd-search-input" id="cmdInput" placeholder="Type a command or search..." autocomplete="off">
          <kbd style="font-size:0.75rem;padding:2px 6px;background:var(--bg-main);border-radius:4px;color:var(--emerald-primary)">ESC</kbd>
        </div>
        <div class="cmd-results-list" id="cmdList"></div>
      </div>
    `;

    document.body.appendChild(modal);

    input = document.getElementById('cmdInput');
    list = document.getElementById('cmdList');

    modal.addEventListener('click', (e) => {
      if (e.target === modal) toggle(false);
    });

    input.addEventListener('input', () => filterCommands(input.value.trim().toLowerCase()));

    const triggerBtn = document.getElementById('cmdPaletteTrigger');
    if (triggerBtn) {
      triggerBtn.addEventListener('click', () => toggle(true));
    }

    renderList(COMMANDS);
  }

  function toggle(state = null) {
    isOpen = state !== null ? state : !isOpen;
    modal.classList.toggle('active', isOpen);
    if (isOpen) {
      input.value = '';
      filterCommands('');
      input.focus();
    }
  }

  function filterCommands(query) {
    if (!query) {
      renderList(COMMANDS);
      return;
    }
    const filtered = COMMANDS.filter(c => c.title.toLowerCase().includes(query) || c.desc.toLowerCase().includes(query));
    renderList(filtered);
  }

  function renderList(items) {
    list.innerHTML = '';
    if (items.length === 0) {
      list.innerHTML = `<div style="padding:20px;text-align:center;color:var(--text-muted)">No matching commands found</div>`;
      return;
    }

    items.forEach((item, index) => {
      const el = document.createElement('div');
      el.className = 'cmd-item';
      el.innerHTML = `
        <div style="display:flex;align-items:center;gap:12px">
          <i class="${item.icon.includes('fa-') ? item.icon : 'fa-solid ' + item.icon}"></i>
          <div>
            <div style="font-weight:600;color:var(--text-main)">${item.title}</div>
            <div style="font-size:0.8rem;color:var(--text-muted)">${item.desc}</div>
          </div>
        </div>
        <i class="fa-solid fa-chevron-right" style="font-size:0.75rem"></i>
      `;

      el.addEventListener('click', () => {
        toggle(false);
        item.action();
      });

      list.appendChild(el);
    });
  }

  window.CommandPalette = { toggle };
})();
