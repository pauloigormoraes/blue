var gplay = require('google-play-scraper');

gplay.app({appId: 'br.com.vivo'})
  .then(console.log, console.log);

// app.list({
//     category: app.category.TOOLS,
//     collection: app.collection.TOP_FREE,
//     lang: 'pt',
//     country: 'br',
//     num: 100,
//     start: 401
//   })
//   .then(console.log, console.log);
