
;(async () => {
    const app = document.createElement('div')
    app.id = 'root'
    app.className = "SideBarDesign";
    const side = document.getElementsByClassName("ul.dds__list dds__flex-column dds__pl-0 dds__text-right dds-link-tabs");
    side[0].appendChild(app);
    const src = chrome?.runtime?.getURL('/react/index.js')
    const event = new CustomEvent("pass-text",{text:"hello world"});
    await import(src)
  })()