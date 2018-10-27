const fs = require('fs');

function selection(arr)
{
  var selected = []
  // SELECIONA COMENTÁRIOS COM 1 OU 2 ESTRELAS
  for (var r = 0; r < arr.length; r++) {
    if((arr[r].score) <= 2) {
      selected.push(arr[r])
    }
  }
  console.log("SELECTED: " + selected.length);
  // SELECIONA RANDOMICAMENTE OS COMENTÁRIOS
  for (var r = 0; r < selected.length; r++) {
    if (r < selected.length) {
      fs.appendFile("./main/dataset/high/.csv",
      "[high_app_1_com_"+(r+1)+"] " + selected[r].content + "\n",
      function(erro) {
          if(erro) {
              throw erro;
          }
      });
    } else break;
  }
  console.log("### SELECTED REVIEWS ###");
}
