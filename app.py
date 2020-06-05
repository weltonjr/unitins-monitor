import winstats
import yaml
import pyrebase
import datetime

def parseDisk(drive):
  fsinfo = winstats.get_fs_usage(drive)
  vinfo = winstats.get_vol_info(drive)
  
  return { 
      "letter": drive,
      "name": vinfo.name,
      "total": fsinfo.total,
      "free": fsinfo.free,
      "used": fsinfo.used 
    }



with open("config.yml") as file:
  config = yaml.load(file, Loader=yaml.FullLoader)

  firebaseConfig = {
    "apiKey": "apiKey",
    "authDomain": "teste-pipelines-267818.firebaseapp.com",
    "databaseURL": "https://teste-pipelines-267818.firebaseio.com/",
    "storageBucket": "teste-pipelines-267818.appspot.com"
  }

  firebase = pyrebase.initialize_app(firebaseConfig)
  db = firebase.database()
 
  meminfo = winstats.get_mem_info()
  drives = winstats.get_drives()

  data = {
    "dateTime": datetime.datetime.now().timestamp(),
    "disks": list(map(parseDisk, drives)),
    "memory": {
      "total": meminfo.TotalPhys,
      "usage":  meminfo.MemoryLoad
    }  
  }

  results = db.child(config['machineName']).push(data)
  