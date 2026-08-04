// Web Audio API Ambient Synthesizer & Sound FX Engine
(function () {
  let audioCtx = null;
  let isMuted = true;
  let masterGain = null;
  let synthOsc = null;

  document.addEventListener('DOMContentLoaded', () => {
    initSoundToggle();
  });

  function initAudio() {
    if (audioCtx) return;
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AudioContext();
      masterGain = audioCtx.createGain();
      masterGain.gain.setValueAtTime(0.08, audioCtx.currentTime);
      masterGain.connect(audioCtx.destination);
    } catch (e) {
      console.warn("Web Audio API not supported");
    }
  }

  function initSoundToggle() {
    const btn = document.createElement('button');
    btn.className = 'icon-btn audio-toggle-btn';
    btn.id = 'audioToggleBtn';
    btn.setAttribute('aria-label', 'Toggle Ambient Sound');
    btn.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';

    document.body.appendChild(btn);

    btn.addEventListener('click', () => {
      initAudio();
      isMuted = !isMuted;
      btn.innerHTML = isMuted ? '<i class="fa-solid fa-volume-xmark"></i>' : '<i class="fa-solid fa-volume-high" style="color:var(--emerald-primary)"></i>';
      
      if (!isMuted && audioCtx) {
        if (audioCtx.state === 'suspended') audioCtx.resume();
        playAmbientChord();
        if (window.ToastManager) window.ToastManager.show('Ambient Audio Synth Enabled 🎵', 'info', 'fa-music');
      } else {
        stopAmbient();
        if (window.ToastManager) window.ToastManager.show('Audio Muted', 'info', 'fa-volume-xmark');
      }
    });

    // Play subtle click sounds on buttons
    document.addEventListener('click', (e) => {
      if (!isMuted && audioCtx && (e.target.closest('.btn') || e.target.closest('.icon-btn') || e.target.closest('.chip-prompt'))) {
        playClickBlip();
      }
    });
  }

  function playAmbientChord() {
    if (!audioCtx || isMuted) return;
    const freqs = [220, 277.18, 329.63, 440]; // A major 7 synth chord
    freqs.forEach(f => {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.value = f;
      gain.gain.setValueAtTime(0.015, audioCtx.currentTime);
      osc.connect(gain);
      gain.connect(masterGain);
      osc.start();
    });
  }

  function stopAmbient() {
    if (audioCtx) {
      audioCtx.suspend();
    }
  }

  function playClickBlip() {
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(440, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.08);
    gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.08);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.08);
  }
})();
