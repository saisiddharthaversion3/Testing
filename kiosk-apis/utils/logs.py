from application import mongo


def save_face_recognition_logs(**kwargs):
    face_recongn_log = mongo.db.logs
    data = {'image': kwargs['image']}
    log = face_recongn_log.insert(data)
    return True
