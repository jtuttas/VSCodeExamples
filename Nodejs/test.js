var express = require('express');
var app = express();
var router = express.Router();
var bodyParser = require('body-parser')
app.use(bodyParser.json());       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));

var server = app.listen(8081, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("Example app listening at http://%s:%s", host, port)

})


app.get('/list/:id', function (req, res, next) {
  console.log('GET empfangen ID=' + req.params.id);
  var obj = { "ID": req.params.id };
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify(obj));
})

app.delete('/del/:id', function (req, res, next) {
  console.log('Delete empfangen ID=' + req.params.id);
  var obj = { "ID": req.params.id };
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify(obj));
})

app.post('/new/', function (req, res) {
  console.log("POST Empfangen mit BODY=" + JSON.stringify(req.body));
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify(req.body));
})

app.put('/update/', function (req, res) {
  console.log("PUT Empfangen mit BODY=" + JSON.stringify(req.body));
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify(req.body));
})

app.get('/powershell/:filter', function (req, res, next) {
  console.log('GET POWERSHELL empfangen FILTER=' + req.params.filter);

  const exec = require('child_process').exec;
  var yourscript = exec('powershell.exe ./test.ps1 '+req.params.filter,
    (error, stdout, stderr) => {
      console.log(`${stdout}`);
      console.log(`${stderr}`);
      if (error !== null) {
        console.log(`exec error: ${error}`);
      }
      res.setHeader('Content-Type', 'application/json');
      res.send(stdout);
    });
})
