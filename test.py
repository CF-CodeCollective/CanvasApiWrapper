from canvas_api import canvas

data_file = open("canvas-token.txt")
token, address, course, id, _ = data_file.readlines()
data_file.close()

token = token.strip()
address = address.strip().rstrip("/")
course = course.strip()
id = id.strip()

cvs = canvas.Canvas(address, token)
object_requester = cvs.get_object_requester()

status_code, user = object_requester.get_user(f"sis_user_id:{id}")
print(status_code)
print(user)
if (status_code == 200):
    print(user.id)
    print(user.name)
    print(user.sortable_name)