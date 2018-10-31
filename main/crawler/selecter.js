const fs = require('fs');

function selection(arr)
{
  var pn, tmp = 0, arr_id_unsorted = [], arr_low_score = [], arr_limit = []

  // Aqui acontece o filtro dos comentários classificados apenas com 1 e 2 estrelas
  for (var r = 0; r < arr.length; r++) {
    if((arr[r].score) <= 2) {
      arr_low_score.push(arr[r])
    }
  }

  console.log("\n--------");
  console.log("SELECTED: #" + arr_low_score.length);
  console.log("--------\n");

  // Aqui eu orderno do maior para o menor o tamanho do meu array de comentários selecionados
  for (var r = 0; r < arr_low_score.length; r++)
    arr_id_unsorted.push(r)

  // Aqui eu desordeno o array para que não haja duplicidade na seleção dos comentários
  for (r = arr_id_unsorted.length; r; ) {
      p = Math.random() * r-- | 0;
      tmp = arr_id_unsorted[p];
      arr_id_unsorted[p] = arr_id_unsorted[r];
      arr_id_unsorted[r] = tmp;
  }

  // Aqui pegos as primeiras X posições do array desordenado
  for (var r = 0; r < 351; r++) {
    arr_limit.push(arr_id_unsorted[r])
  }

  for (var r = 0; r < arr_limit.length; r++) {
    for (var p = 0; p < arr_low_score.length; p++) {
      if(arr_limit[r] == p) {
        tmp = r
        // fs.appendFile("C:/Projects/blueway/main/dataset/raw_data/low_reviews.csv",
        // "[low_app_4_com_"+(tmp++)+"] " + arr_low_score[arr_limit[r]].content + "\n",
        fs.appendFile("C:/Projects/blueway/main/dataset/raw_data/high_reviews.csv",
        "[high_app_5_com_"+(tmp++)+"] " + arr_low_score[arr_limit[r]].content + "\n",
        function(erro) {
            if(erro) {
                throw erro;
            }
        });
      }
    }
  }

  console.log("\n----------------");
  console.log("REVIEWS SELECTED: #" + tmp);
  console.log("-----------------\n");

}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}


arr = [

]

selection(arr)
