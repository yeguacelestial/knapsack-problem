# Input -> * Knapsack Weight (ksw)
#       -> * 'i' element weight (wi)
#       -> * 'i' element value (vi)
#       -> * number of items (n)
#       -> * pelos.dat file
# Output -> Objective function (objF)
#        -> Number of items (nItems)

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