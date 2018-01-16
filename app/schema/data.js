var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/__db', {
useMongoClient: true });

  var application = new mongoose.Schema({
    app_name: String,
    app_categorie: String,
    app_published: Date,
    app_installs: Number,
    app_current_version: Number,
    app_update: Date,
    app_require_android: Number,
    app_reviews: [{
      rw_username: String,
      rw_date: Date,
      rw_avaliation: Number,
      rw_description: String
    }]
  });

module.exports = { Mongoose: mongoose, modelSchema: application }
