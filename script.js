const translations = {
  it: {
    "nav.services": "Servizi", "nav.about": "Chi siamo", "nav.contact": "Contatti", "nav.cta": "Contattaci",
    "hero.eyebrow": "AUTOMOTIVE · PRAVISDOMINI", "hero.lead": "Tutto per l’automobile, in un unico posto.",
    "hero.copy": "Noleggio, vendita, trasporto merci, soccorso stradale, autofficina, autoricambi e gommista. Un partner unico per ogni esigenza.",
    "hero.services": "Scopri i servizi", "hero.quote": "Richiedi informazioni", "facts.services": "SERVIZI INTEGRATI",
    "facts.contacts": "NUMERI DIRETTI", "facts.partner": "PARTNER UNICO", "facts.location": "SEDE A PRAVISDOMINI",
    "services.kicker": "SERVIZI", "services.title": "I nostri servizi",
    "services.intro": "Sette specialità, un solo partner. Soluzioni complete per te e per la tua automobile.",
    "services.cta": "Parliamo della tua esigenza", "service.open": "Scopri il servizio",
    "service.rental": "Noleggio", "service.sales": "Vendita auto", "service.transport": "Trasporto merci",
    "service.roadside": "Soccorso stradale", "service.workshop": "Autofficina", "service.parts": "Autoricambi", "service.tyres": "Gommista",
    "about.kicker": "NEWTON AUTOSERVICE", "about.title": "Una risposta completa per la tua mobilità.",
    "about.copy": "Newton riunisce servizi automotive e trasporto in un unico punto di riferimento a Pravisdomini. Un contatto semplice, soluzioni coordinate e attenzione concreta alle tue necessità.",
    "about.one": "Servizi per privati, professionisti e imprese", "about.two": "Assistenza chiara e diretta",
    "about.three": "Sette competenze, un solo partner", "about.link": "Contatta Newton", "contact.kicker": "CONTATTI",
    "contact.title": "Parliamo della tua esigenza.", "contact.copy": "Chiamaci, scrivici su WhatsApp o vieni a trovarci a Pravisdomini.",
    "contact.addressLabel": "INDIRIZZO", "contact.primary": "NUMERO PRINCIPALE E WHATSAPP", "contact.info": "INFORMAZIONI",
    "contact.whatsapp": "Scrivici su WhatsApp", "contact.call": "Chiama ora", "footer.copy": "Servizi automotive e trasporto a Pravisdomini."
  },
  en: {
    "nav.services": "Services", "nav.about": "About us", "nav.contact": "Contact", "nav.cta": "Contact us",
    "hero.eyebrow": "AUTOMOTIVE · PRAVISDOMINI", "hero.lead": "Everything for your vehicle, all in one place.",
    "hero.copy": "Rental, vehicle sales, freight transport, roadside assistance, workshop, spare parts and tyre services. One partner for every need.",
    "hero.services": "Explore services", "hero.quote": "Request information", "facts.services": "INTEGRATED SERVICES",
    "facts.contacts": "DIRECT NUMBERS", "facts.partner": "ONE PARTNER", "facts.location": "BASED IN PRAVISDOMINI",
    "services.kicker": "SERVICES", "services.title": "Our services",
    "services.intro": "Seven specialities, one partner. Complete solutions for you and your vehicle.",
    "services.cta": "Tell us what you need", "service.open": "View service",
    "service.rental": "Vehicle rental", "service.sales": "Vehicle sales", "service.transport": "Freight transport",
    "service.roadside": "Roadside assistance", "service.workshop": "Workshop", "service.parts": "Spare parts", "service.tyres": "Tyre service",
    "about.kicker": "NEWTON AUTOSERVICE", "about.title": "One complete answer for your mobility.",
    "about.copy": "Newton brings automotive and transport services together at one trusted location in Pravisdomini. A simple point of contact, coordinated solutions and genuine attention to your needs.",
    "about.one": "Services for individuals, professionals and businesses", "about.two": "Clear, direct assistance",
    "about.three": "Seven areas of expertise, one partner", "about.link": "Contact Newton", "contact.kicker": "CONTACT",
    "contact.title": "Let’s talk about what you need.", "contact.copy": "Call us, message us on WhatsApp or visit us in Pravisdomini.",
    "contact.addressLabel": "ADDRESS", "contact.primary": "PRIMARY NUMBER & WHATSAPP", "contact.info": "INFORMATION",
    "contact.whatsapp": "Message us on WhatsApp", "contact.call": "Call now", "footer.copy": "Automotive and transport services in Pravisdomini."
  }
};

let language = localStorage.getItem("newton-language") === "en" ? "en" : "it";

function applyLanguage(lang) {
  language = lang;
  document.documentElement.lang = lang;
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const textValue = translations[lang][element.dataset.i18n];
    if (textValue) element.textContent = textValue;
  });
  document.querySelectorAll(".language-switch [data-lang]").forEach((button) => {
    const active = button.dataset.lang === lang;
    button.classList.toggle("active", active);
    button.setAttribute("aria-pressed", String(active));
  });
  document.title = lang === "it"
    ? "Newton Autoservice | Servizi automotive a Pravisdomini"
    : "Newton Autoservice | Automotive services in Pravisdomini";
  localStorage.setItem("newton-language", lang);
}

document.querySelectorAll(".language-switch [data-lang]").forEach((button) => {
  button.addEventListener("click", () => applyLanguage(button.dataset.lang));
});

const menu = document.querySelector(".main-nav");
const toggle = document.querySelector(".menu-toggle");
toggle.addEventListener("click", () => {
  const open = menu.classList.toggle("open");
  toggle.setAttribute("aria-expanded", String(open));
});
menu.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => {
  menu.classList.remove("open");
  toggle.setAttribute("aria-expanded", "false");
}));

document.getElementById("year").textContent = new Date().getFullYear();
applyLanguage(language);
