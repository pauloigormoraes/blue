const request = require('request')
const cheerio = require('cheerio');
const csv = require('csv-write-stream');
const fs = require('fs');
const uri = 'https://play.google.com/store/getreviews';
const values = {
    reviewType: 0,
    pageNum: 10,
    id: "com.google.android.apps.youtube.mango",
    reviewSortOrder: 0,
    xhr: 1
}
var resreviews;



request(uri, function(error, result, html) {
  if(!error) {
    const $ = cheerio.load(html);
    resreviews = reviews($);
  } else {
    console.log("Check error: " + error.message);
  }
});

function reviews($) {
  let arr = [];
  let reviewsBox = $('div[class=single-review]');
  reviewsBox.each(function (r) {
    let _id = $(this).find('div[class=review-header]').data('reviewid').trim();
    let username = $(this).find('span[class=author-name]').text().trim();
    let date = $(this).find('span[class=review-date]').text().trim();
    let score = isNum($(this).find('.star-rating-non-editable-container').attr('aria-label').trim());
    let content = $(this).find('.review-body').text().trim();
    let review = { _id, username, date, score, content };
    arr[r] = review;
  });
  return reviews;
}

function isNum(arr) {
  let str = arr.split(" ")
  for (var r = 0; r < str.length; r++)
      if ((isNaN(str[r])) === false) num = str[r]
  return parseInt(num)
}
