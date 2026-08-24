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
              <h4 style="font-size:0.95rem;font-weight:700">SANJAY AI OS v2.5</h4>
              <span style="font-size:0.75rem;color:var(--emerald-primary)"><i class="fa-solid fa-bolt" style="color:var(--golden-yellow)"></i> Online · Neural Co-Pilot OS</span>
            </div>
          </div>
          <button class="icon-btn" id="aiChatCloseBtn" style="width:30px;height:30px;font-size:0.8rem"><i class="fa-solid fa-xmark"></i></button>
        </div>

        <div class="chat-body" id="chatBody">
          <div class="chat-msg bot">
            ⚡ <strong>Sanjay AIOS v2.5 Initialized</strong>.<br>
            Trained on Sanjay G. L.'s (Sanju) 28+ projects, 86+ verified certificates, immediate roadmaps (Vulnerability Scanner, AI Emotion Detection, Resume Analyzer), and technical interview question bank.<br><br>
            Ask me anything or type <strong>"Initialize Interview Mode"</strong> to begin!
          </div>
        </div>

        <div class="chat-chips-row" style="display:flex; flex-wrap:wrap; gap:6px; padding: 8px 12px; height:auto; overflow-y:visible;">
          <button class="chip-prompt" data-q="Show Active Project Roadmap">🚀 Active Roadmap</button>
          <button class="chip-prompt" data-q="Initialize Interview Mode">🎯 Interview Mode</button>
          <button class="chip-prompt" data-q="What are Sanjay's top skills?">🛠️ Skillset Matrix</button>
          <button class="chip-prompt" data-q="How many certificates does Sanjay have?">🎓 86 Certificates</button>
          <button class="chip-prompt" data-q="Tell me about Sindhanai Full Stack AI">🤖 Sindhanai AI</button>
          <button class="chip-prompt" data-q="Contact Sanjay">📬 Contact Info</button>
        </div>

        <form class="chat-footer" id="chatForm">
          <input type="text" class="chat-input" id="chatInput" placeholder="Ask Sanjay AIOS v2.5..." autocomplete="off">
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

  function getSessionId() {
    let sid = sessionStorage.getItem('sanjay_agent_session_id');
    if (!sid) {
      sid = 'session_' + Math.random().toString(36).substring(2, 15) + '_' + Date.now();
      sessionStorage.setItem('sanjay_agent_session_id', sid);
    }
    return sid;
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

    fetch('/api/agent', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        message: query,
        session_id: getSessionId()
      })
    })
    .then(res => res.json())
    .then(data => {
      typingMsg.remove();
      appendMessage(data.reply, 'bot');
    })
    .catch(err => {
      console.warn("Agent chat route offline, providing client fallback:", err);
      typingMsg.remove();
      let fallbackText = "I am Sanjay's AI Assistant! You can explore his 29+ projects categorized into <strong>AI & Machine Learning</strong>, <strong>Web Applications</strong>, <strong>Tools & Security</strong>, <strong>Games</strong>, and <strong>Portfolios & Profiles</strong>. Direct messages can be sent to <strong>sanjaygl2006@gmail.com</strong>.";
      const lower = query.toLowerCase();
      if (lower.includes("contact") || lower.includes("email") || lower.includes("mail") || lower.includes("message")) {
        fallbackText = "You can contact Sanjay directly via email at <a href='mailto:sanjaygl2006@gmail.com' style='color:var(--emerald-primary)'>sanjaygl2006@gmail.com</a>, phone at +91 81239 81877, or using the contact form on this site.";
      } else if (lower.includes("project") || lower.includes("built")) {
        fallbackText = "Sanjay has built 29+ projects including DermAI, AI Agent using Google API, DataGauge, Pure Weaves E-Commerce, Property Manager Dashboard, and Paperless Office System. Check them out on the <a href='projects.html' style='color:var(--emerald-primary)'>Projects Page</a>!";
      } else if (lower.includes("skill") || lower.includes("react")) {
        fallbackText = "Sanjay specializes in React, Modern Web Development, Python (Flask/FastAPI), SQL, Cybersecurity, and AI/ML systems.";
      }
      appendMessage(fallbackText, 'bot');
    });
  }

  function appendMessage(text, sender) {
    const body = document.getElementById('chatBody');
    const msg = document.createElement('div');
    msg.className = `chat-msg ${sender}`;
    msg.innerHTML = text;
    body.appendChild(msg);
    body.scrollTop = body.scrollHeight;
  }
})();

