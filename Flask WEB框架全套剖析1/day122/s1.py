from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple


@Request.application
def hello(request):
    return Response('Hello World!')

if __name__ == '__main__':
    # 请求一旦到来，执行第三个参数    参数()
    run_simple('localhost', 4000, hello) # hello（xxx）