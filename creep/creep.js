const promise = require('request-promise');
const cheerio = require('cheerio');

const content = {
  uri: 'https://www.allexlima.com',
  transform: function (body) {
    return cheerio.load(body);
  }
};

promise(content)
  .then(($) => {
    console.log('---# CONTENT #---');
    console.log($('.text-justify').text());
    // console.log($('.person-info').text());
  })
  .catch((err) => {
    console.log('---# ERROR #---');
    console.log(err);
  });
