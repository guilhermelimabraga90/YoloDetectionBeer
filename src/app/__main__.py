import glob
import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, xmin, ymin, xmax, ymax, conf, class_name):
      self.xmin = xmin
      self.ymin = ymin
      self.xmax = xmax
      self.ymax = ymax
      self.conf = conf
      self.class_name = class_name



def overlap(r1, r2):

    if r1.xmin > r2.xmax or r1.xmax < r2.xmin:
        return False

    if r1.ymax < r2.ymin or r1.ymin > r2.ymax:
        return False

    return True

def importModel():
    
    imagestest = glob.glob("/content/YoloDetectionBeer/src/images/testImages/*.jpg")
    results = []
    model = YOLO('/content/YoloDetectionBeer/src/weights/best.pt')

    for image in imagestest:
        print("test")
        results.append(model(source=image, save=True))
    return results

def interection(results):
    
    for i in range(len(results)):
        img = mpimg.imread('/content/YoloDetectionBeer/runs/detect/predict/image' + str(i+1)+ ".jpg") #Replace "image.jpg" with the path of your image
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        for result in results[i]:
            boxes = []
        for box in result.boxes:
            xmin, ymin, xmax, ymax = box.xyxy[0].tolist()  # Obtendo as posições do BB
            class_id = box.cls[0].item()  # ID do objeto detectado
            conf = box.conf[0].item()  # Confiança na detecção
            class_name = result.names[class_id]  # Obtenha o nome da classe a partir de seu ID
            boxes.append(Retangulo(xmin, ymin, xmax, ymax, conf, class_name))
        for i in range(len(boxes)):
            for j in range(i+1, len(boxes)):
                if overlap(boxes[i], boxes[j]) and boxes[i].class_name != boxes[j].class_name:
                    if  (boxes[i].class_name == "Man" and boxes[j].class_name == "Woman") or  (boxes[i].class_name == "Woman" and boxes[j].class_name == "Man"):
                        pass
                    else:
                        print(f"Interaction between : {boxes[i].class_name} and {boxes[j].class_name}")



def main():
    results = importModel()
    interection(results)
    

if __name__ == '__main__':
    main()