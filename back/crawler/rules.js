const fs = require('fs');
const request = require('request');
const cheerio = require('cheerio');
const sleep = require('system-sleep');
const ur = require('unique-random');

var count = 0
var selected = []

arr = []

// SELECIONA COMENTÁRIOS COM 1 OU 2 ESTRELAS
for (var r = 0; r < arr.length; r++)
{
  if((arr[r].score) <= 2) {
    selected.push(arr[r])
  }
}

console.log("SELECTED: " + selected.length);

// SELECIONA RANDOMICAMENTE OS COMENTÁRIOS
for (var r = 0; r < 2215; r++)
{
  const rand = ur(0, 2215)
  var rd = rand()
  if (count < 281) {
    count++
    fs.appendFile("/home/paulomoraes/Projects/blueway/back/dataset/low/.csv",
    "[low_app_1_com_"+count+"] " + selected[rd].content + "\n",
    function(erro) {
        if(erro) {
            throw erro;
        }
    });
  } else break;
}

console.log("### SELECTED REVIEWS ###");
