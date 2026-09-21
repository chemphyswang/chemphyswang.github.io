---
layout: page
permalink: /news/index.html
title: News
---

## News and Updates

<div class="news-grid">
  <div class="news-card news-card--milestone">
    <div class="news-meta">
      <span class="news-date">September 2026</span>
      <span class="news-tag news-tag--milestone">Milestone</span>
    </div>
    <p>We welcome Hua Jiang, who joins our group as a Master's student.</p>
  </div>

  <div class="news-card news-card--publication">
    <div class="news-meta">
      <span class="news-date">July 2026</span>
      <span class="news-tag news-tag--publication">Publication</span>
    </div>
    <p>Our collaborative review, <a href="https://doi.org/10.1007/s11426-025-3385-5"><strong>"Organic Room-Temperature Phosphorescence Materials"</strong></a>, is out in <em>Sci. China Chem.</em></p>
  </div>

  <div class="news-card news-card--publication">
    <div class="news-meta">
      <span class="news-date">June 2026</span>
      <span class="news-tag news-tag--publication">Publication</span>
    </div>
    <p>Hongping's paper, <a href="https://doi.org/10.1093/nsr/nwag394"><strong>"Molecular Orbital Node Engineering in Pyrene: Linking Chemical Reactivity with Room-Temperature Phosphorescence"</strong></a>, is out in <em>Natl. Sci. Rev.</em></p>
  </div>

  <div class="news-card news-card--publication">
    <div class="news-meta">
      <span class="news-date">May 2026</span>
      <span class="news-tag news-tag--publication">Publication</span>
    </div>
    <p>Aoyuan's paper, <a href="https://doi.org/10.1002/anie.8043102"><strong>"Nature-Inspired Organic–Inorganic Hybridization Enables High-Temperature and Multicolor Organic Phosphorescence"</strong></a>, is out in <em>Angew. Chem. Int. Ed.</em> (Selected as an <a href="https://onlinelibrary.wiley.com/doi/10.1002/anie.2026-m2506061400">inside back cover</a>).</p>
  </div>

  <div class="news-card news-card--publication">
    <div class="news-meta">
      <span class="news-date">April 2026</span>
      <span class="news-tag news-tag--publication">Publication</span>
    </div>
    <p>Hao's paper, <a href="https://doi.org/10.1021/acsnano.6c00162"><strong>"Ultra-Linear Afterglow Oxygen Sensing and Visualization in Morphology-Engineered Phosphorescent Microporous Copolymers"</strong></a>, is out in <em>ACS Nano</em>.</p>
  </div>
</div>

<script>
// Entry animation for the cards visible in the initial viewport only.
// Cards below the fold are always fully visible (no scroll-gated reveal),
// so mobile visitors never mistake the page for having only a few items.
(function() {
  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.news-card').forEach(function(card) {
    if (prefersReduced) return;
    var rect = card.getBoundingClientRect();
    if (rect.top < window.innerHeight && rect.bottom > 0) {
      card.classList.add('animate-in');
    }
  });
})();
</script>
