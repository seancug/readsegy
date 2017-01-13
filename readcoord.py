import segypy as sg
import os
import time
from PyQt4 import QtGui, QtCore
import numpy as np
import sys
# endian='>' # Big Endian  # modified by A Squelch
# endian='<' # Little Endian
# endian='=' # Native
app=QtGui.QApplication(sys.argv)
begin = time.clock()
filelist = os.listdir('data')

progressDialog = QtGui.QProgressDialog()
progressDialog.setWindowModality(QtCore.Qt.WindowModal)
progressDialog.setWindowTitle("Processing")
progressDialog.setLabelText("Transform...")
progressDialog.setRange(0, len(filelist) - 1)
progressDialog.setCancelButton(None)
progressDialog.show()
inum = 0
progressDialog.setValue(1)

for filename in filelist:
    fileshort = filename.split('.')[0]
    sg.verbose = 1
    # [Data,SH,STH]=sg.readSegy(filename);
    segdata = open('data/' + filename, 'rb').read()
    SH = sg.getSegyHeader('data/' + filename, '>')
    STH = sg.getAllSegyTraceHeaders(SH, segdata, '>')
    SourceX = np.abs(STH['SourceX'])/3600.0/1000.0
    SourceY = STH['SourceY']/3600.0/1000.0
    Tracenum = STH['FieldRecord']
    if os.path.exists('coord') == False:
        os.makedirs('coord')
    fp = open('coord/' + fileshort + '.txt', 'w')


    for (num, ax, ay) in zip(Tracenum, SourceX, SourceY):
        strtmp = '%s\t%6d\t%14.8f\t%14.8f\n' % (fileshort, num, ax, ay)
        fp.writelines(strtmp)
    fp.close()
    inum += 1
    progressDialog.setValue(inum)

progressDialog.close()
end = time.clock()
print "read time: %f s" % (end - begin)
