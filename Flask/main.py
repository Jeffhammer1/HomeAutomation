from website import start_server

app = start_server()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", use_reloader=False)