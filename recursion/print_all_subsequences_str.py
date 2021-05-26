string = input().strip()
res = set()
out_str = ""

def all_subsets(string, out_str):
    if len(string) == 0:
        res.add(out_str)
        return
    
    op1 = out_str
    op2 = out_str + string[0]
    string = string[1:]
    all_subsets(string, op1)
    all_subsets(string, op2)


all_subsets(string, out_str)
print(res)
