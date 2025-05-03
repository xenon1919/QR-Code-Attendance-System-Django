import numpy as np
import os, cv2, pymysql, time

global employeeID, currentDate
employeeID = 0

def isEmpExists(code):
    flag = False
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='admin', password='root123',
                              database='emp_attendance', charset='utf8')
    with connect:
        curs = connect.cursor()
        curs.execute("SELECT * FROM employee_details WHERE employeeID = %s", (code,))
        rows = curs.fetchall()
        flag = bool(rows)
    return flag

def isAttendanceTaken(code):
    flag = False
    current_date = str(time.strftime('%Y-%m-%d'))
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='admin', password='root123',
                              database='emp_attendance', charset='utf8')
    with connect:
        curs = connect.cursor()
        curs.execute("SELECT * FROM mark_attendance WHERE employeeID = %s AND attended_date = %s", (code, current_date))
        rows = curs.fetchall()
        flag = bool(rows)
    return flag

def takeAttendance(employee_code):
    message = "Internal error occurred"
    current_date = str(time.strftime('%Y-%m-%d'))

    if not isEmpExists(employee_code):
        message = "Waiting for scan"
    elif isAttendanceTaken(employee_code):
        message = "Attendance accepted only once per day"
    else:
        connect = pymysql.connect(host='127.0.0.1', port=3306, user='admin', password='root123',
                                  database='emp_attendance', charset='utf8')
        with connect:
            curs = connect.cursor()
            curs.execute("INSERT INTO mark_attendance (employeeID, attended_date) VALUES (%s, %s)",
                         (employee_code, current_date))
            connect.commit()
        message = f"✅ Attendance Accepted for Employee ID {employee_code}"

    return message

def startWebcam():
    global employeeID
    status = "Waiting"

    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("❌ Failed to open webcam. Is it connected or in use by another app?")
        return

    qr_reader = cv2.QRCodeDetector()

    while True:
        ret, image = webcam.read()
        if not ret:
            print("❌ Failed to grab frame from webcam.")
            break

        code, bounding, _ = qr_reader.detectAndDecode(image)

        if bounding is not None and len(bounding) > 0:
            points = bounding.astype(int).reshape(-1, 2)
            for i in range(len(points)):
                pt1 = tuple(points[i])
                pt2 = tuple(points[(i + 1) % len(points)])
                cv2.line(image, pt1, pt2, color=(255, 0, 0), thickness=2)

        if code and code != employeeID:
            status = "Last Scan Result: " + takeAttendance(code)
            employeeID = code

        cv2.putText(image, status, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        cv2.imshow("Employee Attendance System", image)

        if cv2.waitKey(1) == ord("q"):
            break

    webcam.release()
    cv2.destroyAllWindows()

# Start the program
startWebcam()
