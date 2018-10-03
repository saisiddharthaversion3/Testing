# @Author: Ankur Nair
# @Date:   2018-05-22T18:59:57+05:30
# @Email:  ankur.nair@cesltd.com
# @Project: Version 3 School Kiosk
# @Last modified by:   Ankur Nair
# @Last modified time: 2018-05-24T15:32:30+05:30
# @Copyright: Version 3



# from flask import Flask, jsonify
# from utils import visual_recognition as vis_util
#
# app = Flask(__name__)
#
# #Boiler plate Update to invoke capture image from DL & Compare with the face captured
# @app.route('/capture', methods=['GET'])
# def capture_image():
#     #return jsonify({'tasks': 'picture'})
#     vis_util.run_recognition('/home/administrator/Pictures/photo.jpg')
#     return jsonify({'tasks': 'picture'})
#
# if __name__ == '__main__':
#     app.run(debug=True)
