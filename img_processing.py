import sys
import math
import cv2 as cv
import numpy as np


def isnear(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):
    if ((abs(ax1-bx1) < 10) and (abs(ay1-by1)<10)):
        return 1
    elif ((abs(ax1-bx2) < 10) and (abs(ay1-by2)<10)):
        return 2
    elif ((abs(ax2-bx1) < 10) and (abs(ay2-by1)<10)):
        return 3
    elif ((abs(ax2-bx2) < 10) and (abs(ay2-by2)<10)):
        return 4
    else :
        return False



def gradient(linehere):
    float(linehere[0])
    float(linehere[1])
    float(linehere[2])
    float(linehere[3])
    return float((linehere[3]-linehere[1])/(linehere[2]-linehere[0]))


def measurelength(linehere):
    xsq = float((linehere[2] - linehere[0])**2)
    ysq = float((linehere[3] - linehere[1])**2)
    return ((ysq + xsq)**0.5)

def angle(x1, y1, x2, y2, len1, len2):
    inner_product = x1*x2 + y1*y2
    lens = float((len1*len2))
    cos = float(inner_product/lens)
    #print('ini ',cos)
    return math.acos(cos)

def measuredegree(connectedline, savedlines, lineLength):
    l1 = connectedline[0]
    len1 = lineLength[0]
    l2 = connectedline[1]
    len2 = lineLength[1]
    if (connectedline[2]==1):
        x0 = savedlines[l1][0]
        y0 = savedlines[l1][1]
        x1 = savedlines[l1][2]
        y1 = savedlines[l1][3]
        x2 = savedlines[l2][2]
        y2 = savedlines[l2][3]
    elif (connectedline[2]==2):
        x0 = savedlines[l1][0]
        y0 = savedlines[l1][1]
        x1 = savedlines[l1][2]
        y1 = savedlines[l1][3]
        x2 = savedlines[l2][0]
        y2 = savedlines[l2][1]
    elif (connectedline[2]==3):
        x0 = savedlines[l2][0]
        y0 = savedlines[l2][1]
        x1 = savedlines[l1][0]
        y1 = savedlines[l1][1]
        x2 = savedlines[l2][2]
        y2 = savedlines[l2][3]
    elif (connectedline[2]==4):
        x0 = savedlines[l2][2]
        y0 = savedlines[l2][3]
        x1 = savedlines[l1][0]
        y1 = savedlines[l1][1]
        x2 = savedlines[l2][0]
        y2 = savedlines[l2][1]
    xx1 = x1 - x0
    yy1 = y1 - y0
    xx2 = x2 - x0
    yy2 = y2 - y0
    #print('masuk degree', xx1, yy1, xx2, yy2, len1, len2)        
    teta = angle(xx1,yy1,xx2,yy2,len1,len2)
    ang = math.degrees(teta)
    return l1,l2,ang


def toSpecialAngle(in_angle):
    if abs(in_angle - 90) < 3 :
        return 90
    elif abs(in_angle - 60) < 3 :
        return 60
    elif abs(in_angle - 45) < 3 :
        return 45
    else :
        return in_angle

def ifSame(in1, in2) :
    if abs(in1 - in2) < 3:
        return in1, in1
    else :
        return in1, in2



