var request = require('request');
var cheerio = require('cheerio');
var csv = require('csv-write-stream');
var fs = require('fs');
const uri = 'https://play.google.com/store/apps/details?id=com.wonder';

request(uri, function(error, result, html) {
  if(!error) {
    const $ = cheerio.load(html);
    const content = $('.details-info');
    const app = content.find('.id-app-title').text().trim();
    const category = content.find('.document-subtitle.category').text().trim();
    const developer = content.find('.document-subtitle.primary').text().trim();
    const date = $($("*[itemprop = 'datePublished']").get(0)).text().trim();
    const version = $($("*[itemprop = 'softwareVersion']").get(0)).text().trim();
    const versionandroid = $($("*[itemprop = 'operatingSystems']").get(0)).text().trim();
    const reviewsall = $('.reviews-num').text().trim();
    const appscore = convert($('.score-container, .score').text().trim());
    const reviews = getReviews($);
    const struct = {
        app: app,
        category: category,
        developer: developer,
        date: date,
        version: version,
        downloads: versionandroid,
        qtdreviews: reviewsall,
        score: appscore,
        reviews: reviews
    }
    console.log(app);
    show(reviews)
  } else {
    console.log("Check error: " + error.message);
  }
});

function getReviews ($) {
  const reviews = [];
  const reviewsBox = $('div[class=single-review]');
  reviewsBox.each(function (r) {
    const _id = $(this).find('div[class=review-header]').data('reviewid').trim();
    const username = $(this).find('span[class=author-name]').text().trim();
    const date = $(this).find('span[class=review-date]').text().trim();
    const score = isNum($(this).find('.star-rating-non-editable-container').attr('aria-label').trim());
    const content = $(this).find('.review-body').text().trim();
    const review = { _id, username, date, score, content };
    reviews[r] = review;
  });
  return reviews;
}

function convert(n) {
  let br = n.split(",");
  for (var r = 0; r < br.length; r++) value = br[0] + "." + br[1];
  return parseFloat(value);
}

function isNum(nan) {
  let str = nan.split(" ");
  for (var r = 0; r < str.length; r++) num = str[3];
  return parseInt(num);
}

function show(reviews) {
  for (var r = 0; r < reviews.length; r++) {
    console.log(reviews[r])
  }
}
