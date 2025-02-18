def middleware(get_response):
    print("first time initialized")
    def my_function(request):
        res = get_response(request)
        print(res)
        print("this is after view")
        return res
    return my_function