// Aqui são coletados a lista de aplicativos.
// A API Google Play Scraper coleta 120 aplicativos a cada requisão e nós coletamos 500.

var app = require('google-play-scraper');
var fs = require('fs');
var arr_result;
var arr_for_save;

app.list({
    category: app.category.GAME_EDUCATIONAL,
    collection: app.collection.TOP_FREE,
    lang: 'pt',
    country: 'br',
    num: 120,
    start: 482
  }).then(function(data) {
    arr_result = data;
  });

function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

sleep(5000).then(() => {
  try {
    for (var r = 0; r < arr_result.length; r++)
    {
      fs.appendFile("C:/Projects/blueway/main/dataset/list_apps.csv", JSON.stringify(arr_result[r]) + ",",
      function(erro) {
          if(erro) {
              throw erro;
          }
      });
      console.log('app:::['+r+']:::saved');
    }
  } catch(err) {
    console.log(err);
  }
});
