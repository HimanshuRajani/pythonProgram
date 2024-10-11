print("20 pip challange ")

level = input(" Enter your current level:- ")
curr_bal = input(" enter the current account balance:- ")
risk23 = (int(curr_bal) * 0.23)
val = risk23/15
val_2 = float(format(val,".2f"))
lot_size = val_2*0.1
real_risk = lot_size*10*15
profit = lot_size*10*20

print("23% risk is ", risk23)
print("the lot size you have to consider at max ",  format(lot_size,".2f"))
print("balance after you win the trade $",  (int(curr_bal) + profit))
print("balance after you loss the trade $", (int(curr_bal) - real_risk))