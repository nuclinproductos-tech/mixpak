document.addEventListener('DOMContentLoaded', () => {
  /* ── 1. Scroll Behavior ── */
  const header = document.getElementById('site-header');
  let ticking = false;

  function handleScroll() {
    if (window.scrollY > 80) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(handleScroll);
      ticking = true;
    }
  });

  // Init scroll state on load
  handleScroll();

  /* ── 2. Active State Logic ── */
  const path = window.location.pathname;
  
  const activateLink = (selector) => {
    document.querySelectorAll(selector).forEach(link => {
      // For desktop
      const parentLi = link.closest('.nav-item');
      if (parentLi) parentLi.classList.add('active');
      
      // For mobile / dropdown items
      link.classList.add('active');

      // If it's a dropdown item, also activate the parent trigger
      const dropdownLi = link.closest('.nav-item--dropdown');
      if (dropdownLi) dropdownLi.classList.add('active');
    });
  };

  // Clear exact active links first (just in case)
  document.querySelectorAll('.nav-item, .nav-mobile-link, .nav-dropdown-item, .nav-mobile-dropdown-item').forEach(el => {
    el.classList.remove('active');
  });

  if (path === '/' || path === '/index.html') {
    activateLink('a[href="/"]');
  } else if (path.includes('/desarrollo-de-producto')) {
    activateLink('a[href="/desarrollo-de-producto"]');
  } else if (path.includes('/fabricacion')) {
    activateLink('a[href="/fabricacion"]');
  } else if (path.includes('/copacking')) {
    activateLink('a[href="/copacking"]');
  } else if (path.includes('/sectores/')) {
    // Find the specific sector link to activate
    activateLink(`a[href="${path}"]`);
  } else if (path.includes('/calidad')) {
    activateLink('a[href="/calidad"]');
  } else if (path.includes('/empresa')) {
    activateLink('a[href="/empresa"]');
  }
  // Note: CTA 'contacto' is not marked active.

  /* ── 3. Desktop Dropdown Logic ── */
  const dropdownItem = document.querySelector('.nav-item--dropdown');
  const dropdownTrigger = document.querySelector('.nav-dropdown-trigger');
  const dropdownMenu = document.querySelector('.nav-dropdown');
  let hoverTimeout;

  if (dropdownItem && dropdownTrigger && dropdownMenu) {
    const openDropdown = () => {
      dropdownItem.classList.add('open');
      dropdownTrigger.setAttribute('aria-expanded', 'true');
    };

    const closeDropdown = () => {
      dropdownItem.classList.remove('open');
      dropdownTrigger.setAttribute('aria-expanded', 'false');
    };

    // Hover
    dropdownItem.addEventListener('mouseenter', () => {
      clearTimeout(hoverTimeout);
      openDropdown();
    });

    dropdownItem.addEventListener('mouseleave', () => {
      hoverTimeout = setTimeout(closeDropdown, 150);
    });

    // Click on trigger (for touch or keyboard)
    dropdownTrigger.addEventListener('click', (e) => {
      e.preventDefault();
      if (dropdownItem.classList.contains('open')) {
        closeDropdown();
      } else {
        openDropdown();
      }
    });

    // Keyboard Accessibility
    dropdownTrigger.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        if (dropdownItem.classList.contains('open')) {
          closeDropdown();
        } else {
          openDropdown();
        }
      } else if (e.key === 'Escape') {
        closeDropdown();
        dropdownTrigger.focus();
      }
    });

    dropdownMenu.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeDropdown();
        dropdownTrigger.focus();
      }
    });

    // Close when tabbing out of the last item
    const dropdownItems = dropdownMenu.querySelectorAll('.nav-dropdown-item');
    if (dropdownItems.length > 0) {
      const lastItem = dropdownItems[dropdownItems.length - 1];
      lastItem.addEventListener('keydown', (e) => {
        if (e.key === 'Tab' && !e.shiftKey) {
          closeDropdown();
        }
      });
    }

    // Click outside to close
    document.addEventListener('click', (e) => {
      if (!dropdownItem.contains(e.target)) {
        closeDropdown();
      }
    });
  }

  /* ── 4. Mobile Menu Logic ── */
  const hamburger = document.querySelector('.nav-hamburger');
  const navMobile = document.getElementById('nav-mobile');

  if (hamburger && navMobile) {
    const toggleMobileMenu = () => {
      const isOpen = hamburger.classList.contains('open');
      if (isOpen) {
        hamburger.classList.remove('open');
        navMobile.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      } else {
        hamburger.classList.add('open');
        navMobile.classList.add('open');
        hamburger.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
      }
    };

    hamburger.addEventListener('click', toggleMobileMenu);

    // Optional: Close mobile menu when a link is clicked (useful if using anchors)
    navMobile.querySelectorAll('.nav-mobile-link, .nav-mobile-dropdown-item, .nav-mobile-cta').forEach(link => {
      if (link.tagName === 'A') {
        link.addEventListener('click', () => {
          if (hamburger.classList.contains('open')) {
            toggleMobileMenu();
          }
        });
      }
    });
  }
});
