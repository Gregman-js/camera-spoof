sudo modprobe v4l2loopback devices=1 exclusive_caps=1
if [ ! -f ./data/shape_predictor_68_face_landmarks.dat ]; then
    wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 -P ./data/
    bzip2 -d data/shape_predictor_68_face_landmarks.dat.bz2
fi