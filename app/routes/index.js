var express = require('express');
var router = express.Router();
let connect = require("../schema/data");
let application = connect.Mongoose.model('application', connect.modelSchema, 'application');

router.get('/', function(req, res) {
  application.find({}).lean().exec(
    function (err, results) {
      console.log(results);
      res.render('index', { datas: results });
    });
});

module.exports = router;
