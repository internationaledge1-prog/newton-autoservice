from pathlib import Path
from html import escape
from urllib.parse import quote

ROOT = Path(__file__).parent

SERVICES = {
    "noleggio": {
        "key": "rental",
        "image": "photo-1549317661-bd32c8ce0db2",
        "photos": ["photo-1549317661-bd32c8ce0db2", "photo-1550355291-bbee04a92027", "photo-1449965408869-eaa3f722e40d"],
        "it": {
            "title": "Noleggio auto",
            "meta": "Noleggio auto a Pravisdomini per privati e imprese. Contatta Newton Autoservice per disponibilità, informazioni e soluzioni di mobilità.",
            "lead": "Mobilità flessibile per privati, professionisti e imprese.",
            "description": "Hai bisogno di un veicolo per lavoro, per un viaggio o per una necessità temporanea? Raccontaci le tue esigenze: ti forniremo informazioni chiare sulle soluzioni disponibili e ti aiuteremo a scegliere quella più adatta.",
            "features": ["Soluzioni per privati e imprese", "Informazioni chiare prima della scelta", "Assistenza diretta da parte di Newton"],
            "faq": [("Come posso chiedere la disponibilità?", "Puoi telefonare oppure scriverci su WhatsApp indicando periodo ed esigenza."), ("Il servizio è disponibile anche per imprese?", "Sì, valutiamo richieste di privati, professionisti e imprese.")],
        },
        "en": {
            "title": "Vehicle rental",
            "meta": "Vehicle rental in Pravisdomini for individuals and businesses. Contact Newton Autoservice for availability and mobility solutions.",
            "lead": "Flexible mobility for individuals, professionals and businesses.",
            "description": "Need a vehicle for work, a journey or a temporary requirement? Tell us what you need and we will provide clear information about available solutions and help you choose the right option.",
            "features": ["Solutions for individuals and businesses", "Clear information before you choose", "Direct assistance from Newton"],
            "faq": [("How can I ask about availability?", "Call or message us on WhatsApp with the dates and your requirements."), ("Is the service available to businesses?", "Yes, we assess requests from individuals, professionals and businesses.")],
        },
    },
    "vendita-auto": {
        "key": "sales",
        "image": "photo-1492144534655-ae79c964c9d7",
        "photos": ["photo-1492144534655-ae79c964c9d7", "photo-1503376780353-7e6692767b70", "photo-1553440569-bcc63803a83d"],
        "it": {
            "title": "Vendita auto",
            "meta": "Vendita auto a Pravisdomini con assistenza diretta nella scelta del veicolo. Contatta Newton Autoservice per informazioni e disponibilità.",
            "lead": "Supporto diretto nella ricerca e nella scelta del veicolo.",
            "description": "Cerchi un’automobile? Parlaci del modello, del budget e dell’utilizzo previsto. Ti aiuteremo a valutare le proposte disponibili e a ottenere le informazioni necessarie prima della scelta.",
            "features": ["Ricerca in base alle tue esigenze", "Informazioni prima dell’acquisto", "Contatto diretto durante la scelta"],
            "faq": [("Come posso conoscere le auto disponibili?", "Contattaci per ricevere le informazioni aggiornate sui veicoli disponibili."), ("Posso indicare modello e budget?", "Sì. Modello, budget e tipo di utilizzo ci aiutano a comprendere meglio la tua richiesta.")],
        },
        "en": {
            "title": "Vehicle sales",
            "meta": "Vehicle sales in Pravisdomini with direct assistance in choosing a car. Contact Newton Autoservice for information and availability.",
            "lead": "Direct support when searching for and choosing a vehicle.",
            "description": "Looking for a car? Tell us the model, budget and intended use. We will help you assess the available options and obtain the information you need before choosing.",
            "features": ["Search based on your needs", "Information before purchase", "Direct contact while you choose"],
            "faq": [("How can I see available vehicles?", "Contact us for current information about available vehicles."), ("Can I specify a model and budget?", "Yes. The model, budget and intended use help us understand your request.")],
        },
    },
    "trasporto-merci": {
        "key": "transport",
        "image": "photo-1601584115197-04ecc0da31d7",
        "photos": ["photo-1601584115197-04ecc0da31d7", "photo-1586191582151-f73872dfd183", "photo-1559297434-fae8a1916a79"],
        "it": {
            "title": "Trasporto merci",
            "meta": "Trasporto merci a Pravisdomini per professionisti e imprese. Contatta Newton Autoservice per descrivere merce, destinazione ed esigenze.",
            "lead": "Soluzioni di trasporto organizzate intorno alle tue necessità.",
            "description": "Indicaci la tipologia di merce, il punto di partenza e la destinazione. Valuteremo la richiesta e ti forniremo le informazioni utili per organizzare il trasporto.",
            "features": ["Servizio per professionisti e imprese", "Organizzazione in base alla richiesta", "Un contatto semplice e diretto"],
            "faq": [("Quali informazioni devo fornire?", "Tipologia di merce, quantità, partenza, destinazione e periodo desiderato."), ("Posso chiedere informazioni senza impegno?", "Sì, contattaci per descrivere la richiesta e verificare la soluzione possibile.")],
        },
        "en": {
            "title": "Freight transport",
            "meta": "Freight transport in Pravisdomini for professionals and businesses. Contact Newton Autoservice with the goods and destination details.",
            "lead": "Transport solutions organised around your needs.",
            "description": "Tell us the type of goods, collection point and destination. We will assess the request and provide the information needed to organise transport.",
            "features": ["Service for professionals and businesses", "Organisation based on your request", "One simple, direct contact"],
            "faq": [("What information should I provide?", "The type and quantity of goods, collection point, destination and preferred date."), ("Can I ask for information without commitment?", "Yes, contact us to describe your request and check the possible solution.")],
        },
    },
    "soccorso-stradale": {
        "key": "roadside",
        "image": "photo-1503736334956-4c8f8e92946d",
        "photos": ["photo-1503736334956-4c8f8e92946d", "photo-1486006920555-c77dcf18193c", "photo-1530046339160-ce3e530c7d2f"],
        "it": {
            "title": "Soccorso stradale",
            "meta": "Soccorso stradale a Pravisdomini e informazioni per assistenza al veicolo. Chiama Newton Autoservice e comunica posizione e problema.",
            "lead": "Un riferimento diretto quando un imprevisto ferma il viaggio.",
            "description": "Se il veicolo è fermo, chiamaci e comunica la posizione, il tipo di veicolo e il problema riscontrato. Ti daremo indicazioni chiare sul supporto disponibile.",
            "features": ["Contatto telefonico immediato", "Valutazione della situazione", "Indicazioni chiare sul supporto"],
            "faq": [("Cosa devo comunicare al telefono?", "La posizione, il tipo di veicolo e una breve descrizione del problema."), ("Posso contattarvi tramite WhatsApp?", "Sì, puoi inviare un messaggio; in caso di urgenza è preferibile telefonare.")],
        },
        "en": {
            "title": "Roadside assistance",
            "meta": "Roadside assistance in Pravisdomini and vehicle support information. Call Newton Autoservice with your location and the problem.",
            "lead": "A direct point of contact when an unexpected issue stops your journey.",
            "description": "If your vehicle has stopped, call us with the location, vehicle type and a description of the issue. We will give you clear guidance about available support.",
            "features": ["Immediate telephone contact", "Assessment of the situation", "Clear guidance on support"],
            "faq": [("What should I say when I call?", "Provide your location, vehicle type and a brief description of the issue."), ("Can I contact you through WhatsApp?", "Yes. You can message us, although calling is preferable in an urgent situation.")],
        },
    },
    "autofficina": {
        "key": "workshop",
        "image": "photo-1486262715619-67b85e0b08d3",
        "photos": ["photo-1486262715619-67b85e0b08d3", "photo-1530046339160-ce3e530c7d2f", "photo-1619642751034-765dfdf7c58e"],
        "it": {
            "title": "Autofficina",
            "meta": "Autofficina a Pravisdomini per controlli, manutenzione e interventi sul veicolo. Contatta Newton Autoservice per informazioni.",
            "lead": "Controlli, manutenzione e interventi per il tuo veicolo.",
            "description": "Descrivici il problema, i sintomi o l’intervento richiesto. Ti aiuteremo a organizzare il controllo del veicolo e ti forniremo informazioni chiare sui passaggi successivi.",
            "features": ["Manutenzione e controlli", "Valutazione delle necessità del veicolo", "Informazioni dirette sull’intervento"],
            "faq": [("Come posso richiedere un controllo?", "Telefonaci o scrivici indicando veicolo, problema e disponibilità."), ("Devo descrivere il problema in anticipo?", "Una breve descrizione ci aiuta a comprendere la richiesta prima del controllo.")],
        },
        "en": {
            "title": "Workshop",
            "meta": "Automotive workshop in Pravisdomini for inspections, maintenance and vehicle service. Contact Newton Autoservice for information.",
            "lead": "Inspections, maintenance and service for your vehicle.",
            "description": "Describe the problem, symptoms or service required. We will help arrange an inspection and give you clear information about the next steps.",
            "features": ["Maintenance and inspections", "Assessment of vehicle needs", "Direct information about the work"],
            "faq": [("How can I request an inspection?", "Call or message us with the vehicle, issue and your availability."), ("Should I describe the problem first?", "A brief description helps us understand your request before the inspection.")],
        },
    },
    "autoricambi": {
        "key": "parts",
        "image": "photo-1580894908361-967195033215",
        "photos": ["photo-1580894908361-967195033215", "photo-1487754180451-c456f719a1fc", "photo-1493238792000-8113da705763"],
        "it": {
            "title": "Autoricambi",
            "meta": "Autoricambi a Pravisdomini: ricerca di ricambi e componenti in base al veicolo. Contatta Newton Autoservice con targa o dati del mezzo.",
            "lead": "Ricambi e componenti per le esigenze del tuo veicolo.",
            "description": "Indicaci marca, modello, anno e componente necessario. Verificheremo la richiesta con te per identificare correttamente il ricambio e fornirti le informazioni disponibili.",
            "features": ["Ricerca in base al veicolo", "Verifica della richiesta", "Supporto diretto prima dell’acquisto"],
            "faq": [("Quali dati servono per cercare un ricambio?", "Marca, modello, anno, motorizzazione e, quando utile, targa o telaio."), ("Posso inviare una fotografia del componente?", "Sì, puoi inviarla su WhatsApp insieme ai dati del veicolo.")],
        },
        "en": {
            "title": "Spare parts",
            "meta": "Spare parts in Pravisdomini: parts and components identified for your vehicle. Contact Newton Autoservice with the vehicle details.",
            "lead": "Parts and components for your vehicle’s needs.",
            "description": "Tell us the make, model, year and part required. We will check the request with you to identify the correct component and provide the available information.",
            "features": ["Search based on your vehicle", "Request verification", "Direct support before purchase"],
            "faq": [("What details are needed to find a part?", "Make, model, year, engine and, when useful, registration or chassis number."), ("Can I send a photo of the part?", "Yes, send it on WhatsApp together with the vehicle details.")],
        },
    },
    "gommista": {
        "key": "tyres",
        "image": "photo-1578844251758-2f71da64c96f",
        "photos": ["photo-1578844251758-2f71da64c96f", "photo-1557411732-1797a9171fcf", "photo-1606577924006-27d39b132ae2"],
        "it": {
            "title": "Gommista",
            "meta": "Gommista a Pravisdomini per informazioni su pneumatici e servizi per il veicolo. Contatta Newton Autoservice indicando misura e modello.",
            "lead": "Servizi pneumatici per sicurezza, aderenza e controllo.",
            "description": "Contattaci indicando il veicolo e la misura degli pneumatici. Ti aiuteremo a verificare le esigenze del mezzo e a ricevere informazioni sul servizio più adatto.",
            "features": ["Verifica delle esigenze del veicolo", "Informazioni sugli pneumatici", "Supporto diretto per il servizio"],
            "faq": [("Dove trovo la misura degli pneumatici?", "È indicata sul fianco dello pneumatico e sulla documentazione del veicolo."), ("Posso inviare la misura tramite WhatsApp?", "Sì, puoi inviare la misura oppure una fotografia leggibile del fianco dello pneumatico.")],
        },
        "en": {
            "title": "Tyre service",
            "meta": "Tyre service in Pravisdomini for information about tyres and vehicle services. Contact Newton Autoservice with the tyre size and model.",
            "lead": "Tyre services for safety, grip and control.",
            "description": "Contact us with the vehicle and tyre size. We will help check the vehicle’s requirements and provide information about the most suitable service.",
            "features": ["Assessment of vehicle needs", "Tyre information", "Direct service support"],
            "faq": [("Where can I find the tyre size?", "It is shown on the tyre sidewall and in the vehicle documentation."), ("Can I send the size through WhatsApp?", "Yes, send the size or a clear photo of the tyre sidewall.")],
        },
    },
}

