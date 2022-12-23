import wasp
class cookieApp():
    NAME = "Cookie"

    def __init__(self):
        self.cookies = 0
        self.cursor = 1
        self.auto = 0

    def background(self):
        try:
            file = open("cookie.save","w")
            file.write(str(self.cookies)+"\n"+str(self.cursor)+"\n"+str(self.auto))
            file.seek(0)
            file.close()
        except Exception as e:
            with open("cookie.log","w") as x:
                x.write(str(e))
                x.close()

    def foreground(self):
        try:
            file = open("cookie.save","r")
            file.seek(0)
            if file.read() != '':
                file.seek(0)
                x = file.read().split('\n')
                try:
                    self.cookies = int(x[0])
                    self.cursor = int(x[1])
                    self.auto = int(x[2])
                except:
                    self.cookies = 0
                    self.cursor = 1
                    self.auto = 0
                self.drawInit()
            else:
                self.cookies = 0
                self.cursor = 1
                self.auto = 0
            file.close()
        except:
            self.cookies = 0
            self.cursor = 1
            self.auto = 0
        wasp.system.request_tick(1000)
        wasp.system.request_event(wasp.EventMask.TOUCH)
        self.drawInit()

    def drawInit(self):
        draw = wasp.watch.drawable
        draw.fill()
        draw.string("CCC",8,128)
        draw.string("CCC",8,128+32)
        draw.string("CCC",8,128+64)
        draw.string("FF",x=138,y=124)
        draw.string("AC",x=13,y=70+16)
        self.update()

    def update(self):
        draw = wasp.watch.drawable
        #'0'*(8-len(str(self.cookies)))+
        draw.string('0'*(12-len(str(self.cookies)))+str(self.cookies)+" c",0,32)
        draw.string(str(self.cursor),x=138,y=173-16)
        draw.string(str(self.auto),x=13,y=70-8)

    def tick(self,_):
        #REMOVE KEEPAWAKE
        wasp.system.keep_awake()
        self.cookies=self.auto+self.cookies
        time = wasp.watch.rtc.get_time()
        wasp.watch.drawable.string(str(time[0])+":"+str(time[1])+" "+str(wasp.watch.battery.level())+"%",0,240-24)
        if self.auto > 0:
            self.update()

    def touch(self,event):
        if event[1] < 64 and event[2] < 213 and event[1] > 4 and event[2] > 122:
            self.cookies=self.cookies+self.cursor
        if event[1] > 137 and event[2] > 122 and event[1] < 174 and event[2] < 180:
            if self.cookies > 99:
                self.cursor=self.cursor+1
                self.cookies=self.cookies-100
        if event[1] > 13 and event[2] > 70 and event[1] < 49 and event[2] < 111:
            if self.cookies > 199:
                self.auto=self.auto+1
                self.cookies=self.cookies-200
        self.update()