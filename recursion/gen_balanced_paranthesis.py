n = int(input().strip())
out_str, op1, op2 = "", "", ""
open_p, closed_p = n, n
res = []

def balanced_parans(out_str, open_p, closed_p):
    if open_p == 0 and closed_p == 0:
        res.append(out_str)
        out_str = ""
        return
    elif open_p and closed_p and closed_p == open_p:
        op1 = out_str + '('
        open_p -= 1
        balanced_parans(op1, open_p, closed_p)
    elif open_p and closed_p and closed_p > open_p:
        op1 = out_str + '('
        temp1 = open_p
        temp1 -= 1
        balanced_parans(op1, temp1, closed_p)
        op2 = out_str + ')'
        temp2 = closed_p
        temp2 -= 1
        balanced_parans(op2, open_p, temp2)
    elif open_p == 0 and closed_p != 0:
        out_str = out_str + ')'
        closed_p -= 1
        balanced_parans(out_str, open_p, closed_p)
    elif open_p != 0 and closed_p == 0:
        out_str = out_str + '('
        open_p -= 1
        balanced_parans(out_str, open_p, closed_p)

balanced_parans(out_str, open_p, closed_p)
print(res)