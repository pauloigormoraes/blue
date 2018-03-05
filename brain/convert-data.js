var csv = require('csv-write-stream');
var fs = require('fs');
const vtr = ['oi', 'tudo', 'bem'];

var writing = csv({
  separator: ',',
  newline: '\n',
  headers: ['description', 'weight'],
  sendHeaders: true
})

writing.pipe(fs.createWriteStream('/home/paulomoraes/Projects/lise/creep/data/game.csv'))
for(var i = 0; i < vtr.length; i++)
  writing.write([vtr[i], 'null'])
writing.end()
