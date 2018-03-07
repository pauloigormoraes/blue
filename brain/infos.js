const request = require('request')
const cheerio = require('cheerio');
const uri = 'url.app.scraper';

request(uri, function(error, result, html) {
  if(!error) {
    const $ = cheerio.load(html);
    const content = $('.details-info');
    const app = content.find('.id-app-title').text().trim();
    const category = content.find('.document-subtitle.category').text().trim();
    const developer = content.find('.document-subtitle.primary').text().trim();
    const date = $($("*[itemprop = 'datePublished']").get(0)).text().trim();
    const version = num($($("*[itemprop = 'softwareVersion']").get(0)).text().trim());
    const versionandroid = $($("*[itemprop = 'operatingSystems']").get(0)).text().trim();
    const reviewsall = $('.reviews-num').text().trim();
    const appscore = num($('.score-container, .score').text().trim());
    const struct = {
        app: app,
        category: category,
        developer: developer,
        date: date,
        version: version,
        downloads: versionandroid,
        qtdreviews: reviewsall,
        score: appscore
    }
  } else {
    console.log("Check error: " + error.message);
  }
});

function num(arr) {
  let str = arr.split(",")
  var value
  for (var r = 0; r < str.length; r++) value = str[0] + "." + str[1];
  return parseFloat(value);
}