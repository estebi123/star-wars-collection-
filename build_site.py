import json
prods=json.load(open('products.json'))
DATA=json.dumps(prods,separators=(',',':'))
CONTACT={"telegram":"estebi1234","email":""}
CJSON=json.dumps(CONTACT)
html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Cantina Collectibles · San Juan, PR</title>
<style>
:root{--bg:#0d0f14;--card:#161a22;--line:#262c38;--txt:#e9edf4;--mut:#9aa4b5;--acc:#ffd34d;--tg:#2aabee}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--txt);font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
header{padding:22px 16px 8px;text-align:center;border-bottom:1px solid var(--line)}
h1{margin:0;font-size:22px;letter-spacing:.5px}
.sub{color:var(--mut);font-size:13px;margin-top:4px}
.wrap{max-width:1100px;margin:0 auto;padding:14px}
.controls{display:flex;flex-direction:column;gap:10px;margin-bottom:8px}
input[type=search]{width:100%;padding:11px 13px;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--txt);font-size:15px}
select{padding:9px 11px;border-radius:9px;border:1px solid var(--line);background:var(--card);color:var(--txt);font-size:14px}
.row{display:flex;flex-wrap:wrap;gap:7px;align-items:center}
.lbl{color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.6px;margin-right:2px;width:100%;margin-bottom:-2px}
.chip{padding:6px 12px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--mut);font-size:13px;cursor:pointer;user-select:none}
.chip.on{background:var(--acc);color:#1a1a1a;border-color:var(--acc);font-weight:600}
.count{color:var(--mut);font-size:13px;margin:10px 2px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}
.ph{position:relative;background:#0a0c10;aspect-ratio:1/1;cursor:zoom-in;overflow:hidden}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.badge{position:absolute;top:8px;left:8px;background:rgba(0,0,0,.66);color:#fff;font-size:11px;padding:3px 7px;border-radius:6px}
.more{position:absolute;bottom:8px;right:8px;background:rgba(0,0,0,.66);color:#fff;font-size:11px;padding:3px 7px;border-radius:6px}
.body{padding:11px 12px 13px;display:flex;flex-direction:column;gap:5px;flex:1}
.nm{font-size:15px;font-weight:600;line-height:1.25}
.ln{color:var(--mut);font-size:12.5px}
.cond{color:var(--mut);font-size:12px}
.pr{font-size:18px;font-weight:700;color:var(--acc);margin-top:2px}
.obo{font-size:11px;color:var(--mut);font-weight:600}
.btns{display:flex;gap:8px;margin-top:8px}
.btn{flex:1;text-align:center;text-decoration:none;padding:9px;border-radius:9px;font-size:13.5px;font-weight:600}
.tg{background:var(--tg);color:#fff}
.em{background:#2a3140;color:var(--txt)}
.iid{color:var(--mut);font-size:11px;margin-top:6px}
footer{color:var(--mut);font-size:12px;text-align:center;padding:22px}
.lb{position:fixed;inset:0;background:rgba(0,0,0,.92);display:none;align-items:center;justify-content:center;flex-direction:column;z-index:50}
.lb.on{display:flex}
.lb img{max-width:94vw;max-height:80vh;object-fit:contain}
.lb .x{position:absolute;top:14px;right:18px;color:#fff;font-size:30px;cursor:pointer}
.lb .nav{display:flex;gap:24px;margin-top:14px}
.lb .nav span{color:#fff;font-size:30px;cursor:pointer;padding:6px 16px;background:rgba(255,255,255,.1);border-radius:10px}
.empty{color:var(--mut);text-align:center;padding:40px}
</style>
</head>
<body>
<header>
<h1>Cantina Collectibles</h1>
<div class="sub">Star Wars collection · San Juan, PR · message to buy</div>
</header>
<div class="wrap">
<div class="controls">
<input id="q" type="search" placeholder="Search name, line, year..."/>
<div class="row">
<span class="lbl">Sort</span>
<select id="sort">
<option value="featured">Featured</option>
<option value="price-asc">Price: Low &rarr; High</option>
<option value="price-desc">Price: High &rarr; Low</option>
<option value="name-asc">Name: A &rarr; Z</option>
<option value="name-desc">Name: Z &rarr; A</option>
</select>
</div>
<div class="row" id="cats"><span class="lbl">Type</span></div>
<div class="row" id="eps"><span class="lbl">Movie / Episode</span></div>
</div>
<div class="count" id="count"></div>
<div class="grid" id="grid"></div>
</div>
<footer>Message to buy &mdash; mention the item #.</footer>
<div class="lb" id="lb"><span class="x" onclick="closeLb()">&times;</span><img id="lbimg" src=""/><div class="nav"><span onclick="lbStep(-1)">&#8249;</span><span onclick="lbStep(1)">&#8250;</span></div></div>
<script>
const PRODUCTS = __DATA__;
const CONTACT = __CONTACT__;
const EPORDER={"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"Saga":9};
let state={q:"",cat:"All",ep:"All",sort:"featured"};
let lb={photos:[],i:0};
function epLabel(e){return e==="Saga"?"Saga":"Episode "+e;}
function uniq(key){return [...new Set(PRODUCTS.map(p=>p[key]))];}
function buildChips(containerId,values,stateKey,labelFn){
  const c=document.getElementById(containerId);
  const all=["All",...values];
  all.forEach(v=>{
    const el=document.createElement("span");
    el.className="chip"+(state[stateKey]===v?" on":"");
    el.textContent=v==="All"?"All":labelFn(v);
    el.onclick=()=>{state[stateKey]=v;[...c.querySelectorAll(".chip")].forEach(x=>x.classList.remove("on"));el.classList.add("on");render();};
    c.appendChild(el);
  });
}
function priceText(p){
  if(p.price==null) return {big:"Make offer",obo:""};
  return {big:"$"+p.price, obo:p.offer?"or best offer":""};
}
function render(){
  let list=PRODUCTS.filter(p=>{
    if(state.cat!=="All" && p.cat!==state.cat) return false;
    if(state.ep!=="All" && p.ep!==state.ep) return false;
    if(state.q){const t=(p.name+" "+p.line+" "+p.year).toLowerCase();if(!t.includes(state.q.toLowerCase())) return false;}
    return true;
  });
  const s=state.sort;
  const pv=p=>p.price==null?Infinity:p.price;
  if(s==="price-asc") list.sort((a,b)=>pv(a)-pv(b)||a.id.localeCompare(b.id));
  else if(s==="price-desc") list.sort((a,b)=>{if(a.price==null&&b.price!=null)return 1;if(b.price==null&&a.price!=null)return -1;return pv(b)-pv(a)||a.id.localeCompare(b.id);});
  else if(s==="name-asc") list.sort((a,b)=>a.name.localeCompare(b.name));
  else if(s==="name-desc") list.sort((a,b)=>b.name.localeCompare(a.name));
  else list.sort((a,b)=>a.id.localeCompare(b.id));
  document.getElementById("count").textContent=list.length+" item"+(list.length!==1?"s":"");
  const g=document.getElementById("grid");g.innerHTML="";
  if(!list.length){g.innerHTML='<div class="empty">No items match.</div>';return;}
  list.forEach(p=>{
    const pt=priceText(p);
    const card=document.createElement("div");card.className="card";
    const photosAttr=encodeURIComponent(JSON.stringify(p.photos));
    let buy="";
    if(CONTACT.telegram) buy+=`<a class="btn tg" href="https://t.me/${CONTACT.telegram}" target="_blank" rel="noopener">Message on Telegram</a>`;
    if(CONTACT.email){const subj=encodeURIComponent("Star Wars item #"+p.id+" - "+p.name);buy+=`<a class="btn em" href="mailto:${CONTACT.email}?subject=${subj}">Email</a>`;}
    card.innerHTML=`
      <div class="ph" data-ph="${photosAttr}" onclick="openLb(this)">
        <img src="${p.photos[0]}" loading="lazy" alt="${p.name}"/>
        <span class="badge">#${p.id} &middot; ${epLabel(p.ep)}</span>
        ${p.photos.length>1?`<span class="more">+${p.photos.length-1} photo${p.photos.length>2?"s":""}</span>`:""}
      </div>
      <div class="body">
        <div class="nm">${p.name}</div>
        <div class="ln">${p.line} &middot; ${p.year}</div>
        <div class="cond">${p.cond}</div>
        <div class="pr">${pt.big} ${pt.obo?`<span class="obo">${pt.obo}</span>`:""}</div>
        <div class="btns">${buy}</div>
        <div class="iid">Item #${p.id} &mdash; mention this when you message</div>
      </div>`;
    g.appendChild(card);
  });
}
function openLb(el){lb.photos=JSON.parse(decodeURIComponent(el.getAttribute("data-ph")));lb.i=0;document.getElementById("lbimg").src=lb.photos[0];document.getElementById("lb").classList.add("on");}
function closeLb(){document.getElementById("lb").classList.remove("on");}
function lbStep(d){lb.i=(lb.i+d+lb.photos.length)%lb.photos.length;document.getElementById("lbimg").src=lb.photos[lb.i];}
document.getElementById("lb").addEventListener("click",e=>{if(e.target.id==="lb")closeLb();});
document.getElementById("q").addEventListener("input",e=>{state.q=e.target.value;render();});
document.getElementById("sort").addEventListener("change",e=>{state.sort=e.target.value;render();});
const cats=uniq("cat").sort();
const eps=uniq("ep").sort((a,b)=>(EPORDER[a]||50)-(EPORDER[b]||50));
buildChips("cats",cats,"cat",v=>v);
buildChips("eps",eps,"ep",epLabel);
render();
</script>
</body>
</html>'''
html=html.replace("__DATA__",DATA).replace("__CONTACT__",CJSON)
open('index.html','w').write(html)
import os
print("written:",len(prods),"items |",round(os.path.getsize('index.html')/1024/1024,2),"MB")