LABELS = {
    "it": {"services": "Servizi", "about": "Chi siamo", "contact": "Contatti", "all": "Tutti i servizi", "service": "IL SERVIZIO", "help": "Come possiamo aiutarti", "gallery": "GALLERIA", "need": "Hai bisogno di questo servizio?", "talk": "Parla direttamente con Newton Autoservice. Ti daremo tutte le informazioni necessarie.", "whatsapp": "Scrivici su WhatsApp", "call": "Chiama ora", "faq": "Domande frequenti", "other": "Scopri anche", "footer": "Servizi automotive e trasporto a Pravisdomini.", "skip": "Vai al contenuto"},
    "en": {"services": "Services", "about": "About us", "contact": "Contact", "all": "All services", "service": "THE SERVICE", "help": "How we can help", "gallery": "GALLERY", "need": "Do you need this service?", "talk": "Speak directly with Newton Autoservice. We will give you all the information you need.", "whatsapp": "Message us on WhatsApp", "call": "Call now", "faq": "Frequently asked questions", "other": "Discover more", "footer": "Automotive and transport services in Pravisdomini.", "skip": "Skip to content"},
}


def img_url(photo, width=1600):
    return f"https://images.unsplash.com/{photo}?auto=format&fit=crop&w={width}&q=84"


