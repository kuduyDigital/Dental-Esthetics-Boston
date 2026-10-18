// Smooth scrolling: one Lenis instance, its own rAF loop (autoRaf).
// respectReducedMotion is on by default, so reduced-motion users get native scrolling.
// Anchor offset comes from CSS scroll-padding-top, which Lenis already honours.
const lenis = window.Lenis
  ? new Lenis({ autoRaf: true, lerp: 0.1, anchors: true, stopInertiaOnNavigate: true })
  : null;

const motionOK = matchMedia('(prefers-reduced-motion: no-preference)').matches;
const header = document.querySelector('.site-header');
const parallax = motionOK ? [...document.querySelectorAll('[data-parallax]')] : [];

// One scroll handler, batched to a frame: header state + parallax
let lastY = scrollY;
let queued = false;
const frame = () => {
  queued = false;
  const y = scrollY;
  header.toggleAttribute('data-scrolled', y > 24);
  if (menu.hidden) header.toggleAttribute('data-hidden', y > lastY && y > 320);
  lastY = y;

  const vh = innerHeight;
  for (const el of parallax) {
    const r = el.getBoundingClientRect();
    if (r.bottom < -100 || r.top > vh + 100) continue;
    // clamp to the 6% overscan the CSS scale(1.12) leaves on each side
    const max = r.height * 0.05;
    const shift = Math.max(-max, Math.min(max, (r.top + r.height / 2 - vh / 2) * -parseFloat(el.dataset.parallax)));
    el.firstElementChild.style.transform = `translate3d(0, ${shift.toFixed(1)}px, 0)`;
  }
};
const onScroll = () => { if (!queued) { queued = true; requestAnimationFrame(frame); } };
addEventListener('scroll', onScroll, { passive: true });
addEventListener('resize', onScroll);

// Mobile menu (Lenis paused while open)
const toggle = document.querySelector('[data-menu-toggle]');
const menu = document.getElementById('mobile-menu');
const setMenu = (open) => {
  menu.hidden = !open;
  toggle.setAttribute('aria-expanded', open);
  toggle.querySelector('[data-menu-label]').textContent = open ? 'Close' : 'Menu';
  header.removeAttribute('data-hidden');
  document.documentElement.style.overflow = open ? 'hidden' : '';
  if (lenis) open ? lenis.stop() : lenis.start();
};
toggle.addEventListener('click', () => setMenu(menu.hidden));
// capture phase: close (and restart Lenis) before Lenis handles the anchor
menu.addEventListener('click', (e) => e.target.closest('a') && setMenu(false), true);
addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && !menu.hidden) { setMenu(false); toggle.focus(); }
});
matchMedia('(min-width: 1024px)').addEventListener('change', (e) => e.matches && setMenu(false));

frame();

// Reveals: fade-up, line-by-line headlines, image mask wipes (CSS is inert under reduced motion)
const items = document.querySelectorAll('[data-reveal]');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    for (const en of entries) if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.12 });
  items.forEach((el) => io.observe(el));
} else {
  items.forEach((el) => el.classList.add('is-in'));
}

// Testimonial slider: buttons drive the native scroll-snap track; state follows the scroll position
for (const slider of document.querySelectorAll('[data-slider]')) {
  const track = slider.querySelector('[data-slider-track]');
  const n = track.children.length;
  const prev = slider.querySelector('[data-slider-prev]');
  const next = slider.querySelector('[data-slider-next]');
  const index = slider.querySelector('[data-slider-index]');
  const bar = slider.querySelector('[data-slider-bar]');
  const current = () => Math.round(track.scrollLeft / track.clientWidth);
  const go = (i) => track.children[Math.max(0, Math.min(n - 1, i))].scrollIntoView({ block: 'nearest', inline: 'start' });
  const sync = () => {
    const i = current();
    index.textContent = String(i + 1).padStart(2, '0');
    bar.style.width = `${((i + 1) / n) * 100}%`;
    prev.disabled = i === 0;
    next.disabled = i === n - 1;
    [...track.children].forEach((s, k) => s.setAttribute('aria-hidden', k !== i));
  };
  prev.addEventListener('click', () => go(current() - 1));
  next.addEventListener('click', () => go(current() + 1));
  track.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') { e.preventDefault(); go(current() + 1); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); go(current() - 1); }
  });
  track.addEventListener('scroll', () => requestAnimationFrame(sync), { passive: true });
  addEventListener('resize', sync);
  sync();
}
