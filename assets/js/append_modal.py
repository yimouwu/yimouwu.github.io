with open('/Users/yimouwu/Desktop/yimou/yimouwu.github.io/assets/js/main.js', 'a') as f:
    f.write("""

/* VIDEO MODAL */
function openVideoModal(src) {
  var modal = document.getElementById('video-modal');
  var video = document.getElementById('modal-video');
  var source = document.getElementById('modal-video-src');
  source.src = src;
  video.load();
  video.play();
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeVideoModal() {
  var modal = document.getElementById('video-modal');
  var video = document.getElementById('modal-video');
  video.pause();
  video.currentTime = 0;
  modal.style.display = 'none';
  document.body.style.overflow = '';
}

document.addEventListener('DOMContentLoaded', function() {
  var modal = document.getElementById('video-modal');
  if (modal) {
    modal.addEventListener('click', function(e) {
      if (e.target === this) closeVideoModal();
    });
  }
});

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeVideoModal();
});
""")
print('done')