from suffix_tree import Tree
import sys, getopt

def main (argv):

    if len(argv) < 2:
        print(argv[0] + " <text file>")
        sys.exit()
        
    ifile = open(argv[1], "r")
 
    data = ifile.read()
 
    ifile.close()

    # Suffix tree
    sys.stderr.write("Building the suffix tree ... ")
    sys.stderr.flush()
    st = Tree ({ 'data' : data })
    sys.stderr.write("Done.\n")
    sys.stderr.flush()
    
    sys.stderr.write("Building the balanced parenthises sequence ... ")
    sys.stderr.flush()
    st.parentheses2()
    sys.stderr.write("Done.\n")
    sys.stderr.flush()
    
        

if __name__ == "__main__":
    main(sys.argv)