def service_page(slug, lang):
    service = SERVICES[slug]
    content = service[lang]
    labels = LABELS[lang]
    english = lang == "en"
    depth = "../../" if english else "../"
    home = "../" if english else "../"
    canonical = f"https://newtonvts.it/{'en/' if english else ''}{slug}/"
    italian_url = f"https://newtonvts.it/{slug}/"
    english_url = f"https://newtonvts.it/en/{slug}/"
    lang_switch = f'<a href="{depth}{slug}/" lang="it" hreflang="it">IT</a><a class="active" href="../{slug}/" lang="en" hreflang="en">EN</a>' if english else f'<a class="active" href="./" lang="it" hreflang="it">IT</a><a href="../en/{slug}/" lang="en" hreflang="en">EN</a>'
    email_subject = quote(("Richiesta informazioni: " if lang == "it" else "Information request: ") + content["title"])
    email_body = quote((f"Buongiorno Newton Autoservice,\n\nvorrei ricevere informazioni sul servizio {content['title']}.\n\nGrazie." if lang == "it" else f"Hello Newton Autoservice,\n\nI would like more information about {content['title']}.\n\nThank you."))
    features = "".join(f"<li>{escape(item)}</li>" for item in content["features"])
    gallery = "".join(f'<figure><a href="{img_url(photo, 2000)}" target="_blank" rel="noopener"><img src="{img_url(photo, 1000 if i else 1600)}" alt="{escape(content["title"])} — Newton Autoservice {i+1}" width="1200" height="800" {'loading="lazy"' if i else 'fetchpriority="high"'}></a></figure>' for i, photo in enumerate(service["photos"]))
    faq_html = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in content["faq"])
    others = "".join(f'<a href="{home}{other_slug}/">{escape(other[lang]["title"])} ↗</a>' for other_slug, other in SERVICES.items() if other_slug != slug)
    faq_schema = ",".join(f'{{"@type":"Question","name":{json_string(q)},"acceptedAnswer":{{"@type":"Answer","text":{json_string(a)}}}}}' for q, a in content["faq"])
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(content['title'])} {'in' if english else 'a'} Pravisdomini | Newton Autoservice</title>
  <meta name="description" content="{escape(content['meta'])}">
  <meta name="theme-color" content="#090a0a">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="it" href="{italian_url}">
  <link rel="alternate" hreflang="en" href="{english_url}">
  <link rel="alternate" hreflang="x-default" href="{italian_url}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(content['title'])} | Newton Autoservice">
  <meta property="og:description" content="{escape(content['meta'])}">
  <meta property="og:image" content="{img_url(service['image'], 1600)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="{'en_GB' if english else 'it_IT'}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{depth}assets/newton-mark.png" type="image/png">
  <link rel="preconnect" href="https://images.unsplash.com" crossorigin>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&amp;family=Oswald:wght@500;600&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{depth}styles.css">
  <link rel="stylesheet" href="{depth}enhancements.css">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Service","name":{json_string(content['title'])},"description":{json_string(content['meta'])},"url":"{canonical}","image":"{img_url(service['image'], 1600)}","areaServed":{{"@type":"AdministrativeArea","name":"Pravisdomini, Pordenone"}},"provider":{{"@type":"AutomotiveBusiness","name":"Newton Autoservice","url":"https://newtonvts.it/","telephone":"+394341801744","email":"info@newtonvts.it","address":{{"@type":"PostalAddress","streetAddress":"Via Isonzo, 65","postalCode":"33076","addressLocality":"Pravisdomini","addressRegion":"PN","addressCountry":"IT"}}}}}}
  </script>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_schema}]}}</script>
