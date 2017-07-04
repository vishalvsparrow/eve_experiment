from eve import Eve

app = Eve()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.config['SERVER_NAME'] = True


