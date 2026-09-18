const menu = document.querySelector(".main-nav");
const toggle = document.querySelector(".menu-toggle");

if (menu && toggle) {
  toggle.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
  menu.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => {
    menu.classList.remove("open");
    toggle.setAttribute("aria-expanded", "false");
  }));
}

const year = document.getElementById("year");
if (year) year.textContent = new Date().getFullYear();

if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("is-visible");
      observer.unobserve(entry.target);
    }
  }), { threshold: 0.12 });

  document.querySelectorAll(".service-card,.process-grid article,.about-image,.about-copy,.faq-list details,.contact-card,.map-wrap").forEach((element) => {
    element.classList.add("reveal");
    observer.observe(element);
  });
}
