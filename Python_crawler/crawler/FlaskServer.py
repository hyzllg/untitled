from flask import Flask,render_template
import time

#搭建服务器
#实例化一个对象
app = Flask(__name__)
#创建视图函数&路由地址
@app.route('/hyzhyz')
def index_1():
    time.sleep(2)
    return "hello Python_crawler"

@app.route('/llgllg')
def index_2():
    time.sleep(2)
    return render_template('html.html')
if __name__ == '__main__':
    #debug=True表示开启调试模式：服务器端代码被修改后按下保存键会自动重启服务
    app.run(debug=True)