import json
prods=json.load(open('products.json'))
DATA=json.dumps(prods,separators=(',',':'))
CONTACT={"telegram":"estebi1234","email":""}
CJSON=json.dumps(CONTACT)
N=len(prods)
SITE="https://estebi123.github.io/star-wars-collection-/"
DESC="Colección Star Wars en venta · San Juan, Puerto Rico · %d piezas: figuras, vehículos, sets coleccionables y más."%N
META=('<meta name="description" content="'+DESC+'"/>\n'
 '<meta property="og:title" content="Cantina Collectibles — Colección Star Wars"/>\n'
 '<meta property="og:description" content="'+DESC+'"/>\n'
 '<meta property="og:type" content="website"/>\n'
 '<meta property="og:url" content="'+SITE+'"/>\n'
 '<meta property="og:image" content="'+SITE+'img/001-1.jpg"/>\n'
 '<meta name="twitter:card" content="summary_large_image"/>\n'
 '<meta name="twitter:title" content="Cantina Collectibles — Colección Star Wars"/>\n'
 '<meta name="twitter:description" content="'+DESC+'"/>\n'
 '<meta name="twitter:image" content="'+SITE+'img/001-1.jpg"/>\n')

COND_ES={
"Appears sealed · light shelf wear":"Aparenta sellado · leve desgaste de estante",
"Boxed (clamshell) · near mint":"En caja (clamshell) · casi perfecto",
"Boxed daily calendar · light box wear":"Calendario diario en caja · leve desgaste de caja",
"Boxed daily calendar · opened, box edge wear":"Calendario diario en caja · abierto, desgaste en bordes de caja",
"Boxed tin · box wear, figures sealed in tin":"Lata en caja · desgaste de caja, figuras selladas en la lata",
"Boxed · box creasing & window scuffs":"En caja · pliegues en caja y roces en la ventana",
"Boxed · box creasing & window wear":"En caja · pliegues en caja y desgaste de ventana",
"Boxed · box edge & corner wear, light shelf wear":"En caja · desgaste en bordes y esquinas, leve desgaste de estante",
"Boxed · box wear, bubble intact":"En caja · desgaste de caja, burbuja intacta",
"Boxed · box wear, case yellowing":"En caja · desgaste de caja, estuche amarillento",
"Boxed · box wear, figures sealed":"En caja · desgaste de caja, figuras selladas",
"Boxed · box wear, tape on flaps":"En caja · desgaste de caja, cinta en las solapas",
"Boxed · box wear, window crease":"En caja · desgaste de caja, pliegue en la ventana",
"Boxed · box wear/creasing":"En caja · desgaste/pliegues en la caja",
"Boxed · box wear/creasing, figure sealed":"En caja · desgaste/pliegues en la caja, figura sellada",
"Boxed · box wear/creasing, top plastic crack":"En caja · desgaste/pliegues en la caja, grieta en plástico superior",
"Boxed · box worn/creased":"En caja · caja desgastada/con pliegues",
"Boxed · box worn/creased, figure sealed":"En caja · caja desgastada/con pliegues, figura sellada",
"Boxed · old store clearance sticker, box wear":"En caja · etiqueta vieja de liquidación, desgaste de caja",
"Boxed · window & box wear, light dust":"En caja · desgaste de ventana y caja, polvo leve",
"Built loose · complete as shown, no box":"Armado suelto · completo según fotos, sin caja",
"Carded (MOC) · CommTech chip, card edge wear":"En blíster (MOC) · chip CommTech, desgaste en bordes del cartón",
"Carded (MOC) · blue variant, card edge wear":"En blíster (MOC) · variante azul, desgaste en bordes del cartón",
"Carded (MOC) · card edge & corner wear":"En blíster (MOC) · desgaste en bordes y esquinas del cartón",
"Carded (MOC) · card edge & corner wear, bubble intact":"En blíster (MOC) · desgaste en bordes y esquinas del cartón, burbuja intacta",
"Carded (MOC) · card edge & corner wear, light shelf wear":"En blíster (MOC) · desgaste en bordes y esquinas del cartón, leve desgaste de estante",
"Carded (MOC) · card edge wear":"En blíster (MOC) · desgaste en bordes del cartón",
"Carded (MOC) · card edge wear, bubble intact":"En blíster (MOC) · desgaste en bordes del cartón, burbuja intacta",
"Carded (MOC) · card edge wear, light dust":"En blíster (MOC) · desgaste en bordes del cartón, polvo leve",
"Carded (MOC) · light shelf wear":"En blíster (MOC) · leve desgaste de estante",
"Carded (MOC) · red variant, card edge wear":"En blíster (MOC) · variante roja, desgaste en bordes del cartón",
"Carded (MOSC) · light shelf wear":"En blíster (MOSC) · leve desgaste de estante",
"Carded 2-pack (MOC) · card edge wear":"Blíster doble (MOC) · desgaste en bordes del cartón",
"Carded in protective case · near mint":"En blíster con estuche protector · casi perfecto",
"Carded watch · front & back shown, clamshell wear, old price sticker":"Reloj en blíster · frente y dorso en fotos, desgaste del clamshell, etiqueta vieja de precio",
"Carded · Disney Star Tours exclusive, card edge wear":"En blíster · exclusivo Disney Star Tours, desgaste en bordes del cartón",
"Carded · card edge wear":"En blíster · desgaste en bordes del cartón",
"Carded · card edge wear & creasing":"En blíster · desgaste y pliegues en bordes del cartón",
"Carded · card edge wear, light dust":"En blíster · desgaste en bordes del cartón, polvo leve",
"Carded · card wear, light dust":"En blíster · desgaste del cartón, polvo leve",
"Factory sealed · shrink intact":"Sellado de fábrica · termoencogido intacto",
"Loose (no packaging) · played-with, see photos":"Suelto (sin empaque) · usado, ver fotos",
"Loose cards · played, see photo":"Cartas sueltas · usadas, ver foto",
"New in box · chrome finish":"Nuevo en caja · acabado cromado",
"New in box · minor edge & corner wear, light dust on case":"Nuevo en caja · leve desgaste en bordes y esquinas, polvo leve en el estuche",
"New in box · minor edge wear & light dust":"Nuevo en caja · leve desgaste en bordes y polvo leve",
"New in box · minor edge wear, light dust":"Nuevo en caja · leve desgaste en bordes, polvo leve",
"Plush · light wear, manufacturer tag attached":"Peluche · desgaste leve, etiqueta del fabricante puesta",
"Reading copy · cover & spine wear":"Copia de lectura · desgaste en portada y lomo",
"Sealed tin · outer box shows shelf wear":"Lata sellada · caja exterior con desgaste de estante",
"Used promo crowns · light wear/creasing":"Coronas promocionales usadas · desgaste/pliegues leves",
}
CONDES=json.dumps(COND_ES)

