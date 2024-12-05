


def read_solve():
    safe_reports_sum = 0
    
    
    with open('input.txt', 'r') as file:
        for line in file:
            safe = True
            numeros_linea = list(map(int, line.split()))
            
            for i in range (1, len(numeros_linea)):
                diff = numeros_linea[i] - numeros_linea [i-1]
                
                # First iteration, select incr or decr
                if i == 1 and diff > 0 :
                    incr = True
                if i == 1 and diff < 0 :
                    incr = False
                
                if incr:
                    if diff < 1 or diff > 3:
                        safe = False; break
                else:
                    if diff > -1 or diff < -3:
                        safe = False; break
              
            if safe:
                safe_reports_sum += 1                
            
                
    return safe_reports_sum

res = read_solve()
    
print(f'Num of safe reports : {res}')