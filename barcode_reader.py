import cv2
import numpy as np
from pyzbar import pyzbar

def read_barcode(frame):
    barcodes = pyzbar.decode(frame)
    
    for barcode in barcodes:
        x,y,w,h = barcode.rect

        #gets the single barcode info and writes it in utf8 format
        barcode_info = barcode.data.decode('utf-8')

        cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,barcode_info,(x+6,y-6),font, 1,(255,255,255),1)

        #creates a text file and prints the last read result
        with open("barcode_result.txt", mode='w') as file: 
            file.write("Taninan Barkod:" + barcode_info)
        
        print(barcode_info) 

    return frame

def main():
    #you can change the value inside video capture
    #to get your desired video capture
    camera = cv2.VideoCapture(0)

    ret, frame = camera.read()

    while ret:
        ret,frame = camera.read()
        #tried experimenting with a gray filter over frame didn't get stable results
        frame = read_barcode(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        
        #to close the window when q key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()