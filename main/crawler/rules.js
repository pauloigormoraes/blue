const fs = require('fs');
const request = require('request');
const cheerio = require('cheerio');
const sleep = require('system-sleep');
const ur = require('unique-random');

var count = 0
var selected = []

arr = [

]


// SELECIONA COMENTÁRIOS COM 1 OU 2 ESTRELAS
for (var r = 0; r < arr.length; r++)
{
  if((arr[r].score) <= 2) {
    selected.push(arr[r])
  }
}

console.log("SELECTED: " + selected.length);

// SELECIONA RANDOMICAMENTE OS COMENTÁRIOS
for (var r = 0; r < selected.length; r++)
{
  if (r < selected.length) {
    fs.appendFile("/home/paulomoraes/Projects/blueway/main/dataset/high/.csv",
    "[high_app_1_com_"+(r+1)+"] " + selected[r].content + "\n",
    function(erro) {
        if(erro) {
            throw erro;
        }
    });
  } else break;
}

console.log("### SELECTED REVIEWS ###");
