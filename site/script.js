// Block scrolling since each page is exactly 100vh.
document.addEventListener('wheel', e => e.preventDefault(), { passive: false });
document.addEventListener('touchmove', e => e.preventDefault(), { passive: false });
document.addEventListener('keydown', e => {
  if (['ArrowDown', 'ArrowUp', 'PageDown', 'PageUp', 'Space'].includes(e.code)) {
    e.preventDefault();
  }
});

// Align nav-overlay to the actual rendered area of the image (object-fit: contain).
function alignOverlay() {
  const img = document.querySelector('.page-img');
  const overlay = document.querySelector('.nav-overlay');
  if (!img || !overlay) return;

  const cw = img.clientWidth;
  const ch = img.clientHeight;
  const nw = img.naturalWidth;
  const nh = img.naturalHeight;
  if (!nw || !nh) return;

  const imgRatio = nw / nh;
  const containerRatio = cw / ch;

  let renderW, renderH, offsetX, offsetY;
  if (containerRatio > imgRatio) {
    // Letterboxed on sides
    renderH = ch;
    renderW = ch * imgRatio;
    offsetX = (cw - renderW) / 2;
    offsetY = 0;
  } else {
    // Letterboxed on top/bottom
    renderW = cw;
    renderH = cw / imgRatio;
    offsetX = 0;
    offsetY = (ch - renderH) / 2;
  }

  overlay.style.position = 'absolute';
  overlay.style.left = offsetX + 'px';
  overlay.style.top = offsetY + 'px';
  overlay.style.width = renderW + 'px';
  overlay.style.height = renderH + 'px';
}

const img = document.querySelector('.page-img');
if (img) {
  if (img.complete) alignOverlay();
  img.addEventListener('load', alignOverlay);
  window.addEventListener('resize', alignOverlay);
}
