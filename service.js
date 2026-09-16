const ui = {
  it: {
    "nav.services":"Servizi","nav.about":"Chi siamo","nav.contact":"Contatti","nav.cta":"Contattaci",
    "back":"Tutti i servizi","whatsapp":"Scrivici su WhatsApp","call":"Chiama ora","detail.kicker":"IL SERVIZIO",
    "gallery":"GALLERIA","contact.title":"Hai bisogno di questo servizio?",
    "contact.copy":"Parla direttamente con Newton Autoservice. Ti daremo tutte le informazioni necessarie.",
    "more.kicker":"ALTRI SERVIZI","more.title":"Scopri anche","footer":"Servizi automotive e trasporto a Pravisdomini."
  },
  en: {
    "nav.services":"Services","nav.about":"About us","nav.contact":"Contact","nav.cta":"Contact us",
    "back":"All services","whatsapp":"Message us on WhatsApp","call":"Call now","detail.kicker":"THE SERVICE",
    "gallery":"GALLERY","contact.title":"Do you need this service?",
    "contact.copy":"Speak directly with Newton Autoservice. We will give you all the information you need.",
    "more.kicker":"OTHER SERVICES","more.title":"You may also need","footer":"Automotive and transport services in Pravisdomini."
  }
};

const services = {
  rental: {
    image:"https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&w=2200&q=88",
    photos:["photo-1549317661-bd32c8ce0db2","photo-1590362891991-f776e747a588","photo-1503376780353-7e6692767b70"],
    it:{title:"Noleggio",lead:"Soluzioni di mobilità per privati, professionisti e imprese.",description:"Contattaci per conoscere veicoli disponibili, condizioni e soluzioni più adatte alle tue esigenze.",features:["Informazioni chiare sulla disponibilità","Soluzioni per esigenze diverse","Contatto diretto con Newton"]},
    en:{title:"Vehicle rental",lead:"Mobility solutions for individuals, professionals and businesses.",description:"Contact us to learn about available vehicles, terms and the solution best suited to your needs.",features:["Clear availability information","Solutions for different needs","Direct contact with Newton"]}
  },
  sales: {
    image:"https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=2200&q=88",
    photos:["photo-1492144534655-ae79c964c9d7","photo-1542282088-72c9c27ed0cd","photo-1550355291-bbee04a92027"],
    it:{title:"Vendita auto",lead:"Supporto diretto nella scelta del tuo prossimo veicolo.",description:"Scopri le proposte disponibili e parla con noi per ricevere informazioni sul veicolo che ti interessa.",features:["Veicoli consultabili con semplicità","Informazioni prima dell’acquisto","Assistenza diretta nella scelta"]},
    en:{title:"Vehicle sales",lead:"Direct support when choosing your next vehicle.",description:"Explore the available vehicles and speak with us for information about the one that interests you.",features:["Easy-to-view vehicles","Information before purchase","Direct help with your choice"]}
  },
  transport: {
    image:"https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&w=2200&q=88",
    photos:["photo-1601584115197-04ecc0da31d7","photo-1586191582151-f73872dfd183","photo-1559297434-fae8a1916a79"],
    it:{title:"Trasporto merci",lead:"Soluzioni di trasporto organizzate intorno alle tue necessità.",description:"Parlaci della merce e della destinazione: valuteremo insieme la soluzione più adatta.",features:["Servizio per professionisti e imprese","Organizzazione in base alla richiesta","Un contatto semplice e diretto"]},
    en:{title:"Freight transport",lead:"Transport solutions organised around your needs.",description:"Tell us about the goods and destination, and we will assess the most suitable solution with you.",features:["Service for professionals and businesses","Organisation based on your request","One simple, direct contact"]}
  },
  roadside: {
    image:"https://images.unsplash.com/photo-1503736334956-4c8f8e92946d?auto=format&fit=crop&w=2200&q=88",
    photos:["photo-1503736334956-4c8f8e92946d","photo-1486006920555-c77dcf18193c","photo-1530046339160-ce3e530c7d2f"],
    it:{title:"Soccorso stradale",lead:"Un riferimento diretto quando un imprevisto ferma il viaggio.",description:"Chiamaci per descrivere il problema e la posizione del veicolo. Ti forniremo le informazioni utili per richiedere assistenza.",features:["Contatto telefonico immediato","Valutazione della situazione","Indicazioni chiare sul supporto"]},
    en:{title:"Roadside assistance",lead:"A direct point of contact when an unexpected issue stops your journey.",description:"Call us to describe the problem and vehicle location. We will provide the information needed to request assistance.",features:["Immediate telephone contact","Assessment of the situation","Clear guidance on support"]}
  },
  workshop: {
    image:"https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?auto=format&fit=crop&w=2200&q=88",
    photos:["photo-1486262715619-67b85e0b08d3","photo-1530046339160-ce3e530c7d2f","photo-1619642751034-765dfdf7c58e"],
    it:{title:"Autofficina",lead:"Controlli, manutenzione e interventi per il tuo veicolo.",description:"Raccontaci il problema o il tipo di intervento richiesto. Ti aiuteremo a organizzare il controllo del veicolo.",features:["Manutenzione e controlli","Valutazione delle necessità del veicolo","Informazioni dirette sull’intervento"]},
    en:{title:"Workshop",lead:"Inspections, maintenance and service for your vehicle.",description:"Tell us about the problem or the service you need. We will help arrange an inspection of your vehicle.",features:["Maintenance and inspections","Assessment of vehicle needs","Direct information about the work"]}
  },
  parts: {
    image:"https://images.unsplash.com/photo-1580894908361-967195033215?auto=format&fit=crop&w=2200&q=88",
    photos:["photo-1580894908361-967195033215","photo-1487754180451-c456f719a1fc","photo-1493238792000-8113da705763"],
    it:{title:"Autoricambi",lead:"Ricambi e componenti per le esigenze del tuo veicolo.",description:"Indicaci veicolo e componente necessario: verificheremo con te la richiesta e le informazioni utili.",features:["Ricerca in base al veicolo","Verifica della richiesta","Supporto diretto prima dell’acquisto"]},
    en:{title:"Spare parts",lead:"Parts and components for your vehicle’s needs.",description:"Tell us the vehicle and part you need, and we will check your request and the relevant information with you.",features:["Search based on your vehicle","Request verification","Direct support before purchase"]}
  },
  tyres: {
    image:"https://images.unsplash.com/photo-1578844251758-2f71da64c96f?auto=format&fit=crop&w=2200&q=88",
    photos:["photo-1578844251758-2f71da64c96f","photo-1557411732-1797a9171fcf","photo-1606577924006-27d39b132ae2"],
    it:{title:"Gommista",lead:"Servizi pneumatici per sicurezza, aderenza e controllo.",description:"Contattaci per informazioni sui pneumatici e sul servizio più adatto al tuo veicolo.",features:["Verifica delle esigenze del veicolo","Informazioni sui pneumatici","Supporto diretto per il servizio"]},
    en:{title:"Tyre service",lead:"Tyre services for safety, grip and control.",description:"Contact us for tyre information and the service best suited to your vehicle.",features:["Assessment of vehicle needs","Tyre information","Direct service support"]}
  }
};

