var express = require('express');
var router = express.Router();
var request = require('request');
const cheerio = require('cheerio');
var connect = require("../schema/data");
var Application = connect.Mongoose.model('application', connect.modelSchema, 'application');

router.get('/', function(req, res) {

    url = 'https://play.google.com/store/apps/details?id=com.wonder';

    request(url, function(error, result, body) {
      if(error) {
        console.log("Check error: " + error.message());
      } else {
        var $ = cheerio.load(body);
        var app_name, app_category;
        $('.id-app-title').filter(function() { app_name = $(this).text(); });
        $('.author').filter(function() { app_category = $(this).children().text(); });
      }
      var test = new Application({
        app_name: app_name,
        app_category: app_category,
        app_published: new Date(),
        app_installs: 00,
        app_current_version: 00,
        app_update: new Date(),
        app_require_android: 00,
        app_reviews: [{
          rw_username: "",
          rw_date: new Date(),
          rw_avaliation: 00,
          rw_description: ""
        }]
      });
      test.save(function (trash) {
         if (trash) {
             console.log("ERRO " + trash.message);
             return trash; }
         else { res.send("Check your console!"); }
      });

    });




});

module.exports = router;
