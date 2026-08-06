// AI Assistant Chatbot powered by knowledge.json
(function () {
  let knowledgeData = null;
  let isOpen = false;

  document.addEventListener('DOMContentLoaded', () => {
    initChatbot();
    fetchKnowledge();
  });

  async function fetchKnowledge() {
    try {
      const res = await fetch('knowledge.json');
      knowledgeData = await res.json();
    } catch (e) {
      console.warn("Using fallback knowledge data for AI Chatbot");
    }
  }

  function initChatbot() {
    const widget = document.createElement('div');
    widget.className = 'ai-chatbot-widget';
    widget.innerHTML = `
      <button class="ai-trigger-btn" id="aiChatTrigger" aria-label="Open AI Assistant">
        <div class="ai-pulse-ring"></div>
        <i class="fa-solid fa-robot"></i>
      </button>

      <div class="chat-window" id="aiChatWindow">
        <div class="chat-header">
          <div class="chat-header-info">
            <i class="fa-solid fa-brain"></i>
            <div>
              <h4 style="font-size:0.95rem;font-weight:700">SANJAY AI OS v2.0</h4>
              <span style="font-size:0.75rem;color:var(--emerald-primary)">Online · Trained on Portfolio Data</span>
            </div>
          </div>
          <button class="icon-btn" id="aiChatCloseBtn" style="width:30px;height:30px;font-size:0.8rem"><i class="fa-solid fa-xmark"></i></button>
        </div>

        <div class="chat-body" id="chatBody">
          <div class="chat-msg bot">
            👋 Hi! I am Sanjay's AI Assistant. Ask me anything about his projects, 102+ certificates, Docker learning journey, skills, or experience!
          </div>
        </div>

        <div class="chat-chips-row" style="display:flex; flex-wrap:wrap; gap:6px; padding: 8px 12px; height:auto; overflow-y:visible;">
          <button class="chip-prompt" data-q="Show Featured Projects">⭐ Featured Projects</button>
          <button class="chip-prompt" data-q="Tell me about Sai AI Assistant">🤖 Sai Assistant</button>
          <button class="chip-prompt" data-q="Tell me about Accident Risk Prediction">🚦 Accident Prediction</button>
          <button class="chip-prompt" data-q="Show AI Projects">🧠 AI Projects</button>
          <button class="chip-prompt" data-q="Show Machine Learning Projects">📊 ML Projects</button>
          <button class="chip-prompt" data-q="Contact Sanjay">Contact</button>
        </div>

        <form class="chat-footer" id="chatForm">
          <input type="text" class="chat-input" id="chatInput" placeholder="Ask AI Assistant..." autocomplete="off">
          <button type="submit" class="btn btn-primary btn-sm" style="padding:8px 16px"><i class="fa-solid fa-paper-plane"></i></button>
        </form>
      </div>
    `;

    document.body.appendChild(widget);

    const trigger = document.getElementById('aiChatTrigger');
    const closeBtn = document.getElementById('aiChatCloseBtn');
    const windowEl = document.getElementById('aiChatWindow');
    const form = document.getElementById('chatForm');
    const input = document.getElementById('chatInput');

    trigger.addEventListener('click', () => toggleChat());
    closeBtn.addEventListener('click', () => toggleChat(false));

    function toggleChat(state = null) {
      isOpen = state !== null ? state : !isOpen;
      windowEl.classList.toggle('active', isOpen);
      if (isOpen) input.focus();
    }

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const q = input.value.trim();
      if (!q) return;
      handleUserQuery(q);
      input.value = '';
    });

    document.querySelectorAll('.chip-prompt').forEach(chip => {
      chip.addEventListener('click', () => {
        const q = chip.getAttribute('data-q');
        handleUserQuery(q);
      });
    });
  }

  function handleUserQuery(query) {
    appendMessage(query, 'user');

    // Show typing dots
    const typingMsg = document.createElement('div');
    typingMsg.className = 'chat-msg bot typing-dots';
    typingMsg.innerHTML = '<span>.</span><span>.</span><span>.</span>';
    const body = document.getElementById('chatBody');
    body.appendChild(typingMsg);
    body.scrollTop = body.scrollHeight;

    setTimeout(() => {
      typingMsg.remove();
      const ans = generateAnswer(query.toLowerCase());
      appendMessage(ans, 'bot');
    }, 600);
  }

  function appendMessage(text, sender) {
    const body = document.getElementById('chatBody');
    const msg = document.createElement('div');
    msg.className = `chat-msg ${sender}`;
    msg.innerHTML = text;
    body.appendChild(msg);
    body.scrollTop = body.scrollHeight;
  }

  function generateAnswer(q) {
    if (q.includes('featured') && q.includes('project')) {
      return "Sanjay's ⭐ <strong>Featured Projects</strong> represent his top-tier work:<br>" +
             "1. 🧠 <strong>Sindhanai Full Stack AI</strong>: Content workspace & WebSocket chat using React, Node.js, Express, MongoDB, Gemini API.<br>" +
             "2. 🔬 <strong>DERMAIT Skin Care AI</strong>: Dermatology triage utility using CNN Keras, Flask, OpenCV (94% accuracy).<br>" +
             "3. 💵 <strong>Billing Management System</strong>: Desktop checkout & PDF billing tool using HTML/CSS/JS, SQLite, Electron.js, PDFKit.<br>" +
             "4. 🚦 <strong>Accident Risk Prediction</strong>: Road safety dashboard with Random Forest model (98% accuracy), Flask, Scikit-learn.<br>" +
             "5. 🤖 <strong>Sai AI Assistant</strong>: Gemini chat assistant with educational Q&A and news widget using Flask, SQLite.<br>" +
             "Explore them with premium 3D tilt cards at the top of the <a href='projects.html' style='color:var(--emerald-primary)'>Projects Page</a>!";
    }
    if (q.includes('sindhanai') || (q.includes('content') && q.includes('generation'))) {
      return "🧠 <strong>Sindhanai Full Stack AI (2026)</strong> is a premium AI-driven workspace:<br>" +
             "&bull; <strong>Tech Stack:</strong> React, Node.js, Express, MongoDB, Google Gemini API, Tailwind CSS, JWT.<br>" +
             "&bull; <strong>Features:</strong> Text editor, automatic document summary, WebSocket streaming chat, code snippets exporter, database query caches, and secure user logins.<br>" +
             "&bull; <strong>Stats:</strong> Gemini Pro Engine, API latency &lt; 800ms, JWT Auth Model.<br>" +
             "Explore it on the <a href='projects.html?id=26' style='color:var(--emerald-primary)'>Projects Page</a>!";
    }
    if (q.includes('dermait') || q.includes('skin') || q.includes('dermatology')) {
      return "🔬 <strong>DERMAIT Skin Care AI (2026)</strong> is a deep learning healthcare utility:<br>" +
             "&bull; <strong>Tech Stack:</strong> Python, Flask, TensorFlow, Keras, OpenCV, Scikit-image, JavaScript, Chart.js.<br>" +
             "&bull; <strong>Features:</strong> Image uploads diagnostic scan, CNN lesion classification, Chart.js probability curves, and clinical warning reports.<br>" +
             "&bull; <strong>Stats:</strong> 94% Model Accuracy, inference speed &lt; 120ms, Keras model.<br>" +
             "Explore it on the <a href='projects.html?id=27' style='color:var(--emerald-primary)'>Projects Page</a>!";
    }
    if (q.includes('billing') || q.includes('invoice') || q.includes('checkout')) {
      return "💵 <strong>Billing Management System (2025)</strong> is a retail desktop manager application:<br>" +
             "&bull; <strong>Tech Stack:</strong> HTML5, CSS3, JavaScript, SQLite, Node.js, Electron.js, PDFKit, Chart.js.<br>" +
             "&bull; <strong>Features:</strong> Desktop framing wrapper, local offline store database, invoice PDFKit print creation, low-stock checks, and sales dashboards.<br>" +
             "&bull; <strong>Stats:</strong> SQLite Local DB, PDF File Export, checkout processing &lt; 5ms.<br>" +
             "Explore it on the <a href='projects.html?id=28' style='color:var(--emerald-primary)'>Projects Page</a>!";
    }
    if (q.includes('sai') || q.includes('sai assistant')) {
      return "🤖 <strong>Sai AI Assistant (2026)</strong> is an intelligent virtual companion:<br>" +
             "&bull; <strong>Tech Stack:</strong> HTML, CSS, JavaScript, Python (Flask), SQLite, and Google Gemini API.<br>" +
             "&bull; <strong>Features:</strong> Chat streams, school problem solver modules, code highlight helpers, current news, WhatsApp text presets, and conversation database storage.<br>" +
             "Explore it on the <a href='projects.html?id=25' style='color:var(--emerald-primary)'>Projects Page</a>!";
    }
    if (q.includes('accident') || q.includes('risk prediction') || q.includes('road')) {
      return "🚦 <strong>Accident Risk Prediction (2026)</strong> is a Machine Learning web dashboard:<br>" +
             "&bull; <strong>Tech Stack:</strong> Flask, Scikit-learn, Pandas, NumPy, Joblib, SQLite, HTML5, CSS3, JavaScript.<br>" +
             "&bull; <strong>Features:</strong> Random Forest Classifier model, weight factors analysis, gauge meters, safety notifications, and CSV dataset logs.<br>" +
             "&bull; <strong>Stats:</strong> 98% model accuracy, &lt; 12ms inference speed, 10k+ records dataset.<br>" +
             "Explore it on the <a href='projects.html?id=24' style='color:var(--emerald-primary)'>Projects Page</a>!";
    }
    if (q.includes('who is') || q.includes('sanjay') || q.includes('about')) {
      return "<strong>Sanjay G. L.</strong> is a BCA student (3rd Year · 5th Sem) at PES Institute of Advanced Management Studies, Shivamogga, Karnataka. He is currently an AI/ML Intern at <strong>Milano Infotech</strong>. He designs scalable web platforms, machine learning models, and containerized dev environments. In his free time, he is an active NSS Volunteer.";
    }
    if (q.includes('internship') || q.includes('milano') || q.includes('experience')) {
      return "💼 Sanjay is currently doing an offline internship at <strong>Milano Infotech</strong> (Shivamogga) in the <strong>Artificial Intelligence, Machine Learning, and Python Development</strong> domains. He builds predictive ML classifiers and custom API endpoints.";
    }
    if (q.includes('learning') || q.includes('current learning') || q.includes('study')) {
      return "📚 <strong>Currently Learning Progress:</strong><br>" +
             "&bull; 🧠 <strong>Artificial Intelligence:</strong> 50% progress<br>" +
             "&bull; 🔬 <strong>Machine Learning:</strong> 40% progress<br>" +
             "&bull; 🐳 <strong>Docker (DevOps):</strong> 35% progress<br>" +
             "&bull; 🛡️ <strong>Kali Linux:</strong> 30% progress<br>" +
             "&bull; ⚛️ <strong>Electron.js:</strong> 25% progress<br>" +
             "&bull; 🦊 <strong>GitLab CI/CD:</strong> Active learning<br>" +
             "&bull; ✍️ <strong>Prompt Engineering:</strong> Active learning";
    }
    if (q.includes('goal') || q.includes('future') || q.includes('career')) {
      return "🚀 <strong>Sanjay's Future Goals:</strong><br>" +
             "&bull; Cyber Security & Threat Auditing<br>" +
             "&bull; Deep Learning & AI Architectures<br>" +
             "&bull; Cloud Native Systems & Infrastructure scaling<br>" +
             "&bull; GitLab CI/CD & DevOps Automation<br>" +
             "&bull; Enterprise System Design & AI Product Engineering";
    }
    if (q.includes('ai project') || q.includes('ai assistant') || q.includes('agent')) {
      return "Sanjay has built <strong>7+ AI Projects</strong>, including:<br>" +
             "&bull; 🧠 <strong>Sindhanai Full Stack AI</strong><br>" +
             "&bull; 🔬 <strong>DERMAIT Skin Care AI</strong><br>" +
             "&bull; 🤖 <strong>Sai AI Assistant</strong><br>" +
             "&bull; 🧩 <strong>AI Agent using Google API</strong> (Google Cloud Run)<br>" +
             "&bull; 💬 <strong>Surya Chatbot</strong><br>" +
             "&bull; 🔮 <strong>Kai Assistant</strong><br>" +
             "&bull; 🛡️ <strong>Spy Detect Pro</strong> (Security chatbot)";
    }
    if (q.includes('machine learning') || q.includes('ml')) {
      return "📊 <strong>Machine Learning Projects (2+):</strong><br>" +
             "1. 🚦 <strong>Accident Risk Prediction</strong>: Flask & Scikit-learn Random Forest model (98% accuracy) for road safety analysis.<br>" +
             "2. 🔬 <strong>DERMAIT Skin Care AI</strong>: Deep learning CNN model (94% accuracy) screening skin lesion risk levels.";
    }
    if (q.includes('react') || q.includes('frontend')) {
      return "Sanjay builds interactive React & TypeScript interfaces! Key projects include: 🎮 <strong>Digital Board Duel</strong>, 📝 <strong>Grab Notes</strong>, 🏠 <strong>Hyper Rent Local</strong>, 📊 <strong>Property Manager Dashboard</strong>, and ⚡ <strong>Sanju Portfolio Pro Hub</strong>.";
    }
    if (q.includes('certificate') || q.includes('count') || q.includes('cert')) {
      return "Sanjay has earned <strong>86 verified certificates</strong>! 🏆 Key items: Pravidhi Tech Fest Coding winner, AICTE Oasis Infobyte Star Performer web dev intern, National Road Safety Quiz, MeitY AI Quiz, HackerRank skills (React, JS, Python, SQL), and Microsoft Azure Fundamentals. Explore credentials on the <a href='certificates.html' style='color:var(--emerald-primary)'>Certificates Page</a>!";
    }
    if (q.includes('contact') || q.includes('email') || q.includes('phone') || q.includes('hire')) {
      return "📧 Email: <a href='mailto:sanjaygl2006@gmail.com' style='color:var(--emerald-primary)'>sanjaygl2006@gmail.com</a><br>📞 Phone: +91 8123981877<br>📍 Location: Shivamogga, Karnataka, India<br>💼 Status: Open to internships, full-stack, and AI dev roles!";
    }
    if (q.includes('resume') || q.includes('cv') || q.includes('download')) {
      return "📄 Download Sanjay's resume PDF <a href='assets/Sanjay_GL_Resume.pdf' target='_blank' style='color:var(--golden-yellow)'>here (Download Resume)</a>.";
    }
    if (q.includes('project') || q.includes('work') || q.includes('total')) {
      return "Sanjay has created <strong>29 total projects</strong> across AI, ML, Finance, E-Commerce, Utilities, Cybersecurity, Games, and Web Dashboards. Explore them on the <a href='projects.html' style='color:var(--emerald-primary)'>Projects Page</a>!";
    }

    return "I am trained on Sanjay G. L.'s full portfolio data. Ask me about his 29 projects, 86+ certificates, Milano Infotech internship, Docker roadmap, React & ML skills, education, or contact details!";
  }
})();
