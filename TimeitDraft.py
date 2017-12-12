import random
import Sorting as s
import BST as t
import Heap as h
import timeit
import numpy as np
import matplotlib.pyplot as plt

iterab = np.logspace(1.0, np.log10(10000, dtype=float), base=10, endpoint=False, dtype=int, num=10)

x = random.choices(range(iterab[-1] + 1), k=iterab[-1])


# Function to measure the sorting time, and plotting the results
def Sorting_t(iterab, x):
    mergeS = []
    quickS = []
    for i in iterab:
        mergeS_time = timeit.timeit(lambda: s.mergeSort(x[:i]), number=10)
        mergeS.append(mergeS_time)
        quickS_time = timeit.timeit(lambda: s.quickSort(x[:i]), number=10)
        quickS.append(quickS_time)

    Show_graph(iterab, [mergeS, quickS], ['mergeSort', 'quickSort'])
    plt.title('Sorting time')
    plt.show()


# Measurements of the Binary Search Tree (insertion, get and delete a random element, find max)
def Tree_time(iterab, x, Graph=True):
    Tree = {'init_tree': [], 'insert_tree': [], 'get_tree': [], 'max_tree': [], 'delete_tree': [], 'final': []}
    for i in iterab:
        ranel = random.choice(x[:i])
        bst = t.BinaryTree(x[:i])
        init_tree = timeit.timeit(lambda: t.BinaryTree(x[:i]), number=10)
        insert_tree = timeit.timeit(lambda: bst.put(ranel), number=1)
        get_tree = timeit.timeit(lambda: bst.get(ranel), number=10)
        max_tree = timeit.timeit(lambda: bst.findMax(), number=10)
        delete_tree = timeit.timeit(lambda: bst.delete(ranel), number=1)
        Tree['init_tree'].append(init_tree)
        Tree['insert_tree'].append(insert_tree)
        Tree['get_tree'].append(get_tree)
        Tree['max_tree'].append(max_tree)
        Tree['delete_tree'].append(delete_tree)
        Tree['final'].append(init_tree + insert_tree + get_tree + max_tree + delete_tree )

    if Graph:  # plot only if it is required
        plt.figure(1)
        plt.subplot(211)
        plt.title('Binary Tree 1st')
        Show_graph(iterab, [Tree['final']], ['Final Time'])
        plt.subplot(212)
        Show_graph(iterab, [Tree['init_tree']], ['Insertion Time'])
        plt.show()

        plt.figure(2)
        plt.title('Binary Tree 2nd')
        Show_graph(iterab, [Tree['insert_tree'], Tree['get_tree'], Tree['max_tree'], Tree['delete_tree']  ],
                   ['Random Get', 'Random Delete', 'Find max', 'Random Insert'])
        plt.show()

    return Tree



def Heap_time(iterab, x, Graph=True):
    Heap = {'init_heap': [], 'insert_heap': [], 'max_heap': [], 'deleteM_heap': [],  'final': []}

    for i in iterab:
        mhp = h.HeapMaximum(x[:i])
        ranel = random.choice(x[:i])
        init_heap = timeit.timeit(lambda: h.HeapMaximum(x[:i]), number=10)
        max_heap= timeit.timeit(lambda: mhp.getMax(), number=10)
        deleteM_heap = timeit.timeit(lambda: mhp.delMax(), number=1)
        insert_heap = timeit.timeit(lambda: mhp.insertion(ranel), number=1)
        Heap['init_heap'].append(init_heap)
        Heap['insert_heap'].append(insert_heap)
        Heap['max_heap'].append(max_heap)
        Heap['deleteM_heap'].append(deleteM_heap)
        Heap['final'].append(init_heap + max_heap + deleteM_heap)

    if Graph:  # plot only if it is required
        plt.figure(3)
        plt.subplot(211)
        plt.title('Heap 1st')
        Show_graph(iterab, [Heap_time()['final']], ['Final Time'])
        plt.subplot(212)
        Show_graph(iterab, [Heap['init_heap']], ['Element Insertion'])
        plt.show()

        plt.figure(4)
        plt.title(' Heap 2nd')
        Show_graph(iterab, [Heap['max_heap'], Heap['deleteM_heap']], ['Find Maximum', 'Random delete'])
        plt.show()
    return Heap_time



def Comparisons(Tree_Time, Heap_Time):
    plt.figure(5)

    plt.subplot(311)
    plt.title('Heap compared to Tree')
    Show_graph(iterab, [Tree_Time['final'], Heap_Time['final']], ['Tree final time', 'Heap final time'])

    plt.subplot(312)
    Show_graph(iterab, [Tree_Time['init_tree'], Heap_Time['init_heap']], ['Tree Insertion', 'Heap insertion'])

    plt.subplot(313)
    Show_graph(iterab, [Tree_Time['insert_tree'], Heap_Time['insert_heap']], ['Tree Random Insertion', 'Heap Random Insertion'])

    plt.show()



def Show_graph(iterab, x, lab):
    plt.grid(True)
    plt.xscale('symlog')
    plt.xlim(10, 9000)
    for i in range(len(lab)):
        plt.plot(iterab, x[i], '.-', label=lab[i])
    plt.ylabel('Time')
    plt.xlabel('Len of our list')
    plt.legend(loc='upper left', shadow=True)
    
    
print(Sorting_time(iterab,x), Tree_time(iterab,x), Heap_time(iterab,x))