STYLE=":root{--bg:#0d0f14;--card:#161a22;--line:#262c38;--txt:#e9edf4;--mut:#9aa4b5;--acc:#ffd34d;--tg:#2aabee}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--txt);font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}header{position:relative;padding:22px 16px 8px;text-align:center;border-bottom:1px solid var(--line)}h1{margin:0;font-size:22px;letter-spacing:.5px}.sub{color:var(--mut);font-size:13px;margin-top:4px}.langsw{position:absolute;top:12px;right:14px;display:flex;gap:5px}.lc{cursor:pointer;font-size:12px;font-weight:700;color:var(--mut);padding:4px 9px;border:1px solid var(--line);border-radius:999px;user-select:none}.lc.on{background:var(--acc);color:#1a1a1a;border-color:var(--acc)}.wrap{max-width:1100px;margin:0 auto;padding:14px}.controls{display:flex;flex-direction:column;gap:10px;margin-bottom:8px}input[type=search]{width:100%;padding:11px 13px;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--txt);font-size:15px}select{padding:9px 11px;border-radius:9px;border:1px solid var(--line);background:var(--card);color:var(--txt);font-size:14px}.row{display:flex;flex-wrap:wrap;gap:7px;align-items:center}.lbl{color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.6px;margin-right:2px;width:100%;margin-bottom:-2px}.chip{padding:6px 12px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--mut);font-size:13px;cursor:pointer;user-select:none}.chip.on{background:var(--acc);color:#1a1a1a;border-color:var(--acc);font-weight:600}.count{color:var(--mut);font-size:13px;margin:10px 2px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}.ph{position:relative;background:#0a0c10;aspect-ratio:1/1;cursor:zoom-in;overflow:hidden}.ph img{width:100%;height:100%;object-fit:cover;display:block}.badge{position:absolute;top:8px;left:8px;background:rgba(0,0,0,.66);color:#fff;font-size:11px;padding:3px 7px;border-radius:6px}.more{position:absolute;bottom:8px;right:8px;background:rgba(0,0,0,.66);color:#fff;font-size:11px;padding:3px 7px;border-radius:6px}.body{padding:11px 12px 13px;display:flex;flex-direction:column;gap:5px;flex:1}.nm{font-size:15px;font-weight:600;line-height:1.25}.ln{color:var(--mut);font-size:12.5px}.cond{color:var(--mut);font-size:12px}.pr{font-size:18px;font-weight:700;color:var(--acc);margin-top:2px}.obo{font-size:11px;color:var(--mut);font-weight:600}.btns{display:flex;gap:8px;margin-top:8px}.btn{flex:1;text-align:center;text-decoration:none;padding:9px;border-radius:9px;font-size:13.5px;font-weight:600}.tg{background:var(--tg);color:#fff}.em{background:#2a3140;color:var(--txt)}.iid{color:var(--mut);font-size:11px;margin-top:6px}footer{color:var(--mut);font-size:12px;text-align:center;padding:22px}.lb{position:fixed;inset:0;background:rgba(0,0,0,.92);display:none;align-items:center;justify-content:center;flex-direction:column;z-index:50}.lb.on{display:flex}.lb img{max-width:94vw;max-height:80vh;object-fit:contain}.lb .x{position:absolute;top:14px;right:18px;color:#fff;font-size:30px;cursor:pointer}.lb .nav{display:flex;gap:24px;margin-top:14px}.lb .nav span{color:#fff;font-size:30px;cursor:pointer;padding:6px 16px;background:rgba(255,255,255,.1);border-radius:10px}.empty{color:var(--mut);text-align:center;padding:40px}.share{display:flex;flex-wrap:wrap;gap:7px;justify-content:center;align-items:center;margin-top:10px}.shlbl{color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.6px}.shbtn{font-size:12.5px;font-weight:600;padding:6px 12px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--txt);cursor:pointer;text-decoration:none;display:inline-block;line-height:1.1}.shbtn.wa{background:#25d366;color:#06310f;border-color:#25d366}.shbtn.tg2{background:var(--tg);color:#fff;border-color:var(--tg)}.shbtn.fb{background:#1877f2;color:#fff;border-color:#1877f2}button.btn{font-family:inherit;border:none;cursor:pointer}.card.sold .ph img{filter:grayscale(1);opacity:.55}.soldrib{position:absolute;top:8px;right:8px;background:#c0392b;color:#fff;font-size:11px;font-weight:700;padding:3px 8px;border-radius:6px;letter-spacing:.5px}.soldbtn{flex:1;text-align:center;padding:9px;border-radius:9px;font-size:13.5px;font-weight:700;background:#3a2327;color:#e8a0a0;cursor:default}.lnk{cursor:pointer;color:var(--tg);text-decoration:underline}.card.hl{outline:2px solid var(--acc);outline-offset:2px;box-shadow:0 0 0 5px rgba(255,211,77,.25)}.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%) translateY(20px);background:#222a36;color:#fff;padding:10px 16px;border-radius:10px;font-size:13px;opacity:0;pointer-events:none;transition:.25s;z-index:60;border:1px solid var(--line);max-width:90vw;text-align:center}.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}"

