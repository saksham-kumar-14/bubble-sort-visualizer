#bubble sort sorting algorithm visualizer
import pygame,sys,random
pygame.init()
WIDTH,HEIGHT = 900,600
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bubble Sort Algorithm Visualizer")
FONT = pygame.font.Font("freesansbold.ttf",40)
IS_SORTED = False

#defining the bubble sort sorting algorithm class 
class bubble_sort:
    def __init__(self,list_):
        self.length = len(list_)
        self.list_ = list_
        self.width = (WIDTH//self.length) - 25


    def unsorted_visualizer(self):
        global FONT
        self.x = 0 
        self.display_word = FONT.render("UNSORTED LIST",True,(255,0,55))
        self.display_word_x,self.display_word_y = 300,50 
        SCREEN.blit(self.display_word,(self.display_word_x,self.display_word_y))
        for item in range(0,self.length):
            self.height = list_[item]
            if item == 0:
                self.x = 20
            else:
                self.x = self.x +self.width + 20
            self.y = HEIGHT-self.height - 15
            pygame.draw.rect(SCREEN,(0,0,0),pygame.Rect(self.x,self.y,self.width,self.height))

    def bubble_sort(self,list_):
        self.display_word0 = FONT.render("SORTING ... ",True,(255,0,55))
        self.display_word_x,self.display_word_y = 300,50 
        SCREEN.fill((255,255,255))
        SCREEN.blit(self.display_word0,(self.display_word_x,self.display_word_y))
        for i in range(0,len(list_)):
            for j in range(0,len(list_)):
                if(list_[i]>list_[j]):
                    temp=  list_[i]
                    list_[i]=list_[j]
                    list_[j] = temp

                for item in range(0,self.length):
                    self.height = self.list_[item]
                    if item == 0:
                        self.x = 20
                    else:
                        self.x = self.x +self.width + 20
                    self.y = HEIGHT-self.height - 15
                    pygame.draw.rect(SCREEN,(0,0,0),pygame.Rect(self.x,self.y,self.width,self.height))

                pygame.time.Clock().tick(45)
                pygame.display.update()


    def sorting_visualizer(self,visualize):
        global FONT,IS_SORTED 
        self.display_word = FONT.render("SORTED LIST",True,(0,55,255))
        self.display_word_x,self.display_word_y = 300,50
        SCREEN.blit(self.display_word,(self.display_word_x,self.display_word_y))

        #bubble sort 
        if not IS_SORTED:
            self.bubble_sort(list_)

        IS_SORTED = True 


        #displaying the sorted list
        if IS_SORTED:
            SCREEN.fill((255,255,255))
            SCREEN.blit(self.display_word,(self.display_word_x,self.display_word_y))
            for item in range(0,self.length):
                self.height = self.list_[item]
                if item == 0:
                    self.x = 20
                else:
                    self.x = self.x +self.width + 20
                self.y = HEIGHT-self.height - 15
                pygame.draw.rect(SCREEN,(0,0,0),pygame.Rect(self.x,self.y,self.width,self.height))




#main execution 
if __name__=="__main__":
    visualize = False
    list_ = [99,70,45,23,15,66,79,88,150,167]
    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

        ########################################################################33
        SCREEN.fill((255,255,255))
        
        #for the algorithm
        algo = bubble_sort(list_)

        if 100>=mouse_pos[0]>=0 and 50>=mouse_pos[1]>=0 :
            pygame.draw.rect(SCREEN,(0,255,0),pygame.Rect(0,0,100,50))
            if True in mouse_pressed:
                visualize = True 
        else:
            pygame.draw.rect(SCREEN,(0,128,0),pygame.Rect(0,0,100,50))

        if visualize:
            algo.sorting_visualizer(visualize)
        else:
            algo.unsorted_visualizer()


        pygame.time.Clock().tick(60)
        pygame.display.update()