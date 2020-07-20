from flask import Flask, render_template #플라스크 라이브러리로 서버를 띄우는 방법

app = Flask(__name__) #대문자 플라스크는 클라스 객체생성
app.debug = True

@app.route('/data')
def index():
    print("Success")
    return render_template('home.html')

if __name__=="__main__":
    # app.run(host = '0.0.0.0', port='8080')
    app.run()
