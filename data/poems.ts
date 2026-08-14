export type Poem = {
  id:string; title:string; author:string; dynasty:string; genre:string; content:string;
  translation:string; authorBio:string; theme:string; emotion:string; imagery:string[];
  devices:string[]; aiHint:string;
};

export const poems: Poem[] = [
 {id:"spring-view",title:"春望",author:"杜甫",dynasty:"唐",genre:"五言律诗",content:"国破山河在，城春草木深。\n感时花溅泪，恨别鸟惊心。\n烽火连三月，家书抵万金。\n白头搔更短，浑欲不胜簪。",translation:"国都虽已残破，但山河依旧存在；春天来到长安城，草木反而长得格外茂盛。感伤时局，看到花也仿佛落泪；怅恨离别，听到鸟鸣也令人心惊。战火持续了很久，一封家书抵得上万金。忧愁使白发越抓越短，简直连簪子都插不住了。",authorBio:"杜甫（712—770），唐代诗人，作品常深切关注社会现实与个人命运，被后世誉为“诗圣”。",theme:"忧国",emotion:"悲愁",imagery:["春","花","鸟","烽火","家书"],devices:["拟人","移情","对偶"],aiHint:"这首诗的悲意并非单靠“国破”表达，而是通过花、鸟、家书等具体意象层层推进。"},
 {id:"quiet-night",title:"静夜思",author:"李白",dynasty:"唐",genre:"五言绝句",content:"床前明月光，疑是地上霜。\n举头望明月，低头思故乡。",translation:"明亮的月光照在床前，好像地上铺了一层白霜。抬起头看着天上的明月，低下头便想起远方的故乡。",authorBio:"李白（701—762），唐代浪漫主义诗人，以想象奇特、语言豪迈著称。",theme:"思乡",emotion:"思乡",imagery:["月","霜","故乡"],devices:["比喻","对偶"],aiHint:"这首诗最动人的地方在于动作极其简单：举头、低头，却把空间从眼前的月光推向了遥远的故乡。"},
 {id:"mountain-walk",title:"山行",author:"杜牧",dynasty:"唐",genre:"七言绝句",content:"远上寒山石径斜，白云生处有人家。\n停车坐爱枫林晚，霜叶红于二月花。",translation:"沿着弯曲的石径登上秋日的山岭，在白云升起的地方隐约有人家。停下车来是因为喜爱傍晚的枫林，经霜的枫叶比二月盛开的春花还要红艳。",authorBio:"杜牧（803—约852），唐代诗人，作品清俊明丽，也长于咏史与写景。",theme:"山水",emotion:"喜悦",imagery:["寒山","白云","人家","枫林","霜叶"],devices:["对比","比喻"],aiHint:"“霜叶红于二月花”不是简单写颜色，而是把秋天的生命力写出了胜过春花的气势。"}
];

export const themes = [
 {name:"山水",value:31},{name:"思乡",value:27},{name:"送别",value:22},{name:"忧国",value:19},{name:"怀古",value:16},{name:"边塞",value:14}
];
export const stats = {
 poems:300, authors:77, themes:24, relations:1268,
 emotions:[{name:"悲愁",value:28},{name:"思乡",value:22},{name:"闲适",value:18},{name:"豪迈",value:14},{name:"喜悦",value:10},{name:"送别",value:8}]
};
export const imagery = ["月","酒","山","水","春","秋","风","云","花","柳","雁","舟"];
