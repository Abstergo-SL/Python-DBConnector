from flask import Flask, request, make_response
import supabase as db
import json


url = "https://vsfzxwsmptkuukibbjcq.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZzZnp4d3NtcHRrdXVraWJiamNxIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjY4NzU4MTksImV4cCI6MTk4MjQ1MTgxOX0.KlPoTtVj4qbDIyFkXJE_00OmPN69fR2JTVsCMm_aBpg"

tablename = "prueba"


supabase = db.create_client(url, key)

app = Flask(__name__)

@app.route('/select', methods=['POST'])
def select():
    table = request.args['table']
    data = supabase.table(table).select("*").execute()
    response = make_response(data.data)
    response.headers.add("Access-Control-Allow-Origin", "http://172.16.51.3")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response



@app.route('/data')
def web():
    data = supabase.table(tablename).select("*").execute()
    jsonData = json.loads(json.dumps(data.data))


    html = "<tr><th>id</th><th>nombre</th><th>apellido</th><th>edad</th></tr>"

    
    
    for item in jsonData:
        td = f"<tr><td>{item['id']}</td><td>{item['nombre']}</td><td>{item['apellido']}</td><td>{item['edad']}</td></tr>"
        html = html + "<tr>"+td+"</tr>"

    html = f"<table border='1'>{html}</table>"
    return html
