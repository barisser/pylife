import math
import factions
import map

def calculate_path(source, destination, world_object):
    startx = world_object.cities[source].x
    starty = world_object.cities[source].y
    endx = world_object.cities[destination].x
    endy = world_object.cities[destination].y

    queue = [[source, 99999999, 0, [source]]]  # city id, score, traversed_score, [previous_moves]

    n=0
    b=True
    while b:
        q = next_step(queue, destination, world_object)
        print q
        queue = q[1]
        if q[0]:
            b=False
            return queue
        n=n+1
        if n>=5:
            b=False
            print "not found"
            return queue


def next_step(queue, destination, world_object):  #queue must be sorted ascending
    arrived = False
    if len(queue) > 0:
        next_queue = queue[0]  #assuming sorted
        queue = queue[1:len(queue)-1]
        if next_queue[0] == destination:
            arrived = True
        else:
            traversed_score_on_queue_item = next_queue[2]
            #next_node = next_queue[0]
            neighbor_roads = world_object.cities[next_queue[0]].roads
            next_nodes = []
            for r in neighbor_roads:
                if r.destination == next_queue[0]:
                  next_nodes.append(r.source)
                else:
                  next_nodes.append(r.destination)

            for x in next_nodes:
                print "NEWQUEUE"
                print next_queue
                new_distance = distance(world_object.cities[x], world_object.cities[next_queue[0]])
                traversed_score_on_queue_item = traversed_score_on_queue_item + new_distance
                result = next_score(traversed_score_on_queue_item, x, destination, world_object)
                moves = next_queue[3]
                moves.append(x)
                new_item = [x, traversed_score_on_queue_item, result, moves]
                print "new item"
                print new_item
                queue.append(new_item)

    queue.sort(key=lambda x: x[1])

    return arrived, queue


def distance(nodea, nodeb):
    rx = nodea.x - nodeb.x
    ry = nodea.y - nodeb.y
    d = rx*rx + ry*ry
    d = math.pow(d, 0.5)
    return d

def next_score(current_traversed, next_node, destination, world_object):
    nodea = world_object.cities[next_node]
    nodeb = world_object.cities[destination]
    score = current_traversed + distance(nodea, nodeb)
    return score
