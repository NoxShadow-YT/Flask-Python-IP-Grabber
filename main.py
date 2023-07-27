import socket
from flask import Flask

app = Flask(name)

@app.route('/')
def index():
return '''

<html> <body> <script> function getIP(onNewIP) { var myPeerConnection = window.navigator.webkitGetUserMedia( {audio:true, video:true}, function(stream) { var ipAddr = stream.ipAddr; onNewIP(ipAddr); }, function(error) { console.log("Failed to get local IP address.",error); } ); };
Copy
     getIP(function(ip) {
       var xmlHttp = new XMLHttpRequest();
       xmlHttp.open( "GET", location.hostname+"/save?ip="+ip, false );  
       xmlHttp.send( null );
     });
   </script>
  </body>
</html>'''
@app.route('/save')
def save():
ip = request.args.get("ip")
with open("ips.txt","a") as f:
f.write(ip+"\n")
return ""

if name == 'main":
app.run(host='0.0.0.0', port=80)
