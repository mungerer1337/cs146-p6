from p6_game import Simulator
import Queue

ANALYSIS = {}


def analyze(design):
    sim = Simulator(design)
    init = sim.get_initial_state()
    moves = sim.get_moves()

    ANALYSIS.clear()

    queue = Queue.Queue()
    visited = []

    queue.put(init)
    ANALYSIS[init] = None
    visited.append(init)

    while not queue.empty():
        curr_state = queue.get()

        for move in moves:

            next_state = sim.get_next_state(curr_state, move)

            if next_state not in visited and next_state is not None:

                ANALYSIS[next_state] = curr_state
                queue.put(next_state)
                visited.append(next_state)


def inspect((i, j), draw_line):

    reachable = False
    dst_pos = (i, j)

    for state in ANALYSIS:
        curr_pos, curr_abilities = state
        if curr_pos == dst_pos:
            reachable = True
            curr_state = state
            my_abilities = curr_abilities

            while curr_state and ANALYSIS[curr_state]:
                curr_pos, curr_abilities = curr_state
                draw_line(curr_pos, ANALYSIS[curr_state][0], my_abilities, curr_abilities)
                curr_state = ANALYSIS[curr_state]

    if reachable:
        print "(%d,%d) is reachable!" % (i, j)
    else:
        print "(%d,%d) is unreachable!" % (i, j)
