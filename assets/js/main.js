// Longfu88 Malaysia — minimal vanilla JS (mobile nav). Kept tiny for Core Web Vitals.
(function () {
  'use strict';
  var toggle = document.getElementById('menu-toggle');
  var nav = document.getElementById('mobile-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('hidden') === false;
      toggle.setAttribute('aria-expanded', String(open));
    });
  }
})();
