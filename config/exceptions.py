from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call DRF's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        # Add a custom 'status' key to all error responses
        response.data["status_code"] = response.status_code
        response.data["message"] = response.data.get("detail", "An error occurred.")

    return response
