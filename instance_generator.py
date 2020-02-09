# Requirements:
# Input -> * Size of Instance (n)
#       -> * Min Value (min_v)
#       -> * Max Value (max_v)
#       -> * Min Weight (min_w)
#       -> * Max Weight (max_w)

# Output -> * | 'i' Column | 'Vi' Column | 'Wi Column'

from random import randint
import sys
from sys import argv

def main():
    try:
        n = int(sys.argv[1])
        min_v = int(sys.argv[2])
        max_v = int(sys.argv[3])
        min_w = int(sys.argv [4])
        max_w = int(sys.argv[5])
        instance(n, min_v, max_v, min_w, max_w)

    except ValueError:
        print("[-] Error: values must be integers.")
    
    except IndexError:
        print("[-] Error: One or more arguments are missing!")

    except Exception as e:
        print(f"[*] Usage: instance_generator.py <instance-size> <min-value> <max-value> <min-weight> <max-weight>")

# Instance generator function
def instance(n=0, min_v=0, max_v=0, min_w=0, max_w=0):
    if n == 0 or max_v == 0 or max_w == 0:
        print("[-] Instance won't be generated with 0 on KS Size or maximum values.")
        exit

    elif type(n) is not int is True:
        print("[-] Instance size must be an integer value.")
        exit

    elif type(min_v) is str or type(max_v) is str or type(min_w) is str or type(max_w) is str:
        print("[-] Values can't be string type.")
    
    else:
        #print(f'[+] Values\nn={n}\nmin_v={min_v}\nmax_v={max_v}\nmin_w={min_w}\nmax_w={max_w}')
        index_list = []
        w_list = []
        v_list = []
        [w_list.append(randint(min_w, max_w)) for i in range(0, n)]
        [v_list.append(randint(min_v, max_v)) for i in range(0, n)]
        [index_list.append(i) for i in range(1, n+1)]
        
        #print(f'[+] Generated lists:\ni: {index_list}\nW: {w_list}\nV: {v_list}')
        #print (tabulate([["value1", "value2", "value3"], ["value3", "value4", "value3"]], ["i", "W", "V"], tablefmt="grid"))
        
        # Pretty table
        f = open('pelos.dat', 'w+')
        sys.stdout = f

        titles = ['i', 'Wi', 'Vi']
        data = [titles] + list(zip(index_list, w_list, v_list))

        for i, d in enumerate(data):
            line = '|'.join(str(x).ljust(10) for x in d)
            print(line)
            if i == 0:
                dash = '-' * len(line)
                print(dash)
        
        sys.stdout = orig_stdout
        f.close()

        f = open('pelos.dat', 'r')
        print(f.read())

if __name__ == '__main__':
    main()