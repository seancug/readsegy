import segypy as sg
import os
import time 

begin=time.clock()
filelist=os.listdir('data')

for filename in filelist:
    fileshort = filename.split('.')[0]
    sg.verbose=1;
    #[Data,SH,STH]=sg.readSegy(filename);
    segdata = open('data/'+filename,'rb').read()
    SH=sg.getSegyHeader('data/'+filename,'=')
    STH = sg.getAllSegyTraceHeaders(SH,segdata)
    SourceX=STH['SourceX']/3600.0;
    SourceY=STH['SourceY']/3600.0;
    Tracenum=STH['TraceSequenceFile']
    if os.path.exists('coord') == False:
        os.makedirs('coord')
    fp=open('coord/'+fileshort+'.txt','w');
    
    for (num,ax,ay) in zip(Tracenum,SourceX,SourceY):
        strtmp='%s\t%6d\t%14.8f\t%14.8f\n' %(fileshort,num,ax,ay)
        fp.writelines(strtmp);
    fp.close();
end=time.clock()
print "read time: %f s" % (end - begin)
