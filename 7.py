from anytree import Node, RenderTree, findall, Resolver

def count_bags(node):
    return sum(int(child.bag_value) + int(child.bag_value) * int(count_bags(child)) for child in node.children)

def main():
   # part 1
   print("# part1:")
   f = open("input7.txt", "r")
   lines = f.readlines()
   f.close()
   root = Node("root")

   # generate first level
   for n_line, line in enumerate(lines):
      splited_line = line.replace("\n","").split(" contain ")
      Node(splited_line[0].strip().replace("bags", "bag").replace(".", ""), parent=root, bag_value=0)


   # generate n-th levels
   for pre, fill, node in RenderTree(root):
      for n_line, line in enumerate(lines):
         splited_line = line.replace("\n","").split(" contain ")
         if(node.name in splited_line[0]):
            desc = splited_line[1].split(",")
            for d in desc:
               d_value = ''.join([i for i in d if i.isdigit()]).strip()
               #if(len(d_value) == 0): d_value = 0
               d_name = ''.join([i for i in d if not i.isdigit()]).strip()
               d_name = d_name.replace("bags", "bag").replace(".", "")
               if(d_name not in "no other bag"):
                  Node(d_name, parent=node, bag_value=d_value)
         

   #print the tree
   # for pre, fill, node in RenderTree(root):
   #   print("%s%s" % (pre, node.name))

   results = []
   for pre, fill, node in RenderTree(root, maxlevel=2):
         finds = findall(node, filter_=lambda n: "shiny gold" in n.name)
         if(len(finds) > 0): results.append(finds)
   
   print("total part1 :", len(results) - 2)

   #part 2

   r = Resolver('name')
   shiny_gold_bag_node = r.get(root, "shiny gold bag")
   shiny_gold_bag_node.bag_value = 1
   # print the tree
   # for pre, fill, node in RenderTree(shiny_gold_bag_node):
   #    print("%s%s(%s)" % (pre, node.name, node.bag_value))
   print("total part2 :", count_bags(shiny_gold_bag_node))

if __name__ == "__main__":
    main()