SCRIPT=r"""
const PRODUCTS = __DATA__;
const CONTACT = __CONTACT__;
const COND_ES = __CONDES__;
const EPORDER={"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"Saga":9};
const I18N={
 es:{sub:"Colección Star Wars · San Juan, PR · escríbeme para comprar",search:"Buscar nombre, línea, año...",sort:"Ordenar",featured:"Destacados",plh:"Precio: menor → mayor",phl:"Precio: mayor → menor",naz:"Nombre: A → Z",nza:"Nombre: Z → A",type:"Tipo",movie:"Película / Episodio",all:"Todos",items:"artículos",item:"artículo",makeoffer:"Haz una oferta",obo:"o mejor oferta",tg:"Escríbeme por Telegram",email:"Correo",photo:"foto",photos:"fotos",iida:"Artículo #",iidb:" — menciónalo al escribir",footer:"Escríbeme para comprar — menciona el # del artículo.",none:"No hay artículos que coincidan.",share:"Compartir",copy:"Copiar enlace",copied:"¡Copiado!",sharemsg:"Mira esta colección de Star Wars en venta en San Juan, PR:",sold:"Vendido",tgmsg:"Hola, me interesa el #{id} — {name} ({price})",tgtoast:"Mensaje copiado — pégalo en Telegram",linktoast:"Enlace de la pieza copiado",copylink2:"🔗 enlace",ep:"Episodio "},
 en:{sub:"Star Wars collection · San Juan, PR · message to buy",search:"Search name, line, year...",sort:"Sort",featured:"Featured",plh:"Price: Low → High",phl:"Price: High → Low",naz:"Name: A → Z",nza:"Name: Z → A",type:"Type",movie:"Movie / Episode",all:"All",items:"items",item:"item",makeoffer:"Make offer",obo:"or best offer",tg:"Message on Telegram",email:"Email",photo:"photo",photos:"photos",iida:"Item #",iidb:" — mention this when you message",footer:"Message to buy — mention the item #.",none:"No items match.",share:"Share",copy:"Copy link",copied:"Copied!",sharemsg:"Check out this Star Wars collection for sale in San Juan, PR:",sold:"Sold",tgmsg:"Hi, I'm interested in #{id} — {name} ({price})",tgtoast:"Message copied — paste it in Telegram",linktoast:"Item link copied",copylink2:"🔗 link",ep:"Episode "}
};
const CAT={Figures:{es:"Figuras",en:"Figures"},Vehicles:{es:"Vehículos",en:"Vehicles"},Games:{es:"Juegos",en:"Games"},Oddities:{es:"Curiosidades",en:"Oddities"},Print:{es:"Impresos",en:"Print"}};
let lang=(function(){try{return localStorage.getItem('lang')||'es'}catch(e){return 'es'}})();
let state={q:"",cat:"All",ep:"All",sort:"featured"};
let lb={photos:[],i:0};
function T(){return I18N[lang];}
function epLabel(e){return e==="Saga"?"Saga":T().ep+e;}
function catLabel(c){return CAT[c]?CAT[c][lang]:c;}
function condText(p){return lang==='es'?(COND_ES[p.cond]||p.cond):p.cond;}
function uniq(key){return [...new Set(PRODUCTS.map(p=>p[key]))];}
function chipClear(id){const c=document.getElementById(id);[...c.querySelectorAll(".chip")].forEach(x=>x.remove());}
function addChips(containerId,values,stateKey,labelFn){
  const c=document.getElementById(containerId);
  const all=["All",...values];
  all.forEach(v=>{
    const el=document.createElement("span");
    el.className="chip"+(state[stateKey]===v?" on":"");
    el.textContent=v==="All"?T().all:labelFn(v);
    el.onclick=()=>{state[stateKey]=v;[...c.querySelectorAll(".chip")].forEach(x=>x.classList.remove("on"));el.classList.add("on");render();};
    c.appendChild(el);
  });
}
function rebuildChips(){chipClear("cats");chipClear("eps");addChips("cats",cats,"cat",catLabel);addChips("eps",eps,"ep",epLabel);}
function priceText(p){if(p.price==null) return {big:T().makeoffer,obo:""};return {big:"$"+p.price, obo:p.offer?T().obo:""};}
function render(){
  const t=T();
  let list=PRODUCTS.filter(p=>{
    if(state.cat!=="All" && p.cat!==state.cat) return false;
    if(state.ep!=="All" && p.ep!==state.ep) return false;
    if(state.q){const tx=(p.name+" "+p.line+" "+p.year).toLowerCase();if(!tx.includes(state.q.toLowerCase())) return false;}
    return true;
  });
  const s=state.sort;
  const pv=p=>p.price==null?Infinity:p.price;
  if(s==="price-asc") list.sort((a,b)=>pv(a)-pv(b)||a.id.localeCompare(b.id));
  else if(s==="price-desc") list.sort((a,b)=>{if(a.price==null&&b.price!=null)return 1;if(b.price==null&&a.price!=null)return -1;return pv(b)-pv(a)||a.id.localeCompare(b.id);});
  else if(s==="name-asc") list.sort((a,b)=>a.name.localeCompare(b.name));
  else if(s==="name-desc") list.sort((a,b)=>b.name.localeCompare(a.name));
  else list.sort((a,b)=>a.id.localeCompare(b.id));
  list=list.filter(function(p){return !p.sold;}).concat(list.filter(function(p){return p.sold;}));
  document.getElementById("count").textContent=list.length+" "+(list.length!==1?t.items:t.item);
  const g=document.getElementById("grid");g.innerHTML="";
  if(!list.length){g.innerHTML='<div class="empty">'+t.none+'</div>';return;}
  list.forEach(p=>{
    const pt=priceText(p);
    const card=document.createElement("div");card.className="card"+(p.sold?" sold":"");card.id="item-"+p.id;
    const photosAttr=encodeURIComponent(JSON.stringify(p.photos));
    let buy="";
    if(p.sold){buy='<span class="soldbtn">'+t.sold+'</span>';}
    else{
    if(CONTACT.telegram) buy+='<button class="btn tg buy" data-id="'+p.id+'">'+t.tg+'</button>';
    if(CONTACT.email){const subj=encodeURIComponent("Star Wars item #"+p.id+" - "+p.name);buy+='<a class="btn em" href="mailto:'+CONTACT.email+'?subject='+subj+'">'+t.email+'</a>';}
    }
    const extra=p.photos.length-1;
    const moreTxt=extra>0?("+"+extra+" "+(extra>1?t.photos:t.photo)):"";
    card.innerHTML='<div class="ph" data-ph="'+photosAttr+'" onclick="openLb(this)"><img src="'+p.photos[0]+'" loading="lazy" alt="'+p.name+'"/><span class="badge">#'+p.id+' &middot; '+epLabel(p.ep)+'</span>'+(extra>0?'<span class="more">'+moreTxt+'</span>':'')+(p.sold?'<span class="soldrib">'+t.sold+'</span>':'')+'</div><div class="body"><div class="nm">'+p.name+'</div><div class="ln">'+p.line+' &middot; '+p.year+'</div><div class="cond">'+condText(p)+'</div><div class="pr">'+pt.big+' '+(pt.obo?'<span class="obo">'+pt.obo+'</span>':'')+'</div><div class="btns">'+buy+'</div><div class="iid">'+t.iida+p.id+t.iidb+' · <span class="lnk" data-id="'+p.id+'">'+t.copylink2+'</span></div></div>';
    g.appendChild(card);
  });
}
function applyLang(){
  const t=T();
  document.documentElement.lang=lang;
  document.getElementById("subt").textContent=t.sub;
  document.getElementById("q").placeholder=t.search;
  document.getElementById("l-sort").textContent=t.sort;
  document.getElementById("l-type").textContent=t.type;
  document.getElementById("l-movie").textContent=t.movie;
  const so=document.getElementById("sort").options;
  so[0].textContent=t.featured;so[1].textContent=t.plh;so[2].textContent=t.phl;so[3].textContent=t.naz;so[4].textContent=t.nza;
  document.getElementById("foot").textContent=t.footer;
  document.getElementById("lang-es").classList.toggle("on",lang==="es");
  document.getElementById("lang-en").classList.toggle("on",lang==="en");
  document.getElementById("sh-lbl").textContent=t.share;document.getElementById("sh-cp").textContent=t.copy;setupShare();rebuildChips();render();
}
function setupShare(){var u=location.origin+location.pathname;var t=T();var m=t.sharemsg+" "+u;document.getElementById("sh-wa").href="https://wa.me/?text="+encodeURIComponent(m);document.getElementById("sh-tg").href="https://t.me/share/url?url="+encodeURIComponent(u)+"&text="+encodeURIComponent(t.sharemsg);document.getElementById("sh-fb").href="https://www.facebook.com/sharer/sharer.php?u="+encodeURIComponent(u);}
function copyLink(){var u=location.origin+location.pathname;navigator.clipboard.writeText(u).then(function(){var b=document.getElementById("sh-cp");b.textContent=T().copied;setTimeout(function(){b.textContent=T().copy;},1500);});}
function contactTG(id){var p=PRODUCTS.find(function(x){return x.id===id;});if(!p)return;var t=T();var price=(p.price==null)?t.makeoffer:("$"+p.price);var msg=t.tgmsg.replace("{id}",p.id).replace("{name}",p.name).replace("{price}",price);if(navigator.clipboard){navigator.clipboard.writeText(msg).catch(function(){});}showToast(t.tgtoast);if(CONTACT.telegram){window.open("https://t.me/"+CONTACT.telegram,"_blank","noopener");}}
function copyItemLink(id){var u=location.origin+location.pathname+"#"+id;if(navigator.clipboard){navigator.clipboard.writeText(u).catch(function(){});}showToast(T().linktoast);}
function showToast(m){var el=document.getElementById("toast");if(!el)return;el.textContent=m;el.classList.add("on");clearTimeout(window._tt);window._tt=setTimeout(function(){el.classList.remove("on");},2200);}
function handleHash(){var h=(location.hash||"").replace("#","");if(!h)return;var el=document.getElementById("item-"+h);if(el){el.scrollIntoView({behavior:"smooth",block:"center"});el.classList.add("hl");setTimeout(function(){el.classList.remove("hl");},2600);}}
function setLang(l){lang=l;try{localStorage.setItem('lang',l)}catch(e){}applyLang();}
function openLb(el){lb.photos=JSON.parse(decodeURIComponent(el.getAttribute("data-ph")));lb.i=0;document.getElementById("lbimg").src=lb.photos[0];document.getElementById("lb").classList.add("on");}
function closeLb(){document.getElementById("lb").classList.remove("on");}
function lbStep(d){lb.i=(lb.i+d+lb.photos.length)%lb.photos.length;document.getElementById("lbimg").src=lb.photos[lb.i];}
document.getElementById("lb").addEventListener("click",e=>{if(e.target.id==="lb")closeLb();});
document.getElementById("q").addEventListener("input",e=>{state.q=e.target.value;render();});
document.getElementById("sort").addEventListener("change",e=>{state.sort=e.target.value;render();});
document.getElementById("grid").addEventListener("click",function(e){var b=e.target.closest(".buy");if(b){contactTG(b.getAttribute("data-id"));return;}var l=e.target.closest(".lnk");if(l){copyItemLink(l.getAttribute("data-id"));return;}});
window.addEventListener("hashchange",handleHash);
const cats=uniq("cat").sort();
const eps=uniq("ep").sort((a,b)=>(EPORDER[a]||50)-(EPORDER[b]||50));
applyLang();
setTimeout(handleHash,250);
"""

