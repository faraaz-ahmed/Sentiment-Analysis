var http = require('http');
var url = require('url');
var fs = require('fs');
const { parse } = require('querystring');
const spawn = require("child_process").spawn;



http.createServer(function (req, res) {
  if(req.method === 'POST'){
    let body = '';
    req.on('data', chunk => {
        body += chunk.toString(); // convert Buffer to string
        console.log(body);
    });
    req.on('end', () => {
        const flag = 0;
        console.log("recorded data is as follows : ",parse(body));
        s = parse(body).review;
        console.log("s = ",s);
        
        // spawning the Naive Bayes python module !
        const pythonProcess = spawn('python',["test.py", s]);
        pythonProcess.stdout.on('data', (data) => {
        // Do something with the data returned from python script
        console.log("data from the python script!", data.toString(),"end");
        console.log(typeof(data.toString()));
        console.log("length of the string = ", data.toString().length);
        var i = 0;
        var sum = 0;
        for(i = 0; i < data.toString().length ; i++){
          sum += data.toString().charCodeAt(i);
          console.log(data.toString().charCodeAt(i));
        }
        console.log('sum = ',sum);
        console.log("at zero", data.toString()[0]);
        console.log("at one", data.toString()[1]);
        console.log("at two", data.toString()[2]);
        
        if(sum === 71){
          console.log("negative review!");
          fs.readFile("negative_index.html", function(err, data) {
            if (err) {
              res.writeHead(404, {'Content-Type': 'text/html'});
              return res.end("404 Not Found");
            }  
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            return res.end();
          });
        }
        else{
          console.log("positive review!");
          fs.readFile("positive_index.html", function(err, data) {
            if (err) {
              res.writeHead(404, {'Content-Type': 'text/html'});
              return res.end("404 Not Found");
            }  
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            return res.end();
          });
        }

        });
        // res.end('ok');
    });
  }
  else{
    var q = url.parse(req.url, true);
    var filename = "." + q.pathname;
    fs.readFile(filename, function(err, data) {
      if (err) {
        res.writeHead(404, {'Content-Type': 'text/html'});
        return res.end("404 Not Found");
      }  
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.write(data);
      return res.end();
    });
  }
}).listen(8080);
