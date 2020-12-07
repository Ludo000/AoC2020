from parse import *

from anytree import Node, RenderTree, AsciiStyle, findall, PostOrderIter, PreOrderIter

def part1():
   # part 1
   print("# part1:")
   f = open("input7.txt", "r")
   lines = f.readlines()
   f.close()
   root = Node("root")

   # generate first level
   for n_line, line in enumerate(lines):
      splited_line = line.replace("\n","").split(" contain ")
      Node(splited_line[0].strip(), parent=root)


   # generate n-th levels
   for pre, fill, node in RenderTree(root):
      for n_line, line in enumerate(lines):
         splited_line = line.replace("\n","").split(" contain ")
         if(node.name in splited_line[0]):
            desc = splited_line[1].split(",")
            for d in desc:
               d_value = ''.join([i for i in d if i.isdigit()]).strip()
               d_name = ''.join([i for i in d if not i.isdigit()]).strip()
               Node(d_name, parent=node, value=d_value)

   #print the tree
   for pre, fill, node in RenderTree(root):
     print("%s%s" % (pre, node.name))

   results = []
   for pre, fill, node in RenderTree(root, maxlevel=2):
         finds = findall(node, filter_=lambda n: "shiny gold" in n.name)
         if(len(finds) > 0): results.append(finds)
   
   for k in results:
      print(k)
   print(len(results))


def part2():
   # part 2
   print("# part2:")




def main():
   part1()
   part2()

if __name__ == "__main__":
    main()