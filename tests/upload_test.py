import logging
import os

from app import db
from app.db.models import User, Song

def test_upload_file(application, client):

    with application.app_context():
        data = {
            'email': '123@gmail.com',
            'password': '123456',
            'confirm': '123456'
        }
        client.post("/register", data=data)

        data_test_1 ={
            'email': '123@gmail.com',
            'password': '123456'

        }

        client.post("/login",data = data_test_1)
        root = os.path.dirname(os.path.abspath(__file__))
        testdir = os.path.join(root, '../tests')
        assert os.path.exists(testdir) == True

        test_file = os.path.join(testdir, 'test.csv')
        assert os.path.exists(test_file) == True
        upload_dir = os.path.join(root, '../app/uploads')
        assert os.path.exists(upload_dir)

        data_test_2 ={
            'file' : open(test_file,'rb')
        }
        responce = client.post('/songs/upload', data = data_test_2)
        assert responce.status_code == 400
        assert len(os.listdir(upload_dir)) == 0
        for f in os.listdir(upload_dir):
            os.remove(os.path.join(upload_dir,f))
       


