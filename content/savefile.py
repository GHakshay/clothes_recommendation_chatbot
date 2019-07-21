#!/usr/bin/python3
import cgi, os
import subprocess
import cgitb
cgitb.enable()
import webbrowser
#from imageai.Detection import ObjectDetection
import matplotlib.pyplot as plt

print("content-type:text/html")
print("")
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   #fn = os.path.basename(fileitem.filename)
   fn='x.jpg'
   open('/usr/lib/cgi-bin/' + fn, 'wb').write(fileitem.file.read())
   #f.close()
   message = 'The file "' + fn + '" was uploaded successfully'

   #execution_path = os.getcwd()
   #detector = ObjectDetection()
   #detector.setModelTypeAsRetinaNet()
   #detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
   #detector.loadModel()
   #detections=detector.detectObjectsFromImage(input_image=os.path.join(execution_path ,"x.jpg"),output_image_path=os.path.join(execution_path 
#,"imagenew.jpg"))

 #  for eachObject in detections:
 #     print(eachObject["name"])
 #     if 'clock' in eachObject["name"]:
 #        print("""<meta http-equiv="refresh" content="0;url=http://13.235.74.9/product.html">""")



























#subprocess.getoutput('python3 aaa.py')
   
#print("""<meta http-equiv="refresh" content="0;url=https://google.com">""")
'''else:
   message = 'No file was uploaded'
  
print """\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,)'''
