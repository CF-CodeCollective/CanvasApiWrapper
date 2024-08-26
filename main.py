from canvas_enroller_minimal import EnrollmentService

data_file = open("canvas-token.txt")
token, address, course, id, _ = data_file.readlines()
data_file.close()

token = token.strip()
address = address.strip().rstrip("/")
course = course.strip()
id = id.strip()

enrollment_service = EnrollmentService(address, token, course)

status_code, body = enrollment_service.EnrollStudent(id)

print(status_code)