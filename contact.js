(() => {
  const english = document.documentElement.lang === 'en';
  const words = english
    ? { title: 'Email Newton', app: 'Open email app', gmail: 'Open Gmail', copy: 'Copy email address', copied: 'Address copied', close: 'Close', hint: 'Choose how to write to us. If no email app opens, use Gmail or copy the address.' }
    : { title: 'Scrivi a Newton', app: 'Apri app email', gmail: 'Apri Gmail', copy: 'Copia indirizzo email', copied: 'Indirizzo copiato', close: 'Chiudi', hint: 'Scegli come scriverci. Se non si apre un’app email, usa Gmail o copia l’indirizzo.' };
  const address = 'info@newtonvts.it';
  const dialog = document.createElement('dialog');
  dialog.className = 'email-dialog';
  dialog.setAttribute('aria-labelledby', 'email-dialog-title');
  dialog.innerHTML = `<button type="button" class="email-close" aria-label="${words.close}">×</button><h2 id="email-dialog-title">${words.title}</h2><p>${words.hint}</p><input class="email-address" aria-label="Email" readonly value="${address}"><div class="email-options"><a class="button button-gold email-app">${words.app}</a><a class="button button-outline email-gmail" target="_blank" rel="noopener">${words.gmail}</a><button type="button" class="button button-outline email-copy">${words.copy}</button></div><p class="email-status" role="status"></p>`;
  document.body.append(dialog);
  dialog.querySelector('.email-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  dialog.querySelector('.email-copy').addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(address);
      dialog.querySelector('.email-status').textContent = words.copied;
    } catch {
      const field = dialog.querySelector('.email-address');
      field.focus();
      field.select();
      dialog.querySelector('.email-status').textContent = english ? 'Select and copy the address above.' : 'Seleziona e copia l’indirizzo qui sopra.';
    }
  });
  document.querySelectorAll('a[href^="mailto:"], a[href^="https://mail.google.com/mail/"]').forEach((link) => {
    const original = new URL(link.href);
    const subject = original.searchParams.get('su') || original.searchParams.get('subject') || '';
    const body = original.searchParams.get('body') || '';
    const params = new URLSearchParams({ subject, body });
    const mailto = `mailto:${address}?${params.toString().replaceAll('+', '%20')}`;
    const gmail = new URL('https://mail.google.com/mail/');
    gmail.search = new URLSearchParams({ view: 'cm', fs: '1', to: address, su: subject, body });
    link.href = mailto;
    link.removeAttribute('target');
    link.setAttribute('aria-haspopup', 'dialog');
    link.addEventListener('click', (event) => {
      if (typeof dialog.showModal !== 'function') return;
      event.preventDefault();
      dialog.querySelector('.email-app').href = mailto;
      dialog.querySelector('.email-gmail').href = gmail.href;
      dialog.querySelector('.email-status').textContent = '';
      dialog.showModal();
    });
  });
  const icon = '<svg class="whatsapp-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M20.52 3.48A11.9 11.9 0 0 0 12.05 0C5.45 0 .08 5.37.08 11.97c0 2.11.55 4.17 1.6 5.99L0 24l6.2-1.63a11.98 11.98 0 0 0 5.84 1.49h.01c6.6 0 11.97-5.37 11.97-11.97 0-3.2-1.25-6.2-3.5-8.41ZM12.05 21.84a9.92 9.92 0 0 1-5.06-1.38l-.36-.21-3.68.97.98-3.59-.24-.37a9.92 9.92 0 0 1-1.52-5.29c0-5.49 4.47-9.96 9.97-9.96 2.66 0 5.16 1.04 7.04 2.92a9.9 9.9 0 0 1 2.91 7.05c0 5.49-4.47 9.96-10.04 9.86Zm5.46-7.46c-.3-.15-1.77-.87-2.04-.97-.28-.1-.48-.15-.68.15-.2.3-.77.97-.94 1.17-.18.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.8-1.49-1.78-1.67-2.08-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.68-1.62-.93-2.22-.24-.58-.48-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.49s1.07 2.89 1.22 3.09c.15.2 2.1 3.21 5.09 4.5.71.31 1.26.49 1.69.63.71.22 1.36.19 1.87.11.57-.08 1.77-.72 2.02-1.42.25-.69.25-1.29.17-1.42-.07-.12-.27-.2-.57-.35Z"/></svg>';
  document.querySelectorAll('a[href^="https://wa.me/"]').forEach((link) => {
    const walker = document.createTreeWalker(link, NodeFilter.SHOW_TEXT);
    const nodes = [];
    while (walker.nextNode()) if (walker.currentNode.textContent.includes('◉')) nodes.push(walker.currentNode);
    nodes.forEach((node) => { const span = document.createElement('span'); span.innerHTML = icon; node.replaceWith(span); });
    if (!nodes.length) link.insertAdjacentHTML('afterbegin', icon);
  });
})();
