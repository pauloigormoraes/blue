var app = require('google-play-scraper');

app.list({
    category: app.category.TOOLS,
    collection: app.collection.TOP_FREE,
    lang: 'pt',
    country: 'br',
    num: 100,
    start: 401
  })
  .then(console.log, console.log);
