# Input -> * Knapsack Weight (ksw)
#       -> * 'i' element weight (wi)
#       -> * 'i' element value (vi)
#       -> * number of items (n)
#       -> * pelos.dat file
# Output -> Objective function (objF)
#        -> Number of items (nItems)

# Read file
wi = []
vi = []

def read_file(file):
    global wi
    global vi

    def columns(list_name, index):
        with open(f'{file}') as f:
            for line in f:
                parts = line.split()
                if len(parts) > 1:
                    list_name.append(parts[index])
            list_name.pop(0)

        list_name_copy = []

        for element in list_name:
            element = list(element)
            element.pop(0)
            element = int("".join(element))
            list_name_copy.append(element)

        list_name = list_name_copy

        return list_name
        
    # 'Wi' list
    wi = columns(wi, 1)
    
    # 'Vi' list
    vi = columns(vi, 2)

    print(f"wi = {wi}\nvi = {vi}")


def knapsack(ksw, wi, vi, n):
    K = [[0 for x in range(ksw+1)] for x in range(n+1)]

    # Build table K[][] in bottom-up manner
    for i in range(n+1):
        for w in range(ksw+1):

            # Base case
            if i==0 or w==0:
                K[i][w] = 0
            
            # Other cases
            elif wi[i-1] <= w:
                K[i][w] = max(vi[i-1] + K[i-1][w-wi[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
            
    return print(f'[+] Number of items: {n}\n[+] Objective function: {K[n][ksw]}')