---
layout: page
---

## About Tao

<img src="/images/avatar.jpg" class="floatpic">

**Tao Wang, PhD, Assoc. Prof.**.<br>

Tao Wang is currently an associate professor in the School of Materials Science & Engineering at the [Beijing Institute of Technology](https://www.bit.edu.cn/). He obtained his Ph.D. in 2019 from the [University of Science and Technology of China (USTC)](https://www.ustc.edu.cn/) under the supervision of Professors [Guoqing Zhang](https://www.hfnl.ustc.edu.cn/2022/0905/c36716a705572/page.htm) and Xingyuan Zhang, where he worked on luminescent polymers. Following this, he joined the Hefei National Laboratory of Physical Science at the Microscale at USTC as a postdoctoral fellow, continuing his work with Professor [Guoqing Zhang](https://www.hfnl.ustc.edu.cn/2022/0905/c36716a705572/page.htm) (2019–2020). In 2020, he was awarded the prestigious [Marie Skłodowska-Curie Research Fellowship](https://cordis.europa.eu/project/id/897098) and moved to the [University of St Andrews](https://www.st-andrews.ac.uk/) to work with Professor [Eli Zysman-Colman](https://www.zysman-colman.com/home). In 2022, he joined the [National University of Singapore](https://www.nus.edu.sg/) to collaborate with Professor [Xiaogang Liu](http://liuxg.science.nus.edu.sg/). In 2024, Tao joined the [Beijing Institute of Technology](https://www.bit.edu.cn/). His research focuses on organic luminescent materials for diverse applications, and he has authored more than 45 publications.<br>

## Research Interests

- Design of Room-Temperature Phosphorescence Materials
- Design of Thermally Activated Delayed Fluorescence Materials
- Exploration of Applications for Optoelectronic Materials
<br>

## Work Experience and Education

<div class="timeline">
  <div class="timeline-progress" id="timeline-progress"></div>

  <div class="timeline-item timeline-item--current">
    <div class="timeline-dot" style="background: #ffffff;">
      <img class="logo-lg" src="/images/logo/bit.svg" alt="Beijing Institute of Technology">
    </div>
    <div class="timeline-card">
      <div class="timeline-header">
        <div class="timeline-role">Associate Professor <span class="timeline-sep">|</span> <span class="timeline-company">Beijing Institute of Technology</span></div>
        <span class="timeline-time">Jul. 2024 - Present</span>
      </div>
      <div class="timeline-details">
        Beijing, China
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background: #ffffff;">
      <img src="/images/logo/nus.svg" alt="National University of Singapore">
    </div>
    <div class="timeline-card">
      <div class="timeline-header">
        <div class="timeline-role">Postdoctoral Research Fellow <span class="timeline-sep">|</span> <span class="timeline-company">National University of Singapore</span></div>
        <span class="timeline-time">Nov. 2022 - Jun. 2024</span>
      </div>
      <div class="timeline-details">
        Singapore · With Professor Xiaogang Liu
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background: #ffffff;">
      <img src="/images/logo/standrews.svg" alt="University of St Andrews">
    </div>
    <div class="timeline-card">
      <div class="timeline-header">
        <div class="timeline-role">Postdoctoral Research Fellow; Marie Skłodowska-Curie Fellow <span class="timeline-sep">|</span> <span class="timeline-company">University of St Andrews</span></div>
        <span class="timeline-time">Oct. 2020 - Nov. 2022</span>
      </div>
      <div class="timeline-details">
        St Andrews, United Kingdom · With Professor Eli Zysman-Colman
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background: #ffffff;">
      <img class="logo-lg" src="/images/logo/ustc.svg" alt="University of Science and Technology of China">
    </div>
    <div class="timeline-card">
      <div class="timeline-header">
        <div class="timeline-role">Postdoctoral Fellow <span class="timeline-sep">|</span> <span class="timeline-company">University of Science and Technology of China</span></div>
        <span class="timeline-time">Jul. 2019 - Oct. 2020</span>
      </div>
      <div class="timeline-details">
        Hefei, China · With Professor Guoqing Zhang
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background: #ffffff;">
      <img class="logo-lg" src="/images/logo/ustc.svg" alt="University of Science and Technology of China">
    </div>
    <div class="timeline-card">
      <div class="timeline-header">
        <div class="timeline-role">Ph.D. in Polymer Chemistry and Physics <span class="timeline-sep">|</span> <span class="timeline-company">University of Science and Technology of China</span></div>
        <span class="timeline-time">Sep. 2014 - Jun. 2019</span>
      </div>
      <div class="timeline-details">
        Hefei, Anhui, China · Supervisors: Prof. Guoqing Zhang and Prof. Xingyuan Zhang
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-dot" style="background: #ffffff;">
      <img class="logo-lg" src="/images/logo/anhui.svg" alt="Anhui University">
    </div>
    <div class="timeline-card">
      <div class="timeline-header">
        <div class="timeline-role">B.E. in Polymer Materials and Engineering <span class="timeline-sep">|</span> <span class="timeline-company">Anhui University</span></div>
        <span class="timeline-time">Sep. 2010 - Jul. 2014</span>
      </div>
      <div class="timeline-details">
        Hefei, Anhui, China
      </div>
    </div>
  </div>

</div>

## Honors and Awards

- Aggregate "Emerging Investigators" (2025)
- Marie Skłodowska-Curie Fellow (2020)

## Teaching

- Advanced Sensing Materials and Devices

## Postgraduate Supervision

- Shikai Yu
- Xinrui Li
- Hua Jiang
- Jing Chen
- Aoyuan Cheng
- Hongping Liu

<script>
(function() {
  var timelineProgress = document.getElementById('timeline-progress');
  var timeline = document.querySelector('.timeline');
  if (!timelineProgress || !timeline) return;

  var items = timeline.querySelectorAll('.timeline-item');

  // IntersectionObserver for in-view class
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
        }
      });
    }, { rootMargin: '0px 0px -15% 0px' });

    items.forEach(function(item, idx) {
      if (idx < 3) {
        // Reveal first 3 immediately on load (still gets the stagger transition)
        item.classList.add('in-view');
      } else {
        observer.observe(item);
      }
    });
  } else {
    items.forEach(function(item) { item.classList.add('in-view'); });
  }

  // Scroll progress bar
  window.addEventListener('scroll', function() {
    var rect = timeline.getBoundingClientRect();
    var totalHeight = timeline.offsetHeight;
    var windowH = window.innerHeight;
    var lineTop = 30;
    var lineBottom = 30;
    var lineHeight = totalHeight - lineTop - lineBottom;

    if (rect.top < windowH && rect.bottom > 0) {
      var scrolled = Math.min(1, Math.max(0, (windowH - rect.top - lineTop) / (totalHeight - lineTop + windowH * 0.4)));
      timelineProgress.style.height = Math.min(scrolled * lineHeight, lineHeight) + 'px';
    }
  }, { passive: true });
})();
</script>

<div class="hobby-quote">
<strong class="quote-text">An experiment is a question which Science poses to Nature and a measurement is the recording of Nature's answer. -- Max Planck</strong>
</div>
---

## Recent Publications

{% include recent-publications.html %}
