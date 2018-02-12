var gplay = require('google-play-scraper');

gplay.reviews({
  appId: 'com.wonder',
  page: 0,
  num: 250,
  sort: gplay.sort.RATING
}).then(console.log, console.log);


// gplay.app({appId: 'com.wonder'})
//   .then(console.log, console.log);
