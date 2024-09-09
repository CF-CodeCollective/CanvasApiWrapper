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
if status_code == 200:
    print(user.id)
    print(user.name)
    print(user.sortable_name)

enrollment_service = cvs.get_enrollment_service()
status_code, enrollment = enrollment_service.enroll(course, f"sis_user_id:{id}", type=enrollment_service.enrollment_type.StudentEnrollment,
                          enrollment_state=enrollment_service.enrollment_state.Active, notify=True, self_enrolled=True)

print(status_code)
if status_code == 200:
    print(enrollment.user_id)
    print(enrollment.enrollment_state)
    print(enrollment.created_at)