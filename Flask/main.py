from website import start_server

app = start_server()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)