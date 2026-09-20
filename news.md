---
layout: page
permalink: /news/index.html
title: News
---

## News

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
    <p>Aoyuan's paper, <a href="https://doi.org/10.1002/anie.8043102"><strong>"Nature-Inspired Organic–Inorganic Hybridization Enables High-Temperature and Multicolor Organic Phosphorescence"</strong></a>, is out in <em>Angew. Chem. Int. Ed.</em></p>
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
(function() {
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-in');
          observer.unobserve(entry);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -60px 0px' });
    document.querySelectorAll('.news-card').forEach(function(card) {
      observer.observe(card);
    });
  } else {
    document.querySelectorAll('.news-card').forEach(function(card) {
      card.classList.add('animate-in');
    });
  }
})();
</script>
