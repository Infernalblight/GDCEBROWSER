// window.js
window.onload = function() {
    const ads = document.querySelectorAll('.ad, .advertisement, [id*="ad"], [class*="ad"]');
    ads.forEach(ad => ad.style.display = 'none');
    console.log("Ad blocker activated.");
};