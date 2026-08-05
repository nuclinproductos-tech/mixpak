(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function closeFaqItem(item) {
    const btn = item.querySelector('.faq-q');
    const answer = item.querySelector('.faq-a');
    item.classList.remove('active');
    if (btn) btn.setAttribute('aria-expanded', 'false');
    if (answer) answer.style.maxHeight = null;
  }

  function openFaqItem(item) {
    const btn = item.querySelector('.faq-q');
    const answer = item.querySelector('.faq-a');
    item.classList.add('active');
    if (btn) btn.setAttribute('aria-expanded', 'true');
    if (answer) answer.style.maxHeight = answer.scrollHeight + 'px';
  }

  document.addEventListener('click', function (event) {
    const faqButton = event.target.closest('.faq-q');
    if (!faqButton) return;

    const item = faqButton.closest('.faq-item');
    if (!item) return;

    event.preventDefault();
    event.stopImmediatePropagation();

    const isOpen = item.classList.contains('active');
    item.parentElement.querySelectorAll('.faq-item.active').forEach(function (openItem) {
      if (openItem !== item) closeFaqItem(openItem);
    });

    if (isOpen) closeFaqItem(item);
    else openFaqItem(item);
  }, true);

  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape') return;

    document.querySelectorAll('.nav-trigger[aria-expanded="true"]').forEach(function (trigger) {
      trigger.setAttribute('aria-expanded', 'false');
      trigger.classList.remove('nav-active');
      const dropdown = document.getElementById(trigger.getAttribute('data-dd'));
      if (dropdown) dropdown.classList.remove('open');
    });

    const drawer = document.getElementById('mobile-drawer') || document.getElementById('mob');
    const hamburger = document.getElementById('hamburger') || document.getElementById('hbg');
    if (drawer && drawer.classList.contains('open')) {
      drawer.classList.remove('open');
      if (hamburger) {
        hamburger.classList.remove('is-active');
        hamburger.setAttribute('aria-expanded', 'false');
      }
      document.body.style.overflow = '';
    }
  });

  document.addEventListener('submit', function (event) {
    const form = event.target.closest('form');
    if (!form) return;
    const submit = form.querySelector('.f-submit, button[type="submit"]');
    window.setTimeout(function () {
      if (submit && submit.disabled) submit.setAttribute('aria-busy', 'true');
    }, 0);
  });

  window.addEventListener('pageshow', function () {
    document.querySelectorAll('.f-submit[aria-busy="true"]').forEach(function (button) {
      if (!button.disabled) button.removeAttribute('aria-busy');
    });
  });

  if (!reduceMotion) return;

  document.querySelectorAll('video[autoplay]').forEach(function (video) {
    video.pause();
    video.removeAttribute('autoplay');
  });
})();
