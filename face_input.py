import cv2
import dlib 
import face_recognition
# print(dlib.__version__)
detector = dlib.cnn_face_detection_model_v1("C:\\Users\\ADMIN\\Downloads\\mmod_human_face_detector.dat")

input_image = cv2.imread("C:\\Users\\ADMIN\\Downloads\\happiness begins here\\open cv\\1684524563633.jpg")

input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

input_faces = detector(input_gray)
if len(input_faces) > 0:
    # input_landmarks = face_recognition.predictor(input_gray, input_faces[0])
    input_landmarks = face_recognition.face_landmarks(input_gray)
    # input_descriptor = face_recognition.compute_face_descriptor(input_gray, input_landmarks)
    input_descriptor = face_recognition.face_encodings(input_gray, input_landmarks)
else:
    print("No faces detected in the input image.")
    exit()