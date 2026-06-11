// Longfu88 Malaysia — minimal vanilla JS. Kept tiny for Core Web Vitals.
(function () {
  'use strict';

  /* ---- Mobile nav ---- */
  var toggle = document.getElementById('menu-toggle');
  var nav = document.getElementById('mobile-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('hidden') === false;
      toggle.setAttribute('aria-expanded', String(open));
    });
  }

  /* ---- Hero banner slider ---- */
  var slider = document.querySelector('.hero-slider');
  if (!slider) return;
  var slides = Array.prototype.slice.call(slider.querySelectorAll('.hero-slide'));
  var dots = Array.prototype.slice.call(slider.querySelectorAll('.hero-dot'));
  if (slides.length < 2) return;

  var DELAY = 5000;
  var index = 0;
  var timer = null;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function show(i) {
    index = (i + slides.length) % slides.length;
    slides.forEach(function (s, n) { s.classList.toggle('is-active', n === index); });
    dots.forEach(function (d, n) {
      var on = n === index;
      d.classList.toggle('is-active', on);
      d.setAttribute('aria-selected', on ? 'true' : 'false');
    });
  }
  function next() { show(index + 1); }
  function prev() { show(index - 1); }
  function stop() { if (timer) { clearInterval(timer); timer = null; } }
  function start() { if (reduce) return; stop(); timer = setInterval(next, DELAY); }

  var nextBtn = slider.querySelector('.hero-slider__arrow--next');
  var prevBtn = slider.querySelector('.hero-slider__arrow--prev');
  if (nextBtn) nextBtn.addEventListener('click', function () { next(); start(); });
  if (prevBtn) prevBtn.addEventListener('click', function () { prev(); start(); });
  dots.forEach(function (d, n) { d.addEventListener('click', function () { show(n); start(); }); });

  slider.addEventListener('mouseenter', stop);
  slider.addEventListener('mouseleave', start);
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) { stop(); } else { start(); }
  });

  show(0);
  start();
})();
