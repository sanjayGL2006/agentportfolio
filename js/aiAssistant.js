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

        <div class="chat-chips-row">
          <button class="chip-prompt" data-q="Who is Sanjay?">Who is Sanjay?</button>
          <button class="chip-prompt" data-q="Show AI projects">AI Projects?</button>
          <button class="chip-prompt" data-q="How many certificates?">Certificates?</button>
          <button class="chip-prompt" data-q="Is he learning Docker?">Docker?</button>
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
    if (q.includes('who is') || q.includes('sanjay') || q.includes('about')) {
      return "<strong>Sanjay G. L.</strong> is a passionate BCA student at PES Institute of Advanced Management Studies (PES IAMS), Shivamogga, Karnataka. He specializes in Full Stack Web Development, Artificial Intelligence, Cybersecurity, and Cloud Engineering.";
    }
    if (q.includes('ai project') || q.includes('agent') || q.includes('ai')) {
      return "Sanjay has built multiple AI projects, including: 🤖 <strong>AI Agent using Google API</strong> (deployed on Google Cloud Run), 🧠 <strong>Kai Assistant</strong>, 💬 <strong>Surya Chatbot</strong>, and AI-powered threat analysis apps like 🛡️ <strong>Spy Detect Pro</strong>.";
    }
    if (q.includes('react') || q.includes('frontend')) {
      return "Sanjay builds modern React 19 & TypeScript apps! Key React projects include: 🎮 <strong>Digital Board Duel</strong>, 📝 <strong>Grab Notes</strong>, 🏠 <strong>Hyper Rent Local</strong>, 📊 <strong>Property Manager Dashboard</strong>, and ⚡ <strong>Sanju Portfolio Pro Hub</strong>.";
    }
    if (q.includes('certificate') || q.includes('count') || q.includes('cert')) {
      return "Sanjay has earned <strong>102+ verified certificates</strong>! 🏆 Highlights include: State Level Pravidhi Coding Fest, AICTE Oasis Infobyte Star Performer, National Road Safety Quiz, MeitY AI Ethics Quiz, HackerRank certifications (React, JS, Python, SQL), and Microsoft Azure & Copilot credentials. Explore all credentials on the <a href='certificates.html' style='color:var(--emerald-primary)'>Certificates Page (102+)</a> or <a href='index.html#certificates' style='color:var(--golden-yellow)'>Home Certificates Showcase</a>!";
    }
    if (q.includes('docker') || q.includes('container')) {
      return "🐳 <strong>Yes! Sanjay is currently mastering Docker</strong>. His Docker learning roadmap covers Docker Images, Containers, Docker CLI, Docker Compose, Docker Hub, Volumes, Networking, and Container Deployment basics.";
    }
    if (q.includes('contact') || q.includes('email') || q.includes('phone') || q.includes('hire')) {
      return "📧 Email: <a href='mailto:sanjaygl2006@gmail.com' style='color:var(--emerald-primary)'>sanjaygl2006@gmail.com</a><br>📞 Phone: +91 8123981877<br>📍 Location: Shivamogga, Karnataka, India<br>💼 Status: Open to Internships & Software Engineering roles!";
    }
    if (q.includes('resume') || q.includes('cv') || q.includes('download')) {
      return "📄 You can download Sanjay's updated resume directly from the header navigation or by clicking <a href='assets/Sanjay_GL_Resume.pdf' target='_blank' style='color:var(--golden-yellow)'>here (Download Resume PDF)</a>.";
    }
    if (q.includes('project') || q.includes('work')) {
      return "Sanjay has created <strong>23 total projects</strong> across AI, Finance, E-Commerce, Utility, Cybersecurity, Games, and Web Dashboards. Check out the dedicated <a href='projects.html' style='color:var(--emerald-primary)'>Projects Page</a> to try live demos!";
    }

    return "I am trained on Sanjay G. L.'s full portfolio data. You can ask me about his 23 projects, 102+ certificates, Docker learning roadmap, React & Python skills, education at PES IAMS, or contact details!";
  }
})();
