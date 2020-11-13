ROOT_PATH="/home/grzegorz/projects/fake-webcam"
sudo modprobe v4l2loopback devices=1 exclusive_caps=1
if [ ! -f $ROOT_PATH/data/shape_predictor_68_face_landmarks.dat ]; then
    wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 -P $ROOT_PATH/data/
    bzip2 -d $ROOT_PATH/data/shape_predictor_68_face_landmarks.dat.bz2
fi
python3 $ROOT_PATH/main.py