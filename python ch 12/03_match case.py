def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "internal Server Error"
        case _:
            return "Unknown status"
        
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(2008))
        