</head>
<body id="top">
  <a class="skip-link" href="#main">{labels['skip']}</a>
  <header class="site-header inner-header">
    <a class="brand" href="{home}" aria-label="Newton Autoservice home"><img src="{depth}assets/newton-mark.png" alt="Newton Autoservice" width="70" height="66"><span><strong>Newton</strong><small>AUTOSERVICE</small></span></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-nav" aria-label="Menu"><span></span><span></span></button>
    <nav id="main-nav" class="main-nav" aria-label="Main navigation"><a href="{home}#servizi">{labels['services']}</a><a href="{home}#chi-siamo">{labels['about']}</a><a href="{home}#contatti">{labels['contact']}</a></nav>
    <div class="header-actions"><div class="language-switch" aria-label="Language">{lang_switch}</div><a class="button button-gold header-cta" href="tel:+394341801744">{labels['contact']}</a></div>
  </header>
  <main id="main" class="service-page-main">
    <section class="service-page-hero">
      <img class="service-hero-image" src="{img_url(service['image'], 2000)}" alt="{escape(content['title'])} — Newton Autoservice" width="2000" height="1125" fetchpriority="high">
      <div class="service-hero-shade"></div>
      <div class="hero-content"><a class="back-link" href="{home}#servizi"><span>←</span><span>{labels['all']}</span></a><div class="eyebrow"><span></span><span>NEWTON AUTOSERVICE</span></div><h1>{escape(content['title'])}</h1><p class="hero-copy">{escape(content['lead'])}</p><div class="hero-buttons"><a class="button button-gold" href="https://wa.me/394341801744" target="_blank" rel="noopener"><span>{labels['whatsapp']}</span><span>↗</span></a><a class="button button-outline" href="tel:+394341801744"><span>☎</span><span>{labels['call']}</span></a></div></div>
    </section>
    <section class="section service-detail"><div class="service-detail-copy"><p class="kicker">{labels['service']}</p><h2>{labels['help']}</h2><p>{escape(content['description'])}</p><ul class="service-detail-list">{features}</ul></div><div><p class="kicker gallery-label">{labels['gallery']}</p><div class="service-gallery">{gallery}</div></div></section>
    <section class="section faq-section service-faq"><div class="section-heading"><div><p class="kicker">FAQ</p><h2>{labels['faq']}</h2></div></div><div class="faq-list">{faq_html}</div></section>
    <section class="detail-contact"><div><h2>{labels['need']}</h2><p>{labels['talk']}</p></div><div class="detail-contact-actions"><a class="button whatsapp" href="https://wa.me/394341801744" target="_blank" rel="noopener">{labels['whatsapp']}</a><a class="button" href="tel:+394341801744">{labels['call']}</a><a class="button" href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=info%40newtonvts.it&amp;su={escape(email_subject)}&amp;body={email_body}" target="_blank" rel="noopener"><span aria-hidden="true">✉</span><span>info@newtonvts.it</span></a></div></section>
    <section class="section more-services"><p class="kicker">{labels['services'].upper()}</p><h2>{labels['other']}</h2><div class="more-links">{others}</div></section>
  </main>
  <footer class="site-footer"><a class="brand footer-brand" href="{home}"><img src="{depth}assets/newton-mark.png" alt="" width="54" height="51"><span><strong>Newton</strong><small>AUTOSERVICE</small></span></a><p>{labels['footer']}</p><p>© <span id="year"></span> Newton Autoservice</p></footer>
  <a class="floating-whatsapp" href="https://wa.me/394341801744" target="_blank" rel="noopener" aria-label="WhatsApp Newton">◉</a>
  <nav class="mobile-contact-dock" aria-label="Quick contacts"><a href="tel:+394341801744"><span>☎</span><span>{labels['call']}</span></a><a href="https://wa.me/394341801744" target="_blank" rel="noopener"><span>◉</span><span>WhatsApp</span></a></nav>
  <script src="{depth}service.js"></script>
