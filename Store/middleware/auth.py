# from django.shortcuts import redirect

# def auth_middlewares(get_response):

#     def middleware(request):
#         if not request.session.get('customer'):
#            return  redirect('login')
#         else:
#          response=get_response(request)
#         return response

#     return middleware        