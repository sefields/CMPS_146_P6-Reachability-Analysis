from p6_game import Simulator
from heapq import heappush, heappop
import p6_tool

ANALYSIS = {}

shortest_paths = {}

#design is a dict containing information loaded from
#the map file named on the cmd line
def analyze(design):
  global ANALYSIS
  ANALYSIS = {}
  #Use this dict to construct a Simulator object.
  sim = Simulator(design)
  init = sim.get_initial_state()
	
  #Prev is a dictionary. The keys are states.
  #The values are lists of states.
  #prev = {}
  
  #heapq of unvisited nodes
  q = []

  #push initial value
  q.append((init, [init]))
  #while we have values in the immediate surrounding unvisited nodes we plan to visit, loop
  while q:
    #pull a state out of q and get pertinent information about node within and surrounding nodes
    (curr_state, path) = q.pop(0)
    #check neighbours
    for move in sim.get_moves():
      next_state = sim.get_next_state(curr_state, move)
      if next_state and next_state not in ANALYSIS:
        ANALYSIS[next_state] = path
        q.append((next_state, path + [next_state]))
        
    #for thing in ANALYSIS:
        #print thing

def inspect((i,j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
    
    found = False
    for next in ANALYSIS:
        if i is next[0][0] and j is next [0][1]:
           path = ANALYSIS[next]
           offset = p6_tool.make_offset()
           color = p6_tool.make_color()
           for n in range(len(path) - 1):
               found = True
               draw_line(path[n][0], path[n+1][0], (next), color)
           draw_line(path[-1][0], (i,j), (next), color)
           
    if not found:
        print "Nothing was found"
    #raise NotImplementedError