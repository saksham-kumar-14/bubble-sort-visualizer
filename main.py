#bubble sort visualizer
import pygame,time,sys
pygame.init()
WIDTH,HEIGHT = 900,600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))



#defining the bubble sort class 
class Bubble_sort:
    def __init__(self,list_,is_sorted):
        self.list_ = list_
        self.is_sorted = is_sorted 

    def display(self,run_time):

        self.item_x,self.item_width = 25,(WIDTH//len(self.list_))//2
        self.font = pygame.font.Font("freesansbold.ttf",32)
        self.font2 = pygame.font.Font("freesansbold.ttf",18)
        self.font_x,self.font_y = WIDTH//2 - 100 , 50  
        if is_sorted:
            self.info = self.font.render("SORTED LIST",True,(0,255,0))
            self.run_time_font = self.font2.render(f"Run Time : {run_time}",True,(128,0,0))
            self.rtx,self.rty = WIDTH//2 - 100 , 100 
        else:
            self.info = self.font.render("UNSORTED LIST",32,(255,0,0))


        SCREEN.blit(self.info,(self.font_x,self.font_y))
        if is_sorted:
            SCREEN.blit(self.run_time_font,(self.rtx,self.rty))
        for i in list_:
            self.item_y = HEIGHT - i 
            pygame.draw.rect(SCREEN,(0,0,0),pygame.Rect(self.item_x,self.item_y,self.item_width,i))
            self.item_x += (WIDTH//len(self.list_))

    def sort(self,should_start):
        #performing bubble sort 
        self.info = self.font.render("SORTING ..... ",True,(255,255,0))
        SCREEN.fill((255,255,255))
        SCREEN.blit(self.info,(self.font_x,self.font_y))

        self.time = time.time()
        for i in range(len(self.list_)):
            for j in range(i+1,len(self.list_)):
                if self.list_[i] > self.list_[j]:
                    self.temp = self.list_[i]
                    self.list_[i] = self.list_[j]
                    self.list_[j] = self.temp 

                    self.item_x = 25 
                    for k in self.list_:
                        self.item_y = HEIGHT - k 
                        pygame.draw.rect(SCREEN,(0,0,0),pygame.Rect(self.item_x,self.item_y,self.item_width,k))
                        self.item_x += (WIDTH//len(self.list_))

                    pygame.time.Clock().tick(10)
                    pygame.display.update()

        self.time = time.time() - self.time 

        self.is_sorted = True 
        should_start = False 

        return [self.list_,should_start,self.is_sorted,self.time]


#defining the button class 
class btn:
    def run(self,x,y,width,height,should_start):
        self.m_pos,self.m_pressed = pygame.mouse.get_pos(),pygame.mouse.get_pressed()
        if x + width >= self.m_pos[0] >= x and y+height>=self.m_pos[1]>=y:
            self.color = (0,255,0)
            if True in self.m_pressed:
                should_start = True 
        else:
            self.color = (0,128,0) 

        pygame.draw.rect(SCREEN,self.color,pygame.Rect(x,y,width,height)) 
        return should_start
          



#main execution
if __name__ == "__main__":
    list_ = [99,70,45,23,15,66,79,88,150,167,49,79,179,42,100,150]
    is_sorted = False
    should_start = False 
    run_time = 0 
    while True :
        SCREEN.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

        algo = Bubble_sort(list_,is_sorted)
        algo.display(run_time)

        should_start = btn().run(0,0,100,50,should_start) 

        if should_start:
            temp = algo.sort(should_start)
            list_ = temp[0]
            should_start = temp[1]
            is_sorted = temp[2]
            run_time = temp[3] 

        pygame.display.update()













