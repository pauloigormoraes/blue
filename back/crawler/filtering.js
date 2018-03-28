var fs = require('fs');
var data = fs.readFileSync('/home/paulomoraes/Projects/blue/back/dataset/apps.txt', 'utf8');
console.log(data['title']);
