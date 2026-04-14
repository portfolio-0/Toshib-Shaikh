/* ══════════════════════════════
   PAGE LOADER
══════════════════════════════ */
window.addEventListener('load', () => {
  const loader = document.getElementById('loader');

  setTimeout(() => {
    loader.classList.add('hidden');
    document.body.classList.add('loaded');

    // Stagger hero elements after load
    const heroEls = document.querySelectorAll('.reveal-tag, .reveal-title, .reveal-fade');
    heroEls.forEach((el, i) => {
      setTimeout(() => el.classList.add('visible'), 200 + i * 160);
    });
  }, 1000);
});

/* ══════════════════════════════
   SCROLL REVEAL (blur + scale)
══════════════════════════════ */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

/* ══════════════════════════════
   COUNT-UP ANIMATION
══════════════════════════════ */
function countUp(el) {
  const raw   = el.textContent.trim();
  const num   = parseFloat(raw.replace(/[^0-9.]/g, ''));
  const suffix = raw.replace(/[0-9.]/g, '');
  if (isNaN(num)) return;

  const duration = 1400;
  const start    = performance.now();

  const tick = (now) => {
    const elapsed  = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // ease out expo
    const eased    = 1 - Math.pow(1 - progress, 4);
    const current  = Math.round(eased * num * 10) / 10;
    el.textContent = (Number.isInteger(num) ? Math.round(current) : current.toFixed(1)) + suffix;
    if (progress < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}

const countObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      countUp(entry.target);
      countObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-box .num, .ci-num, .cf-subs').forEach(el => {
  countObserver.observe(el);
});

/* ══════════════════════════════
   NAV SCROLL SHRINK
══════════════════════════════ */
const nav = document.querySelector('nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    nav.style.padding = '10px 22px';
    nav.style.boxShadow = '0 12px 48px rgba(0,0,0,0.45)';
  } else {
    nav.style.padding = '';
    nav.style.boxShadow = '';
  }
}, { passive: true });

/* ══════════════════════════════
   CARD TILT ON HOVER
══════════════════════════════ */
document.querySelectorAll('.service-card, .client-card, .stat-box').forEach(card => {
  card.addEventListener('mousemove', e => {
    const rect   = card.getBoundingClientRect();
    const x      = e.clientX - rect.left;
    const y      = e.clientY - rect.top;
    const cx     = rect.width  / 2;
    const cy     = rect.height / 2;
    const rotateX = ((y - cy) / cy) * -6;
    const rotateY = ((x - cx) / cx) *  6;
    card.style.transform = `translateY(-8px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.01)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
    card.style.transition = 'transform 0.5s cubic-bezier(0.16,1,0.3,1)';
    setTimeout(() => card.style.transition = '', 500);
  });
});

/* ══════════════════════════════
   CONTACT FORM
══════════════════════════════ */
function handleSubmit(e) {
  e.preventDefault();
  
  const name = document.getElementById('contact-name').value.trim();
  const phone = document.getElementById('contact-phone').value.trim();
  const email = document.getElementById('contact-email').value.trim();
  const msg = document.getElementById('contact-msg').value.trim();

  if (!name || !phone || !email) {
    alert('Please fill out all the details carefully (Name, Phone, and Email).');
    return;
  }

  const btn = e.target.querySelector('.submit-btn');
  const originalText = btn.textContent;
  btn.textContent = 'Sending...';
  btn.style.background = 'linear-gradient(135deg, #5dde7a, #3db85e)';
  btn.style.color = '#141f17';
  btn.style.transform = 'scale(1.03)';

  // Send data to Google Forms silently
  const formUrl = 'https://docs.google.com/forms/d/e/1FAIpQLSfjX7iusbX9s7lmcYjrEbKVrNYVrW0LQsZE6rWm2e9jHcSBmQ/formResponse';
  const formData = new FormData();
  formData.append('entry.1723697301', name);
  formData.append('entry.512566268', phone);
  formData.append('entry.491741544', email);
  formData.append('entry.684053222', msg);

  fetch(formUrl, {
    method: 'POST',
    mode: 'no-cors',
    body: formData
  }).then(() => {
    btn.textContent = 'Message Sent ✓';
    setTimeout(() => {
      btn.textContent = originalText;
      btn.style.background = '';
      btn.style.color = '';
      btn.style.transform = '';
      e.target.reset();
    }, 3000);
  }).catch((error) => {
    console.error('Error submitting form:', error);
    btn.textContent = 'Error Try Again';
    btn.style.background = '#e74c3c';
    setTimeout(() => {
      btn.textContent = originalText;
      btn.style.background = '';
      btn.style.color = '';
      btn.style.transform = '';
    }, 3000);
  });
}

/* ══════════════════════════════
   SMOOTH SCROLL
══════════════════════════════ */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    e.preventDefault();
    const target = document.querySelector(a.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth' });
  });
});
