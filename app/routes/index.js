var express = require('express');
var router = express.Router();
let connect = require("../schema/data");
let application = connect.Mongoose.model('application', connect.modelSchema, 'application');

// router.get('/main', function(req, res) {
//   application.find({}).lean().exec(
//     function (err, results) {
//       res.render('main', { datas: results });
//     });
// });
//
// router.get('/view', function(req, res) {
//   application.find({}).lean().exec(
//     function (err, results) {
//       res.render('view-data', { datas: results });
//     });
// });

module.exports = router;
