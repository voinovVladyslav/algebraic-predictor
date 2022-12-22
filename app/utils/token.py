def get_token(request):
    try:
        return request.headers['Authorization'].split()[1]
    except Exception:
        return
