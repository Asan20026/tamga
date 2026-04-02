function toggleMenu() {
  const nav = document.getElementById('site-nav');
  if (nav) nav.classList.toggle('open');
}

document.addEventListener('click', (e) => {
  const nav = document.getElementById('site-nav');
  const burger = document.querySelector('.burger');
  if (!nav || !burger) return;
  if (!nav.contains(e.target) && !burger.contains(e.target)) {
    nav.classList.remove('open');
  }
});

document.querySelectorAll('[data-carousel]').forEach((carousel) => {
  const slides = Array.from(carousel.querySelectorAll('.yurt-card'));
  const prev = carousel.querySelector('.prev');
  const next = carousel.querySelector('.next');
  const dotsWrap = carousel.querySelector('.carousel-dots');
  let index = 0;
  let timer;

  const dots = slides.map((_, i) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.addEventListener('click', () => show(i));
    dotsWrap.appendChild(btn);
    return btn;
  });

  function show(i) {
    index = (i + slides.length) % slides.length;
    slides.forEach((slide, sIndex) => slide.classList.toggle('active', sIndex === index));
    dots.forEach((dot, dIndex) => dot.classList.toggle('active', dIndex === index));
  }

  function autoplay() {
    clearInterval(timer);
    timer = setInterval(() => show(index + 1), 5000);
  }

  prev?.addEventListener('click', () => { show(index - 1); autoplay(); });
  next?.addEventListener('click', () => { show(index + 1); autoplay(); });

  let startX = 0;
  carousel.addEventListener('touchstart', (e) => startX = e.changedTouches[0].clientX, { passive: true });
  carousel.addEventListener('touchend', (e) => {
    const endX = e.changedTouches[0].clientX;
    if (Math.abs(endX - startX) < 40) return;
    if (endX < startX) show(index + 1);
    else show(index - 1);
    autoplay();
  }, { passive: true });

  show(0);
  autoplay();
});
