var express = require('express');
var router = express.Router();
let connect = require("../schema/data");
let application = connect.Mongoose.model('application', connect.modelSchema, 'application');

router.get('/index', function(req, res) {
  application.find({}).lean().exec(
    function (err, results) {
      res.render('main', { datas: results });
    });
});

router.get('/index/category/education', function(req, res) {
    res.render('education', );
});

router.get('/index/category/network', function(req, res) {
    res.render('social', );
});

router.get('/index/category/finance', function(req, res) {
    res.render('finance', );
});

router.get('/teste', function(req, res) {
    res.render('error', );
});

module.exports = router;