FAVICON='<link rel="icon" type="image/svg+xml" href="favicon.svg"/>\n'
H=[]
H.append('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="utf-8"/>\n<meta name="viewport" content="width=device-width, initial-scale=1"/>\n')
H.append('<title>Cantina Collectibles · San Juan, PR</title>\n'+FAVICON+META+'<style>'+STYLE+'</style>\n</head>\n<body>\n')
H.append('<header>\n<div class="langsw"><span class="lc" id="lang-es" onclick="setLang(\'es\')">ES</span><span class="lc" id="lang-en" onclick="setLang(\'en\')">EN</span></div>\n')
H.append('<h1>Cantina Collectibles</h1>\n<div class="sub" id="subt"></div>\n<div class="share" id="share"><span class="shlbl" id="sh-lbl"></span><a class="shbtn wa" id="sh-wa" target="_blank" rel="noopener">WhatsApp</a><a class="shbtn tg2" id="sh-tg" target="_blank" rel="noopener">Telegram</a><a class="shbtn fb" id="sh-fb" target="_blank" rel="noopener">Facebook</a><button class="shbtn cp" id="sh-cp" onclick="copyLink()"></button></div>\n</header>\n')
H.append('<div class="wrap">\n<div class="controls">\n<input id="q" type="search"/>\n')
H.append('<div class="row"><span class="lbl" id="l-sort"></span>\n<select id="sort">\n<option value="featured"></option>\n<option value="price-asc"></option>\n<option value="price-desc"></option>\n<option value="name-asc"></option>\n<option value="name-desc"></option>\n</select>\n</div>\n')
H.append('<div class="row" id="cats"><span class="lbl" id="l-type"></span></div>\n<div class="row" id="eps"><span class="lbl" id="l-movie"></span></div>\n</div>\n')
H.append('<div class="count" id="count"></div>\n<div class="grid" id="grid"></div>\n</div>\n')
H.append('<footer id="foot"></footer>\n')
H.append('<div class="lb" id="lb"><span class="x" onclick="closeLb()">&times;</span><img id="lbimg" src=""/><div class="nav"><span onclick="lbStep(-1)">&#8249;</span><span onclick="lbStep(1)">&#8250;</span></div></div>\n<div class="toast" id="toast"></div>\n')
H.append('<script>'+SCRIPT+'</script>\n</body>\n</html>')
html="".join(H)
html=html.replace("__DATA__",DATA).replace("__CONTACT__",CJSON).replace("__CONDES__",CONDES)
open('index.html','w',encoding='utf-8').write(html)
import os
print("written:",len(prods),"items |",round(os.path.getsize('index.html')/1024/1024,2),"MB")
