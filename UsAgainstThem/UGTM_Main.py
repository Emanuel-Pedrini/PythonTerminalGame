from UGT_Mains.UGTM_HealthClass import cUGT_Health

f = cUGT_Health(100, 100, 0)
x = f.fInt_ReduceHealth(30)
y = f.fInt_IncreaseHealth(10)
f.fInt_ChangeMaximumHealth(+50)
print(y, f.iInt_ActualHealth, f.iInt_MaximumHealth)
