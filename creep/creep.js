var gplay = require('google-play-scraper');
// gplay.app({appId: 'com.memorado.brain.games'});
// gplay.search({term: "educação", num: 3, lang: "pt", country: "br"}).then(console.log);

gplay.reviews({
  appId: 'co.brainly',
  lang: 'pt',
  page: 0
}).then(console.log, console.log);

// db.play.insert({"info":{"url": "https://play.google.com/store/apps/details?id=co.brainly", "appId": 'co.brainly', "title": 'Brainly - estude com a gente', "score": 4, "price": 0, "free": "true"}});
// db.play.insert({
// "category": [
// ["url": "https://play.google.com/store/apps/details?id=org.khanacademy.android", "appId": 'org.khanacademy.android', "title": 'Khan Academy', "score": 4, "price": 0, "free": "true" ],
// ["url": "https://play.google.com/store/apps/details?id=co.brainly", "appId": 'co.brainly', "title": 'Brainly - estude com a gente', "score": 4, "price": 0, "free": "true" ],
// ["url": "https://play.google.com/store/apps/details?id=com.ionicframework.cursosdegraca", "appId": 'com.ionicframework.cursosdegraca', "title": 'Cursos de Graça', "score": 4, "price": 0, "free": "true"]]});
