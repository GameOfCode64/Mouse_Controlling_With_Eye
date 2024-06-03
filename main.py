import cv2
import mediapipe as mp
import pyautogui as pg

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,  screen_h = pg.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    _, frame_h, frame_w, = frame.shape


    if landmark_points:
        landmartks = landmark_points[0].landmark
        for id,  landmark in enumerate(landmartks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pg.moveTo(screen_x, screen_y)
    #
    left = [landmartks[145], landmartks[159]]
    for landmark in left:
        x = int(landmark.x * frame_w)
        y = int(landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 255))
    if(left[0].y - left[1].y) < 0.004:
        pg.click()
        pg.sleep(5)

    cv2.imshow('Eno Eye Control Mouse', frame)
    cv2.waitKey(1)



if __name__ == '__main__':
    print_hi('PyCharm')
