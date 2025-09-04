import wget
model_link = "http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d2_coco17_tpu-32.tar.gz"
wget.download(model_link)
import tarfile
tar = tarfile.open('efficientdet_d2_coco17_tpu-32.tar.gz')
tar.extractall('.')
tar.close()