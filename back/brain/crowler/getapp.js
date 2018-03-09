var gplay = require('google-play-scraper');

gplay.list({
    category: gplay.category.EDUCATION,
    collection: gplay.collection.TOP_FREE,
    lang: 'pt',
    country: 'br',
    num: 5
  })
  .then(console.log, console.log);
