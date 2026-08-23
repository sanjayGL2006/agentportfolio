// Theme Manager, Visitor Counter, PWA, and Easter Eggs
(function () {
  // Theme Manager
  const savedTheme = localStorage.getItem('sanjay_portfolio_theme') || 'light';
  if (savedTheme === 'light') {
    document.body.classList.add('light-theme');
  }

  window.toggleTheme = function () {
    const isLight = document.body.classList.toggle('light-theme');
    localStorage.setItem('sanjay_portfolio_theme', isLight ? 'light' : 'dark');
    
    const icon = document.querySelector('#themeToggleBtn i');
    if (icon) {
      icon.className = isLight ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
    }

    if (window.ToastManager) {
      window.ToastManager.show(`Switched to ${isLight ? 'Light' : 'Dark'} Mode`, 'info', isLight ? 'fa-sun' : 'fa-moon');
    }
  };

  // Visitor Counter
  let visitCount = parseInt(localStorage.getItem('sanjay_portfolio_visitors') || '1428');
  if (!sessionStorage.getItem('visited')) {
    visitCount += 1;
    localStorage.setItem('sanjay_portfolio_visitors', visitCount.toString());
    sessionStorage.setItem('visited', 'true');
  }

  document.addEventListener('DOMContentLoaded', () => {
    // Sync Theme Button Icon
    const themeBtn = document.getElementById('themeToggleBtn');
    if (themeBtn) {
      themeBtn.addEventListener('click', window.toggleTheme);
      const icon = themeBtn.querySelector('i');
      if (icon) {
        icon.className = document.body.classList.contains('light-theme') ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
      }
    }

    // Set Visitor Counter text
    const visitorEl = document.getElementById('visitor-count-num');
    if (visitorEl) {
      visitorEl.textContent = visitCount.toLocaleString();
    }

    // Register / Unregister Service Worker for PWA
    if ('serviceWorker' in navigator) {
      const isLocal = Boolean(
        window.location.hostname === 'localhost' ||
        window.location.hostname === '127.0.0.1' ||
        window.location.hostname === '[::1]' ||
        window.location.hostname.endsWith('.local')
      );

      if (isLocal) {
        navigator.serviceWorker.getRegistrations().then((registrations) => {
          for (const registration of registrations) {
            registration.unregister();
          }
        }).catch(() => {});
      } else {
        navigator.serviceWorker.register('sw.js').catch(() => {});
      }
    }


    // Developer Console Welcome Message
    console.log("Welcome to Sanjay G. L. Portfolio Website!");
  });

  // Konami Code Easter Egg (↑ ↑ ↓ ↓ ← → ← → B A)
  const konamiSequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];
  let konamiIndex = 0;

  document.addEventListener('keydown', (e) => {
    if (e.keyCode === konamiSequence[konamiIndex]) {
      konamiIndex++;
      if (konamiIndex === konamiSequence.length) {
        konamiIndex = 0;
        triggerEasterEgg();
      }
    } else {
      konamiIndex = 0;
    }

    // Keyboard Shortcuts
    if ((e.ctrlKey || e.metaKey) && e.key && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (window.CommandPalette) window.CommandPalette.toggle();
    }
    if (e.key && e.key.toLowerCase() === 't' && document.activeElement && document.activeElement.tagName && !['input', 'textarea'].includes(document.activeElement.tagName.toLowerCase())) {
      window.toggleTheme();
    }
  });

  function triggerEasterEgg() {
    if (window.ToastManager) {
      window.ToastManager.show('🌟 UNLOCKED: AI OS GOD MODE ACHIEVED!', 'success', 'fa-award');
    }
    // Matrix particle explosion
    for (let i = 0; i < 50; i++) {
      const star = document.createElement('div');
      star.className = 'star-particle';
      star.textContent = '⚡';
      star.style.left = Math.random() * window.innerWidth + 'px';
      star.style.top = Math.random() * window.innerHeight + 'px';
      star.style.setProperty('--dx', (Math.random() * 200 - 100) + 'px');
      star.style.setProperty('--dy', (Math.random() * 200 - 100) + 'px');
      document.body.appendChild(star);
      setTimeout(() => star.remove(), 1000);
    }
  }
})();
