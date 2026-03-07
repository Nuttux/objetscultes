// Navigation is via standard <a href> links between pages.
// Block scrolling since each page is exactly 100vh.
document.addEventListener('wheel', e => e.preventDefault(), { passive: false });
document.addEventListener('touchmove', e => e.preventDefault(), { passive: false });
document.addEventListener('keydown', e => {
  if (['ArrowDown', 'ArrowUp', 'PageDown', 'PageUp', 'Space'].includes(e.code)) {
    e.preventDefault();
  }
});
