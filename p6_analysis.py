from p6_game import Simulator
from heapq import heappush, heappop

ANALYSIS = {}

shortest_paths = {}

#design is a dict containing information loaded from
#the map file named on the cmd line
def analyze(design):
  #Use this dict to construct a Simulator object.
  sim = Simulator(design)
  init = sim.get_initial_state()
  iPos, iAb = init
	
  prev = {}

  #initial values for dictionaries
  prev[iPos] = None
    
  #heapq of unvisited nodes
  q = []

  #push initial value
  q.append(init)
  #while we have values in the immediate surrounding unvisited nodes we plan to visit, loop
  while q:
    #pull a state out of q and get pertinent information about node within and surrounding nodes
    curr_state = q.pop(0)
    cPos, cAb = curr_state
    #check neighbours
    for move in sim.get_moves():
      next_state = sim.get_next_state(curr_state, move)
      if next_state and next_state not in prev:
        prev[next_state] = curr_state
        nPos = ()
        nPos, nAb = next_state
        q.append(next_state)
  
  ANALYSIS = prev

def inspect((i,j), draw_line):
    