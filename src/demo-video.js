// Select a recording before playback; rotating a phone must not restart it.
const phoneScreen = window.matchMedia("(max-width: 740px)");
for (const video of document.querySelectorAll("video[data-phone-src]")) {
  const desktop = { src: video.getAttribute("src"), poster: video.poster };
  const selectRecording = () => {
    if (!video.paused || video.played.length > 0) return;
    const phone = phoneScreen.matches;
    const src = phone ? video.dataset.phoneSrc : desktop.src;
    if (video.getAttribute("src") === src) return;
    video.poster = phone ? video.dataset.phonePoster : desktop.poster;
    video.src = src;
  };
  selectRecording();
  phoneScreen.addEventListener("change", selectRecording);
}
