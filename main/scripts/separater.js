const fs = require('fs');

function separating(arr_apps)
{
  for (var r = 0; r < arr_apps.length; r++) {
    if (arr_apps[r].score <= 3) {
      fs.appendFile("C:/Projects/blueway/main/dataset/url_low_score.csv", JSON.stringify(arr_apps[r].url) + "\n",
      function(erro) {
          if(erro) {
              throw erro;
          }
      });
    } else {
      fs.appendFile("C:/Projects/blueway/main/dataset/url_high_score.csv", JSON.stringify(arr_apps[r].url) + "\n",
      function(erro) {
          if(erro) {
              throw erro;
          }
      });
    }
  }
  console.log("\n :::apps:::separated::: \n");
}

var arr_apps = []

separating(arr_apps)
