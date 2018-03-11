var app = require('google-play-scraper');

app.list({
    category: app.category.ENTERTAINMENT,
    collection: app.collection.TOP_FREE,
    lang: 'pt',
    country: 'br',
    num: 5
  })
  .then(console.log, console.log);
