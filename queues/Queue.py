class Queue:
    def __init__(self):
        self.items = [];
    
    # is-empty operation
    def is_empty(self):
        return self.items ==[];
    
    # enqueue
    def enqueue(self, item):
        self.items.insert(0, item);
    
    # denqueue

    def denqueue(self):
        return self.items.pop();

    # size
    def size(self):
        return len(self.items);


def hot_potato(name_list, num):
    sim_queue = Queue()

    for name in name_list:
        sim_queue.enqueue(name);

    while sim_queue.size() > 1:

        for i in range(num):
            sim_queue.enqueue(sim_queue.denqueue());
        sim_queue.denqueue()
        
    return sim_queue.denqueue();

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent",
"Brad"], 7))