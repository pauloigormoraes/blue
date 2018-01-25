var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/__db', {
useMongoClient: true });

  var application = new mongoose.Schema({
    app_title: String,
    app_category: String,
    app_author: String,
    app_updated: String,
    app_current_version: String,
    app_require_android: String,
    app_reviews_total: Number,
    app_score: String,
    app_reviews: [{
      rw_username: String,
      rw_date: Date,
      rw_avaliation: Number,
      rw_description: String
    }]
  });

module.exports = { Mongoose: mongoose, modelSchema: application }
