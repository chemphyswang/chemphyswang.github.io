---
layout: page
permalink: /hobbies/index.html
title: Beyond Research
---

## 2026/10/18<br>Juyongguan Great Wall
{: .lang-en}

## 2026/10/18<br>居庸关长城
{: .lang-zh}

On October 18, 2026, our group joined the hike up the Juyongguan Great Wall organized by Prof. Haizheng Zhong.
{: .lang-en}

2026年10月18日，课题组参加了由钟海政教授组织的居庸关长城攀登活动。
{: .lang-zh}

<div class="album">
  <div class="album-stack" tabindex="0" role="button" aria-expanded="false" aria-controls="album-grid-juyongguan">
    <span class="stack-layer stack-l3"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/03.jpg" alt="" loading="lazy"></span>
    <span class="stack-layer stack-l2"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/02.jpg" alt="" loading="lazy"></span>
    <span class="stack-cover"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/01.jpg" alt="Group outing at Juyongguan Great Wall, October 2026"></span>
    <span class="album-badge"><span class="badge-open"><span class="lang-en">10 photos · Click to browse</span><span class="lang-zh">共 10 张 · 点击浏览</span></span><span class="badge-close"><span class="lang-en">Click to collapse</span><span class="lang-zh">点击收起</span></span></span>
  </div>
  <div class="album-grid" id="album-grid-juyongguan">
    <div class="album-row">
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/01.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/01.jpg" alt="Juyongguan Great Wall, photo 1" loading="lazy" decoding="async"></a></div>
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/02.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/02.jpg" alt="Juyongguan Great Wall, photo 2" loading="lazy" decoding="async"></a></div>
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/03.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/03.jpg" alt="Juyongguan Great Wall, photo 3" loading="lazy" decoding="async"></a></div>
    </div>
    <div class="album-row">
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/04.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/04.jpg" alt="Juyongguan Great Wall, photo 4" loading="lazy" decoding="async"></a></div>
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/05.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/05.jpg" alt="Juyongguan Great Wall, photo 5" loading="lazy" decoding="async"></a></div>
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/06.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/06.jpg" alt="Juyongguan Great Wall, photo 6" loading="lazy" decoding="async"></a></div>
    </div>
    <div class="album-row">
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/07.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/07.jpg" alt="Juyongguan Great Wall, photo 7" loading="lazy" decoding="async"></a></div>
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/08.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/08.jpg" alt="Juyongguan Great Wall, photo 8" loading="lazy" decoding="async"></a></div>
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/09.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/09.jpg" alt="Juyongguan Great Wall, photo 9" loading="lazy" decoding="async"></a></div>
    </div>
    <div class="album-row">
      <div class="album-photo"><a href="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/full/10.jpg"><img src="{{ site.baseurl }}/images/hobbies/juyongguan-2026-10/10.jpg" alt="Juyongguan Great Wall, photo 10" loading="lazy" decoding="async"></a></div>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.album-stack').forEach(function (stack) {
    var grid = document.getElementById(stack.getAttribute('aria-controls'));
    if (!grid) return;
    var toggle = function () {
      var open = stack.getAttribute('aria-expanded') === 'true';
      stack.setAttribute('aria-expanded', String(!open));
      stack.classList.toggle('open', !open);
      grid.classList.toggle('open', !open);
    };
    stack.addEventListener('click', toggle);
    stack.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
    });
  });

  // While the lightbox is open, tag <body> so CSS can pause the sticky
  // header's backdrop blur — the fullscreen fade otherwise stutters.
  var mo = new MutationObserver(function () {
    document.body.classList.toggle('lightbox-open', !!document.querySelector('.mfp-bg'));
  });
  mo.observe(document.body, { childList: true });
});
</script>

{% comment %}
<div class="hobbies-pinterest-container">

<div class="hobby-section" markdown="1">

## Personal Photos

<div class="third">
  <div class="image-container">
    <a href="/images/hobbies/dsm2.jpg" class="image-popup">
      <img src="/images/hobbies/dsm2.jpg" alt="Siming's personal photo">
    </a>
  </div>
  <div class="image-container">
    <a href="/images/hobbies/dsm3.jpg" class="image-popup">
      <img src="/images/hobbies/dsm3.jpg" alt="Siming at the Forbidden City in Beijing">
    </a>
    <div class="image-caption">
      <div class="caption-title">Forbidden City, Beijing</div>
    </div>
  </div>
  <div class="image-container">
    <a href="/images/hobbies/dsm4.jpg" class="image-popup">
      <img src="/images/hobbies/dsm4.jpg" alt="Siming's personal photo">
    </a>
  </div>
</div>

</div>

<div class="hobby-section cooking-section" markdown="1">

## Possibly the World's Best Amateur Chef

<div class="cooking-text-card">
Every meal is an opportunity to create, taste, and share.
</div>

<div class="cooking-gallery">
  <div class="cooking-featured">
    <a href="/images/hobbies/Dish1.jpg" class="image-popup">
      <img src="/images/hobbies/Dish1.jpg" alt="Siming's signature dish">
    </a>
  </div>
  <div class="cooking-grid">
    <div class="cooking-item">
      <a href="/images/hobbies/Dish2.jpg" class="image-popup">
        <img src="/images/hobbies/Dish2.jpg" alt="Homemade meal by Siming">
      </a>
    </div>
    <div class="cooking-item">
      <a href="/images/hobbies/Dish3.jpg" class="image-popup">
        <img src="/images/hobbies/Dish3.jpg" alt="Culinary creation by Siming">
      </a>
    </div>
  </div>
</div>

</div>

<div class="hobby-section" markdown="1">

## Passion for the Blues: My Guitar Journey

Beyond academia and AI innovation, you'll find me lost in the soulful rhythms of the blues. For me, the guitar isn't just an instrument — it's a bridge between logic and emotion, a medium to channel life's raw, unfiltered energy. I've spent countless evenings with fingers dancing across the fretboard, honing the perfect bend or riff until my mom practically dragged me out for dinner. To me, blues is more than music; it's a storytelling language where every note carries joy, struggle, and resilience.

My musical heroes are legends who pioneered the genre: <span class="artist-name">B.B. King</span>'s soulful improvisation, <span class="artist-name">Eric Clapton</span>'s blues-rock mastery, and <span class="artist-name">John Mayer</span>'s modern reinvention. Their influence resonates in my playing—whether I'm jamming the blues' foundational 12-bar shuffle or experimenting with ambient textures.

<div class="hobby-quote">
"Life isn't just about hitting the right notes in code; it's about finding harmony between mind and soul."
</div>

</div>

<div class="hobby-section guitar-showcase" markdown="1">

<p class="guitar-tagline">My guitar, my life. My guitar, my wife :)</p>

<div class="guitar-image-container">
  <a href="/images/hobbies/guitar.jpg" class="image-popup">
    <img src="/images/hobbies/guitar.jpg" alt="Martin OM28 acoustic guitar and Fender American Professional II">
  </a>
</div>

</div>

</div><!-- End hobbies-pinterest-container -->
{% endcomment %}
