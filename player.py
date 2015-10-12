class player():

    def __init__(self,name,picture):
        self.person=0
        self.picture=picture
        self.name=name
        self.money=0
        self.bonus=0
        self.diamond=0
        self.star=0
        #self.passcard=0
        self.overdraft=0
        self.label=0
        self.position=0
        self.x=240
        self.y=0
        self.area=0
        self.house=0
        self.pictures={}
        

    def __str__(self):
        return "%s \n %i \n %i \n %i \n %i \n %i \n " %(self.name,self.money,self.diamond,self.star,self.overdraft,self.position)
        

    def buy_cell(self,cell,ans):
        if ans:
            self.money-=cell.money
            self.diamond-=cell.diamond
            cell.area.owner=self
            self.area=cell.area.size
            

    def pay(self,opponent,cell):
        if(cell.grade==1):
            self.money-=100
            opponent.money+=100
        elif(cell.grade==2):
            self.money-=200
            opponent.money+=200
        elif(cell.grade==3):
            self.money-=300
            opponent.money+=300

    def buy_goods(self,ans1,ans2):
        if(self.money>0):
            if ans1 :
                self.diamond+=1
                self.money-=200
            elif ans2:
                self.star+=1
                self.money-=100
            
        

    def upgrade(self,cell,ans):
        if(self.star>0 and cell.grade<3 and cell.grade>=1):
            if ans:
                cell.grade+=1
                self.star-=1

    def build(self,cell,ans):
        if(cell.grade==0 and self.money>=200):
            if ans:
                self.money-=200
                cell.grade=1
                self.house+=1
            

    def get(self):
        self.money+=self.bonus
    
    
