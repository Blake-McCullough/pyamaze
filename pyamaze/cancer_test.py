import pytest
import test
from pyamaze import maze,agent,COLOR

def test_normal_case(self):
        
    m=maze(test.maxy,test.maxz)
    #m.CreateMaze(loadMaze= r"E:\_TAFE_WORK\Robotics\MyMazeCrap\pyamaze\maze--2022-11-18--14-20-17.csv")
    m.CreateMaze()
    b=agent(m,shape='arrow',color=COLOR.blue,footprints=True)
    c=agent(m,shape='square',color=COLOR.red,footprints=True)
    path,path2=test.wallFollower(m)


    m.tracePath({b:path2,c:path},delay=0)
    assert (path == (1,1)) == True, "Cannot start there"
    m.run()
    

test_normal_case("self")