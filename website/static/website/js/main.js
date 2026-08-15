document.addEventListener('DOMContentLoaded', function () {

  // Mobile menu toggle
  const menuToggle = document.getElementById('menuToggle');
  const navLinks = document.getElementById('navLinks');

  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', function () {
      navLinks.classList.toggle('active');
    });

    // Close menu when a link is clicked (mobile)
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('active');
      });
    });
  }

  // Close mobile menu if clicking outside it
  document.addEventListener('click', function (e) {
    if (navLinks && navLinks.classList.contains('active')) {
      if (!navLinks.contains(e.target) && !menuToggle.contains(e.target)) {
        navLinks.classList.remove('active');
      }
    }
  });

});

document.addEventListener('DOMContentLoaded', function () {

  // ===== Scroll-reveal animations =====
  const revealTargets = document.querySelectorAll(
    '.core-service-card, .compact-card, .process-item, .pricing-card, ' +
    '.testimonial-card, .portfolio-card, .blog-card, .mv-card, .offer-card'
  );

  revealTargets.forEach(function (el) {
    el.classList.add('reveal-init');
  });

  const revealObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  revealTargets.forEach(function (el) {
    revealObserver.observe(el);
  });

  // ===== Animated stat counters =====
  const statValues = document.querySelectorAll('.stat-value, .mini-value');

  function animateCount(el) {
    const raw = el.textContent.trim();
    const match = raw.match(/^(\d+)(.*)$/); // splits "250+" into 250 and "+"
    if (!match) return;

    const target = parseInt(match[1], 10);
    const suffix = match[2];
    let current = 0;
    const duration = 1200;
    const stepTime = Math.max(Math.floor(duration / target), 15);

    const timer = setInterval(function () {
      current += Math.ceil(target / (duration / stepTime));
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      el.textContent = current + suffix;
    }, stepTime);
  }

  const countObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animateCount(entry.target);
        countObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  statValues.forEach(function (el) {
    countObserver.observe(el);
  });

  // ===== Navbar shadow on scroll =====
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 10) {
        navbar.classList.add('navbar-scrolled');
      } else {
        navbar.classList.remove('navbar-scrolled');
      }
    });
  }

});