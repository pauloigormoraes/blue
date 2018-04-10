const fs = require('fs');
const request = require('request');
const cheerio = require('cheerio');
const sleep = require('system-sleep');
const ur = require('unique-random');

let count = 0
let selected = []

arr = [

]

// SELECIONA OS APLICATIVOS COM AS REGRAS
// for (var app = 0; app < arr.length; app++)
// {
//   url = arr[app].url;
//   request(url, function(error, result, html) {
//     if(!error) {
//       const $ = cheerio.load(html)
//       const score = $('div.BHMmbe').text()
//       const appscore = parseFloat(score)
//       const reviews = $('span.EymY4b').text()
//       const appreviews = num(reviews)
//       console.log(":::processing:::["+app+"]::: " + "SCORE: " + appscore + " | REVIEWS: " + appreviews);
//       if((appscore >= 3.5) & (appreviews >= 1000)) {
//         // fs.appendFile("/home/paulomoraes/Projects/blueway/back/dataset/apps_filters_less.csv",
//         fs.appendFile("/home/paulomoraes/Projects/blueway/back/dataset/apps_filters_more.csv",
//         arr[app].url+"\n",
//         function(erro) {
//             if(erro) {
//                 throw erro;
//             }
//             console.log("#######[save-one]#######");
//         });
//       }
//     } else {
//       console.log("Check error: " + error.message);
//     }
//   });
//   sleep(5000);
// }
//
// // RECONFIGURANDO SCORE
// function num(n)
// {
//   let br = n.split(",")
//   let pr = br[(br.length)-1].split(" ")
//   switch (br.length) {
//     case 1:
//       value = pr[0]
//       break;
//     case 2:
//       value = br[0]+pr[0]
//       break;
//     case 3:
//       value = br[0]+br[1]+pr[0]
//       break;
//   }
//   return parseInt(value);
// }

// SELECIONA COMENTÁRIOS COM 1 OU 2 ESTRELAS
for (var r = 0; r < arr.length; r++)
{
  if((arr[r].score) <= 2) {
    selected.push(arr[r])
  }
}
// SELECIONA RANDOMICAMENTE OS COMENTÁRIOS
for (var r = 0; r < selected.length; r++)
{
  const rand = ur(0, selected.length)
  var rd = rand()
  if (count < 230) {
    count++
    fs.appendFile("/home/paulomoraes/Projects/blueway/back/dataset/selected_more.csv",
    arr[rd].content+"\n",
    function(erro) {
        if(erro) {
            throw erro;
        }
    });
  } else break;
}

console.log("### SELECTED REVIEWS ###");
