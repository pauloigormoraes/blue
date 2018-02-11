var express = require('express');
var router = express.Router();
var request = require('request');
var cheerio = require('cheerio');
var connect = require("../schema/data");
var Application = connect.Mongoose.model('application', connect.modelSchema, 'application');

router.get('/index', function(req, res) {
  application.find({}).lean().exec(
    function (err, results) {
      console.log(results);
      res.render('index', { datas: results });
    });
});

router.get('/', function(req, res) {

    // uri = 'https://play.google.com/store/apps/details?id=com.legacygames.crayolacds';
    uri = 'https://play.google.com/store/apps/details?id=com.wonder';

    function format(rating) {
      var arr = rating.split(" ");
       for (var r = 0; r < arr.length; r++) {
         scop = arr[0];
       }
      return parseInt(scop);
    };

    function convert(number) {
      var br = number.split(",");
      for (var r = 0; r < br.length; r++) value = br[0] + "." + br[1];
      return parseFloat(value);
    }

    request(uri, function(error, result, html) {
      if(error) {
        console.log("Check error: " + error.message);
      } else {
        var $ = cheerio.load(html);
        var name, category, author, updated, current_version, require_android, reviews_total, score, var_score, user, descript;
        $('.id-app-title').filter(function() { name = $(this).text(); });
        $('.document-subtitle.category').filter(function() { category = $(this).children().text(); });
        $('.document-subtitle.primary').filter(function() { author = $(this).children().text(); });
        var date = $("*[itemprop = 'datePublished']").get(0); updated = $(date).text().trim();
        var c_version = $("*[itemprop = 'softwareVersion']").get(0); current_version = $(c_version).text().trim();
        var r_android = $("*[itemprop = 'operatingSystems']").get(0); require_android = $(r_android).text().trim();
        $('.reviews-stats, .reviews-num').filter(function() { reviews_total = $(this).text(); });
        $('.score-container, .score').filter(function() { var_score = $(this).text(); }); score = convert(var_score);
        $('.featured-review .author-name').filter(function() { user = $(this).text(); });
        $('.featured-review span.review-text').filter(function() { descript = $(this).children().text(); });

      }
      var application = new Application({
        app_title: name,
        app_category: category,
        app_author: author,
        app_updated: updated,
        app_current_version: current_version,
        app_require_android: require_android,
        app_reviews_total: reviews_total,
        app_score: score,
        app_reviews: [{
          rw_username: user,
          rw_date: new Date(),
          rw_avaliation: 00,
          rw_description: descript
        }]
      });

      application.save(function (error) {
         if (error) {
             console.log("ERRO " + error.message);
             return error; }
         else { res.redirect("/"); }
      });

    });

});

module.exports = router;
