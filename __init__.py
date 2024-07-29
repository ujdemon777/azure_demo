# import logging
# import azure.functions as func

# def main(req: func.HttpRequest) -> func.HttpResponse:
#     method = req.method

#     if method == "GET":
#         return handle_get(req)
#     elif method == "POST":
#         return handle_post(req)
#     elif method == "PATCH":
#         return handle_patch(req)
#     elif method == "DELETE":
#         return handle_delete(req)
#     else:
#         return func.HttpResponse(
#             "Method not allowed",
#             status_code=405
#         )

# def handle_get(req: func.HttpRequest) -> func.HttpResponse:
#     # Implement GET logic here
#     return func.HttpResponse("GET request received")

# def handle_post(req: func.HttpRequest) -> func.HttpResponse:
#     # Implement POST logic here
#     return func.HttpResponse("POST request received")

# def handle_patch(req: func.HttpRequest) -> func.HttpResponse:
#     # Implement PATCH logic here
#     return func.HttpResponse("PATCH request received")

# def handle_delete(req: func.HttpRequest) -> func.HttpResponse:
#     # Implement DELETE logic here
#     return func.HttpResponse("DELETE request received")