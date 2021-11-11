
import requests
import shutil

with open("data.csv","r",encoding="utf8") as file:
   data = file.read()
   for a in data.split(";"):
       print(a)
       image_url = a
       filename = image_url.split("/")[-1]
       print("oao")
       if(image_url!=""):
           r = requests.get(image_url.replace(u'\ufeff', ''), stream = True)
           if r.status_code == 200:
               r.raw.decode_content = True
               with open(filename,'wb') as f:
                   shutil.copyfileobj(r.raw, f)
                   print('Image sucessfully Downloaded: ',filename)
           else:
               print('Image Couldn\'t be retreived')
