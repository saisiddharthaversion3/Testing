from flask import Blueprint
import flask_restful
import face_recognition
import base64
from flask_restful import reqparse
from utils.twilio import send_warning_message
from utils.logs import save_face_recognition_logs
API_VERSION_V1 = 1
API_VERSION = API_VERSION_V1

face_auth = Blueprint('face_auth', __name__)
api_v1 = flask_restful.Api(face_auth)


class HelloWorld(flask_restful.Resource):
    def get(self):
        return {
            'hello': 'world',
            'version': API_VERSION,
        }


api_v1.add_resource(HelloWorld, '/helloworld')


class FaceRecognition(flask_restful.Resource):

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('image', type=str)

        args = parse.parse_args(strict=True)
        imgdata = base64.b64decode(args['image'])
        try:
            save_face_recognition_logs(image=args['image'])
        except Exception as e:
            print("An Exception Occured-{log}".format(log=e))
        with open("imageToSave.png", "rb+") as fh:
            fh.write(imgdata)
            known_image = face_recognition.load_image_file(fh)
            known_face_encoding = face_recognition.face_encodings(known_image)[0]
            unknown_image = face_recognition.load_image_file(
                "/home/administrator/Pictures/514222_v9_bb.jpg")
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
            # Load a second sample picture and learn how to recognize it.

            # Create arrays of known face encodings and their names
            known_face_names = [
                "Subject"
            ]
            process_this_frame = True

            if process_this_frame:
                results = face_recognition.compare_faces([unknown_face_encoding], known_face_encoding)
                # If a match was found in known_face_encodings, just use the first one.
                if True in results:
                    first_match_index = results.index(True)
                    name = known_face_names[first_match_index]
                    return {"message": "Face Matched"}
                else:
                    # send_warning_message()
                    return {"message": "Face Unmatched"}


api_v1.add_resource(FaceRecognition, '/scanface')
