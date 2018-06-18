from CTFd import create_app

app = create_app()
app.run(debug=True, threaded=True, host="45.63.122.81", port=4000)
