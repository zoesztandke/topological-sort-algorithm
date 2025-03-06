from typing import Dict, Union, Set

def top_sort(G: Dict[Union[int, str], Set[Union[int, str]]]) -> list:
    """
    Topological sort of directed graph
    :param G: a graph G
    :return: a list of vertices in topological order
    """
    state = {node: 'white' for node in G} # set initial state of all nodes to white

    L = [] # begin with an empty list

    for v in G: # for each vertex
        if state[v] == 'white': # if the vertex is white
            sort_from_vertex(G, v, L, state) # sort from the vertex

    return L # return the list of vertices in topological order

def sort_from_vertex(G: Dict[Union[int, str], Set[Union[int, str]]], v: Union[int, str], L: list, state: Dict[Union[
    int, str], str]) -> None:
    state[v] = 'gray' # set the state of the vertex to gray
    for w in v: # for each vertex w adjacent to v
        if state[w] == 'white': # if the vertex is white (hasn't been visited)
            sort_from_vertex(G, w, L, state) # sort from the vertex
        elif state[w] == 'gray': # if the vertex is grey (has been visited)
            print('Cycle detected') # cycle detected, stop the function
            break
    state[v] = 'black' # set the state of the vertex to black (finished)
    L.insert(0, v) # insert the vertex to the front of the list
