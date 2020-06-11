var express = require('express');
var app = express();
var https = require('https')
var vm = require('vm')
var concat = require('concat-stream');

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.get('/view', function(req, res) {
	res.sendFile(__dirname + '/views/player.html')

});

app.get('/player', function(req, res) {
	https.get('https://sdk.scdn.co/spotify-player.js', (res) => {
		console.log('check');
		res.setEncoding('utf8');
		console.log("1")
		res.pipe(
			concat({ encoding: 'string' }),
			function(remoteSrc) {
				console.log(remoteSrc);
				vm.runInThisContext(remoteSrc, 'scripts/player.js');
			}
		);
	});	
	
	res.send('check');
});

console.log("listening");
app.listen(8888);
