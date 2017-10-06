from flask import Flask, url_for
import os
import socket

app = Flask(__name__)

# "<img src = 'static/oc.png' ><br>" \
# "<img src = 'static/ArnoldSchwartzenegger.jpeg' > <br>" \

@app.route("/")
def hello():
        
    html = "<h2>Hello {name}!</h2>" \
        "<img src = 'static/ArnoldSchwartzenegger.jpeg' > <br>" \
        "<h3>Hostname is dynamically named by container runtime platform:</h3>" \
        "<b>Hostname is </b> {hostname}<br/>" \
    
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

