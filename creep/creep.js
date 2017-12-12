const rp = require('request-promise');
const ch = require('cheerio');

const content = {
  uri: 'https://www.pauloigormoraes.com',
  transform: function (body) {
    return ch.load(body);
  }
};

rp(content)
  .then(($) => {
    console.log('---# CONTENT #---');
    console.log($('.person-info').text());
  })
  .catch((err) => {
    console.log('---# ERROR #---');
    console.log(err);
  });