</body>
</html>
'''


def json_string(value):
    import json
    return json.dumps(value, ensure_ascii=False)


for slug in SERVICES:
    italian_dir = ROOT / slug
    english_dir = ROOT / "en" / slug
    italian_dir.mkdir(parents=True, exist_ok=True)
    english_dir.mkdir(parents=True, exist_ok=True)
    (italian_dir / "index.html").write_text(service_page(slug, "it"), encoding="utf-8")
    (english_dir / "index.html").write_text(service_page(slug, "en"), encoding="utf-8")

HOME_EN = {
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
    "service.rentalCopy": "Flexible mobility for individuals and businesses.", "service.salesCopy": "Direct support when choosing your vehicle.",
    "service.transportCopy": "Organised solutions for professionals and businesses.", "service.roadsideCopy": "A direct contact when your journey stops.",
    "service.workshopCopy": "Inspections, maintenance and service.", "service.partsCopy": "Parts and components for your vehicle.",
    "service.tyresCopy": "Tyres, grip and control on the road.",
    "process.kicker": "HOW IT WORKS", "process.title": "Simple. Direct. Newton.",
    "process.intro": "From your first request to the solution, you always have a clear and immediate point of contact.",
    "process.oneTitle": "Choose a service", "process.oneCopy": "Open its dedicated page and see how we can help.",
    "process.twoTitle": "Contact us", "process.twoCopy": "Call or message us on WhatsApp and tell us what you need.",
    "process.threeTitle": "Get assistance", "process.threeCopy": "We give you clear information about the most suitable service.",
    "about.kicker": "NEWTON AUTOSERVICE", "about.title": "One complete answer for your mobility.",
    "about.copy": "Newton brings automotive and transport services together at one trusted location in Pravisdomini. A simple point of contact, coordinated solutions and genuine attention to your needs.",
    "about.one": "Services for individuals, professionals and businesses", "about.two": "Clear, direct assistance",
    "about.three": "Seven areas of expertise, one partner", "about.link": "Contact Newton",
    "faq.kicker": "FREQUENTLY ASKED QUESTIONS", "faq.title": "Useful information", "faq.intro": "Quick answers before you contact us.",
    "faq.oneQ": "Which services does Newton offer?", "faq.oneA": "Rental, vehicle sales, freight transport, roadside assistance, workshop, spare parts and tyre service.",
    "faq.twoQ": "How can I request information?", "faq.twoA": "Call our primary number or message us directly on WhatsApp.",
    "faq.threeQ": "Where are you located?", "faq.threeA": "We are at Via Isonzo 65, 33076 Pravisdomini (PN), Italy.",
    "contact.kicker": "CONTACT", "contact.title": "Let’s talk about what you need.",
    "contact.copy": "Call us, message us on WhatsApp or email us, or visit us in Pravisdomini.",
    "contact.addressLabel": "ADDRESS", "contact.primary": "PRIMARY NUMBER & WHATSAPP", "contact.info": "INFORMATION", "contact.email": "EMAIL",
    "contact.whatsapp": "Message us on WhatsApp", "contact.call": "Call now", "contact.directions": "Get directions",
    "footer.copy": "Automotive and transport services in Pravisdomini.",
}


def generate_english_home():
    from lxml import html, etree

    source = (ROOT / "index.html").read_text(encoding="utf-8")
    document = html.document_fromstring(source)
    document.set("lang", "en")
    document.xpath("//title")[0].text = "Newton Autoservice | Automotive services in Pravisdomini"
    description = "Newton Autoservice in Pravisdomini: rental, vehicle sales, freight transport, roadside assistance, workshop, spare parts and tyre service."
    document.xpath('//meta[@name="description"]')[0].set("content", description)
    document.xpath('//meta[@property="og:title"]')[0].set("content", "Newton Autoservice | Automotive services in Pravisdomini")
    document.xpath('//meta[@property="og:description"]')[0].set("content", description)
    document.xpath('//meta[@property="og:url"]')[0].set("content", "https://newtonvts.it/en/")
    document.xpath('//meta[@property="og:locale"]')[0].set("content", "en_GB")
    document.xpath('//link[@rel="canonical"]')[0].set("href", "https://newtonvts.it/en/")

    for node in document.xpath('//*[@data-i18n]'):
        value = HOME_EN.get(node.get("data-i18n"))
        if value:
            node.text = value

    for node in document.xpath('//link[@rel="stylesheet"] | //link[@rel="icon"] | //script[@src] | //img[@src]'):
        attr = "src" if node.tag in ("script", "img") else "href"
        value = node.get(attr)
        if value and not value.startswith(("http:", "https:", "/", "../")):
            node.set(attr, "../" + value)

    switches = document.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " language-switch ")]/a')
    switches[0].set("href", "../")
    switches[0].set("class", "")
    switches[1].set("href", "./")
    switches[1].set("class", "active")

    output_dir = ROOT / "en"
    output_dir.mkdir(exist_ok=True)
    output = "<!doctype html>\n" + etree.tostring(document, method="html", encoding="unicode", pretty_print=True)
    (output_dir / "index.html").write_text(output, encoding="utf-8")


generate_english_home()
print("Generated", len(SERVICES) * 2, "static service pages and the English homepage")
