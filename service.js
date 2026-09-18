const menu = document.querySelector(".main-nav");
const toggle = document.querySelector(".menu-toggle");

if (location.pathname.endsWith("/servizio.html")) {
  const legacyRoutes = {
    rental: "noleggio/",
    sales: "vendita-auto/",
    transport: "trasporto-merci/",
    roadside: "soccorso-stradale/",
    workshop: "autofficina/",
    parts: "autoricambi/",
    tyres: "gommista/"
  };
  const type = new URLSearchParams(location.search).get("tipo");
  if (legacyRoutes[type]) location.replace(`/${legacyRoutes[type]}`);
}

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
