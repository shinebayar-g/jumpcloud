def verify_response(response):
    try:
        return response.json()
    except ValueError:
        return {"message": response.text}
