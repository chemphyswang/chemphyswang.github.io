---
layout: page
permalink: /news/index.html
title: News
---

## News and Updates
{: .lang-en}

## 新闻动态
{: .lang-zh}

<div class="news-grid">
  <div class="news-card news-card--milestone">
    <div class="news-meta">
      <span class="news-date"><span class="lang-en">September 2026</span><span class="lang-zh">2026年9月</span></span>
      <span class="news-tag news-tag--milestone"><span class="lang-en">Milestone</span><span class="lang-zh">里程碑</span></span>
    </div>
    <p><span class="lang-en">We welcome Hua Jiang, who joins our group as a Master's student.</span><span class="lang-zh">欢迎蒋华同学加入课题组攻读硕士学位。</span></p>
  </div>

  <div class="news-card news-card--publication">
    <div class="news-meta">
      <span class="news-date"><span class="lang-en">July 2026</span><span class="lang-zh">2026年7月</span></span>
      <span class="news-tag news-tag--publication"><span class="lang-en">Publication</span><span class="lang-zh">论文</span></span>
    </div>
    <p><span class="lang-en">Our collaborative review, <a href="https://doi.org/10.1007/s11426-025-3385-5"><strong>"Organic Room-Temperature Phosphorescence Materials"</strong></a>, is out in <em>Sci. China Chem.</em></span><span class="lang-zh">我们的合作综述<a href="https://doi.org/10.1007/s11426-025-3385-5"><strong>"Organic Room-Temperature Phosphorescence Materials"</strong></a>在 <em>Sci. China Chem.</em> 正式发表。</span></p>
  </div>

  <div class="news-card news-card--publication">
    <div class="news-meta">
      <span class="news-date"><span class="lang-en">June 2026</span><span class="lang-zh">2026年6月</span></span>
      <span class="news-tag news-tag--publication"><span class="lang-en">Publication</span><span class="lang-zh">论文</span></span>
    </div>
    <p><span class="lang-en">Hongping's paper, <a href="https://doi.org/10.1093/nsr/nwag394"><strong>"Molecular Orbital Node Engineering in Pyrene: Linking Chemical Reactivity with Room-Temperature Phosphorescence"</strong></a>, is out in <em>Natl. Sci. Rev.</em></span><span class="lang-zh">恭喜洪平，论文<a href="https://doi.org/10.1093/nsr/nwag394"><strong>"Molecular Orbital Node Engineering in Pyrene: Linking Chemical Reactivity with Room-Temperature Phosphorescence"</strong></a>在 <em>Natl. Sci. Rev.</em> 正式发表。</span></p>
  </div>

  <div class="news-card news-card--publication">
    <div class="news-meta">
      <span class="news-date"><span class="lang-en">May 2026</span><span class="lang-zh">2026年5月</span></span>
      <span class="news-tag news-tag--publication"><span class="lang-en">Publication</span><span class="lang-zh">论文</span></span>
    </div>
    <p><span class="lang-en">Aoyuan's paper, <a href="https://doi.org/10.1002/anie.8043102"><strong>"Nature-Inspired Organic–Inorganic Hybridization Enables High-Temperature and Multicolor Organic Phosphorescence"</strong></a>, is out in <em>Angew. Chem. Int. Ed.</em> (Selected as an <a href="https://onlinelibrary.wiley.com/doi/10.1002/anie.2026-m2506061400">inside back cover</a>).</span><span class="lang-zh">恭喜奥远，论文<a href="https://doi.org/10.1002/anie.8043102"><strong>"Nature-Inspired Organic–Inorganic Hybridization Enables High-Temperature and Multicolor Organic Phosphorescence"</strong></a>在 <em>Angew. Chem. Int. Ed.</em> 正式发表（被选为 <a href="https://onlinelibrary.wiley.com/doi/10.1002/anie.2026-m2506061400">inside back cover</a>）。</span></p>
  </div>

  <div class="news-card news-card--publication">
    <div class="news-meta">
      <span class="news-date"><span class="lang-en">April 2026</span><span class="lang-zh">2026年4月</span></span>
      <span class="news-tag news-tag--publication"><span class="lang-en">Publication</span><span class="lang-zh">论文</span></span>
    </div>
    <p><span class="lang-en">Hao's paper, <a href="https://doi.org/10.1021/acsnano.6c00162"><strong>"Ultra-Linear Afterglow Oxygen Sensing and Visualization in Morphology-Engineered Phosphorescent Microporous Copolymers"</strong></a>, is out in <em>ACS Nano</em>.</span><span class="lang-zh">恭喜苏昊，论文<a href="https://doi.org/10.1021/acsnano.6c00162"><strong>"Ultra-Linear Afterglow Oxygen Sensing and Visualization in Morphology-Engineered Phosphorescent Microporous Copolymers"</strong></a>在 <em>ACS Nano</em> 正式发表。</span></p>
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
