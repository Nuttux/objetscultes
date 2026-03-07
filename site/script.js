// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Parallax-like subtle movement for background figurines on mousemove
const bgFigs = document.querySelectorAll('.bg-fig');
const exhibition = document.querySelector('.section-exhibition');

if (exhibition) {
  exhibition.addEventListener('mousemove', e => {
    const rect = exhibition.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;

    bgFigs.forEach((fig, i) => {
      const depth = 0.5 + (i % 3) * 0.3;
      const moveX = x * 15 * depth;
      const moveY = y * 10 * depth;
      fig.style.transform = `translate(${moveX}px, ${moveY}px)`;
    });
  });
}

// Fade-in sections on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.section').forEach(section => {
  observer.observe(section);
});
