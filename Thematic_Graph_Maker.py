# NIKIFORIDIS KONSTANTINOS 9084 ECE AUTH
# EXERCISE IN NETWORK THEORY
# JANUARY, 2021

import wikipedia
import networkx as nx
import random


# Theme
theme = "Tennis"


def_counter_run = 0

# english language
wikipedia.set_lang("en") 

# Dimiourgia tou thematikou diktiou (directed)
themnet = nx.DiGraph()

temp_list = []

# Epipeda 
level_1 = []
level_2 = []
level_3 = []

# Sinartisi pou dimiourgei komvous kai akmes analoga tin arxiki lexi
def links_nodes_edges(key_word):

    global themnet
    global def_counter_run
    node_links = []
    node_links.clear()
    n = 350                         

    
    try:
        temp_list = wikipedia.WikipediaPage(key_word).links
        for i in random.sample(temp_list, n if len(temp_list) > n else len(temp_list)):    
            if wikipedia.WikipediaPage(i).content.lower().count(theme.lower()) > 25 :
                node_links.append(i)                                                        
                themnet.add_node(i)
                themnet.add_edge(key_word, i)
                def_counter_run += 1
                print(def_counter_run)
    except:                                                             
        def_counter_run += 1
        print(def_counter_run)
        return ["Newbie"]
        



    return node_links #epistrefi lista me ta links-themata


level_1.append(theme)
level_2 = links_nodes_edges(theme)
print(level_2)
print("i am done with level 2")
for i in level_2:
    level_3.append(links_nodes_edges(i))

print("i am done with level 3")

for i in level_3:
    for j in i:
        links_nodes_edges(j)

print("i am done with level 4")


nx.write_gml(themnet, "Thematic_graph_gmlformat.gml")
