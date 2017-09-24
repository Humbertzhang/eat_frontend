from app import app , generate_app

if __name__ == '__main__' :
    app = generate_app(app)
    app.run(host='0.0.0.0')