const type = Object.hasOwn(services, new URLSearchParams(location.search).get("tipo")) ? new URLSearchParams(location.search).get("tipo") : "workshop";
let language = localStorage.getItem("newton-language") === "en" ? "en" : "it";

function imageUrl(id, width) {
  return `https://images.unsplash.com/${id}?auto=format&fit=crop&w=${width}&q=86`;
}

function renderService() {
  const service = services[type];
  const content = service[language];
  document.getElementById("service-hero").style.setProperty("--service-image", `url('${service.image}')`);
  document.getElementById("service-title").textContent = content.title;
  document.getElementById("service-lead").textContent = content.lead;
  document.getElementById("detail-title").textContent = language === "it" ? "Come possiamo aiutarti" : "How we can help";
  document.getElementById("service-description").textContent = content.description;
  document.getElementById("service-features").replaceChildren(...content.features.map((feature) => {
    const item = document.createElement("li"); item.textContent = feature; return item;
  }));
  document.getElementById("service-gallery").replaceChildren(...service.photos.map((photo, index) => {
    const figure = document.createElement("figure");
    const link = document.createElement("a");
    link.href = imageUrl(photo, 2000); link.target = "_blank"; link.rel = "noopener";
    const image = document.createElement("img");
    image.src = imageUrl(photo, index === 0 ? 1500 : 900); image.alt = `${content.title} — ${index + 1}`; image.loading = index ? "lazy" : "eager";
    link.append(image); figure.append(link); return figure;
  }));
  document.getElementById("more-links").replaceChildren(...Object.entries(services).filter(([key]) => key !== type).map(([key, value]) => {
    const link = document.createElement("a"); link.href = `servizio.html?tipo=${key}`; link.textContent = `${value[language].title} ↗`; return link;
  }));
  document.title = `${content.title} | Newton Autoservice`;
  const description = `${content.lead} ${content.description}`;
  const canonical = `https://newtonvts.it/servizio.html?tipo=${type}`;
  document.querySelector('meta[name="description"]').setAttribute("content", description);
  document.querySelector('meta[property="og:title"]').setAttribute("content", `${content.title} | Newton Autoservice`);
  document.querySelector('meta[property="og:description"]').setAttribute("content", description);
  document.querySelector('meta[property="og:url"]').setAttribute("content", canonical);
  document.querySelector('link[rel="canonical"]').setAttribute("href", canonical);
}

function applyLanguage(lang) {
  language = lang;
  document.documentElement.lang = lang;
  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const textValue = ui[lang][element.dataset.i18n]; if (textValue) element.textContent = textValue;
  });
  document.querySelectorAll(".language-switch [data-lang]").forEach((button) => {
    const active = button.dataset.lang === lang;
    button.classList.toggle("active", active); button.setAttribute("aria-pressed", String(active));
  });
  localStorage.setItem("newton-language", lang);
  renderService();
}

document.querySelectorAll(".language-switch [data-lang]").forEach((button) => button.addEventListener("click", () => applyLanguage(button.dataset.lang)));
const menu = document.querySelector(".main-nav");
const toggle = document.querySelector(".menu-toggle");
toggle.addEventListener("click", () => { const open = menu.classList.toggle("open"); toggle.setAttribute("aria-expanded", String(open)); });
document.getElementById("year").textContent = new Date().getFullYear();
applyLanguage(language);
