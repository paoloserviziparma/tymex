/* Tymex — comportamenti del sito. Nessun cookie, nessun tracciamento. */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var lang = doc.lang === "en" ? "en" : "it";

  /* Intestazione: scompare scorrendo in giù, ricompare in su; resta in cima e con il menu aperto */
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".menu-toggle");
  var menu = document.getElementById("mobile-menu");
  var lastY = window.scrollY, ticking = false;
  function onScroll() {
    var y = window.scrollY;
    if (header) {
      var open = menu && menu.classList.contains("is-open");
      header.classList.toggle("is-scrolled", y > 8);
      if (y < 80 || open || y < lastY - 2) header.classList.remove("is-hidden");
      else if (y > lastY + 2) header.classList.add("is-hidden");
    }
    lastY = y;
    parallax();
    ticking = false;
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { window.requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  header && header.addEventListener("focusin", function () { header.classList.remove("is-hidden"); });

  /* Menu a tendina su mobile */
  function setMenu(open) {
    if (!menu || !toggle) return;
    menu.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? toggle.dataset.close : toggle.dataset.open);
    if (open) header.classList.remove("is-hidden");
  }
  toggle && toggle.addEventListener("click", function () { setMenu(!menu.classList.contains("is-open")); });
  menu && menu.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { setMenu(false); closeVideo(); } });
  window.addEventListener("resize", function () { if (window.innerWidth > 1080) setMenu(false); });

  /* Titoli che salgono parola per parola */
  document.querySelectorAll("[data-split]").forEach(function (el) {
    if (reduce) return;
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (child) {
        if (child.nodeType === 3) {
          var parts = child.textContent.split(/(\s+)/);
          var frag = document.createDocumentFragment();
          parts.forEach(function (p) {
            if (!p) return;
            if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(" ")); return; }
            var w = document.createElement("span"); w.className = "w";
            var s = document.createElement("span"); s.textContent = p; s.style.setProperty("--i", i++);
            w.appendChild(s); frag.appendChild(w);
          });
          node.replaceChild(frag, child);
        } else if (child.nodeType === 1 && !child.classList.contains("kw")) { walk(child); }
      });
    })(el);
    el.classList.add("split-words");
  });

  /* Blocchi che compaiono allo scroll (IntersectionObserver) */
  var targets = document.querySelectorAll(".reveal, .split-words");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    targets.forEach(function (t) { io.observe(t); });
  } else { targets.forEach(function (t) { t.classList.add("is-in"); }); }

  /* Parallax leggero (dimezzato su mobile) */
  var pEls = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll("[data-parallax]"));
  function parallax() {
    if (!pEls.length) return;
    var vh = window.innerHeight, k = window.innerWidth < 768 ? 0.5 : 1;
    pEls.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var speed = parseFloat(el.dataset.parallax) || 0.08;
      var off = (r.top + r.height / 2 - vh / 2) * -speed * k;
      el.style.transform = "translate3d(0," + off.toFixed(1) + "px,0)";
    });
  }
  parallax();

  /* Finestra video: si carica solo al clic (YouTube senza cookie, Vimeo con dnt, mp4 locali) */
  var modal = null, lastFocus = null;
  function closeVideo() {
    if (!modal) return;
    modal.remove(); modal = null; document.body.style.overflow = "";
    lastFocus && lastFocus.focus();
  }
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-video]");
    if (!b) return;
    e.preventDefault();
    lastFocus = b;
    var src = b.dataset.video, type = b.dataset.videoType || "youtube", title = b.dataset.videoTitle || "Video";
    modal = document.createElement("div");
    modal.className = "video-modal"; modal.setAttribute("role", "dialog"); modal.setAttribute("aria-modal", "true"); modal.setAttribute("aria-label", title);
    var inner = document.createElement("div"); inner.className = "inner";
    var media;
    if (type === "mp4") { media = document.createElement("video"); media.src = src; media.controls = true; media.autoplay = true; media.playsInline = true; }
    else {
      media = document.createElement("iframe");
      media.src = type === "vimeo" ? "https://player.vimeo.com/video/" + src + "?dnt=1&autoplay=1" : "https://www.youtube-nocookie.com/embed/" + src + "?autoplay=1&rel=0";
      media.allow = "autoplay; fullscreen; picture-in-picture"; media.allowFullscreen = true; media.title = title;
    }
    var close = document.createElement("button");
    close.className = "close"; close.type = "button"; close.setAttribute("aria-label", lang === "en" ? "Close video" : "Chiudi video");
    close.innerHTML = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>';
    close.addEventListener("click", closeVideo);
    inner.appendChild(media); modal.appendChild(inner); modal.appendChild(close);
    modal.addEventListener("click", function (ev) { if (ev.target === modal) closeVideo(); });
    document.body.appendChild(modal); document.body.style.overflow = "hidden"; close.focus();
  });

  /* Selettore "Tymex fa per te?" — consiglio e modulo precompilato */
  var quiz = document.getElementById("quiz");
  if (quiz) {
    var steps = quiz.querySelectorAll("[data-step]");
    var dots = quiz.querySelectorAll(".progress span");
    var answers = {};
    var cur = 0;
    var T = JSON.parse(quiz.querySelector("script[type='application/json']").textContent);
    function show(n) {
      cur = n;
      steps.forEach(function (s, i) { s.hidden = i !== n; });
      dots.forEach(function (d, i) { d.classList.toggle("on", i <= Math.min(n, dots.length - 1)); });
      var focusable = steps[n].querySelector("legend, h3, button");
      if (focusable && n > 0) { focusable.setAttribute("tabindex", "-1"); focusable.focus({ preventScroll: true }); }
    }
    quiz.addEventListener("click", function (e) {
      var opt = e.target.closest(".opt");
      if (opt) {
        var step = opt.closest("[data-step]");
        step.querySelectorAll(".opt").forEach(function (o) { o.setAttribute("aria-pressed", o === opt ? "true" : "false"); });
        answers[step.dataset.step] = { v: opt.dataset.value, label: opt.textContent.trim() };
        setTimeout(function () { show(cur + 1); if (cur === steps.length - 1) result(); }, reduce ? 0 : 180);
        return;
      }
      if (e.target.closest("[data-back]")) { show(Math.max(0, cur - 1)); return; }
      if (e.target.closest("[data-restart]")) { answers = {}; quiz.querySelectorAll(".opt").forEach(function (o) { o.setAttribute("aria-pressed", "false"); }); show(0); return; }
      if (e.target.closest("[data-apply]")) { apply(); }
    });
    function result() {
      var out = quiz.querySelector("[data-result]");
      var pts = [];
      var a = answers;
      if (a.oggi) pts.push(T.oggi[a.oggi.v]);
      if (a.chi) pts.push(T.chi[a.chi.v]);
      if (a.gest) pts.push(T.gest[a.gest.v]);
      out.innerHTML = "";
      var p = document.createElement("p"); p.textContent = T.intro; out.appendChild(p);
      var ul = document.createElement("ul");
      pts.forEach(function (t) { var li = document.createElement("li"); li.textContent = t; ul.appendChild(li); });
      out.appendChild(ul);
    }
    function apply() {
      var form = document.getElementById("demo-form");
      if (!form) return;
      var n = quiz.querySelector("[name='quiz_persone']");
      var lines = [T.summary];
      ["oggi", "chi", "gest"].forEach(function (k) { if (answers[k]) lines.push("• " + T.q[k] + " " + answers[k].label); });
      if (n && n.value) lines.push("• " + T.q.persone + " " + n.value);
      var msg = form.querySelector("[name='messaggio']");
      if (msg) msg.value = lines.join("\n") + (msg.value ? "\n\n" + msg.value : "\n\n");
      var sel = form.querySelector("[name='utenti']");
      if (sel && n && n.value) {
        var v = parseInt(n.value, 10);
        sel.value = isNaN(v) ? sel.value : v <= 10 ? "1-10" : v <= 50 ? "11-50" : "50+";
      }
      var hid = form.querySelector("[name='selettore']");
      if (hid) hid.value = ["oggi", "chi", "gest"].map(function (k) { return answers[k] ? answers[k].v : "-"; }).join(" / ");
      document.getElementById("contatti").scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
      setTimeout(function () { var f = form.querySelector("[name='nome']"); f && f.focus({ preventScroll: true }); }, reduce ? 0 : 600);
    }
    show(0);
  }

  /* Anno corrente nel piè di pagina */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