def main(path):
    filename = path
    outfile = 'out' + filename
    savedlines = []
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
    if src is None:
        print ('Error opening image!')
        return -1
    dst = cv.Canny(src, 50, 200, None, 3)
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdst2 = np.copy(cdst)

    '''lines = cv.HoughLines(dst, 1, np.pi / 180, 50, None, 0, 0)
    
    if lines is not None:
        for i in range(0, len(lines)):
            print(lines[i])
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(cdst2, pt1, pt2, (0,0,255), 3, cv.LINE_AA)'''
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    if linesP is not None:
        for i in range(0, len(linesP)):
            #print(linesP[i])
            l = linesP[i][0]
            #print('batas')
            cv.line(cdst2, (l[0], l[1]), (l[2], l[3]), (0,255,255), 3, cv.LINE_AA)
    if linesP is not None:
        linenya = linesP[0][0]
        savedlines.append(linenya)
        #print('garis pada gambar (format koordinat awal dan akhir ==> x0,y0,x,y):')
        #print(savedlines)
        for i in range(1, len(linesP)):
            taken = True
            j = 0
            while (j<len(savedlines) and (taken)):
                same = 0
                if (abs(linesP[i][0][0]-savedlines[j][0])<10):
                    #print(linesP[i][0][0], end='-')
                    #print(savedlines[j][0], end=',')
                    same += 1
                    #savedlines.append(linesP[i][0])
                    #taken = True
                if (abs(linesP[i][0][1]-savedlines[j][1])<10):
                    #print(linesP[i][0][1], end='-')
                    #print(savedlines[j][1], end=',')
                    same += 1
                    #savedlines.append(linesP[i][0])
                    #taken = True
                if (abs(linesP[i][0][2]-savedlines[j][2])<10):
                    #print(linesP[i][0][2], end='-')
                    #print(savedlines[j][2], end=',')
                    same += 1
                    #savedlines.append(linesP[i][0])
                    #taken = True
                if (abs(linesP[i][0][3]-savedlines[j][3])<10):
                    #print(linesP[i][0][3], end='-')
                    #rint(savedlines[j][3])
                    same += 1
                    #savedlines.append(linesP[i][0])
                    #taken = True
                if ((same == 4) or ((abs(gradient(linesP[i][0]) - gradient(savedlines[j])) < 0.05) and (isnear(linesP[i][0][0], linesP[i][0][1], linesP[i][0][2], linesP[i][0][3], savedlines[j][0], savedlines[j][1], savedlines[j][2], savedlines[j][3])))):
                    taken = False
                j += 1
            if (taken):
                savedlines.append(linesP[i][0])                                                           
            #print(linesP[i][0][0], linesP[i][0][1], linesP[i][0][2], linesP[i][0][3])
    if savedlines is not None:
        for i in range(0, len(savedlines)):
            #print(i, end= ' ')
            print(savedlines[i])
            l = savedlines[i]
            cv.line(cdst, (l[0], l[1]), (l[2], l[3]), (0,255,255), 3, cv.LINE_AA)
    #print(len(linesP))
    #print("banyaknya garis")
    #print(len(savedlines))
    countLine = len(savedlines)

    connectedlines = []
    for i in range (len(savedlines)):
        for j in range (i+1, len(savedlines)):
            if (isnear(savedlines[i][0], savedlines[i][1], savedlines[i][2], savedlines[i][3], savedlines[j][0], savedlines[j][1], savedlines[j][2], savedlines[j][3])) :
                connectedline = []
                connectedline.append(i)
                connectedline.append(j)
                connectedline.append(isnear(savedlines[i][0], savedlines[i][1], savedlines[i][2], savedlines[i][3], savedlines[j][0], savedlines[j][1], savedlines[j][2], savedlines[j][3]))
                connectedlines.append(connectedline)
    #print(connectedlines)

    lineLength = [] #panjang setiap garis
    for i in range (len(savedlines)):
        length = measurelength(savedlines[i])
        lineLength.append(length)
    #print("panjang setiap garis, urutan sama kayak garis berdasarkan koordinat")
    #print(lineLength)

    angleDegree = []
    degreeAja = []
    for i in range (len(connectedlines)):
        l1,l2,degree = measuredegree(connectedlines[i], savedlines, lineLength)
        an_angle = []
        an_angle.append(l1)
        an_angle.append(l2)
        an_angle.append(toSpecialAngle(degree))
        angleDegree.append(an_angle)
        degreeAja.append(degree)
    #print("besar sudut, format : garis 1, garis 2, besar sudut, urutan garis sama kayak atas")
    for i in range (len(angleDegree)):
        for j in range (i+1, len(angleDegree)):
            angleDegree[i][2], angleDegree[j][2] = ifSame(angleDegree[i][2], angleDegree[j][2])
    #print(angleDegree)
    countDegree = len(angleDegree)
    #cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst2)
    #cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdst)
    cv.imwrite(outfile,cdst)
    #cv.waitKey()
    return countLine, savedlines,lineLength, countDegree, angleDegree

countLine, savedlines,lineLength, countDegree, angleDegree = main('img/layang.jpg')
print("jumlah sisi: " + str(countLine))
print(lineLength)
print(countDegree)
print(angleDegree)