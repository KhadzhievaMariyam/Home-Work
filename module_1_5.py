immutable_var = 1,2,[35, 17],True,"integer"
print(immutable_var)
#immutable_var[0]=12
#print(immutable_var)
# Изменить значения элементов кортежа нельзя, потому что кортеж не поддерживает обращение по элементам
mutable_list=[1,2,"string"]
mutable_list[0]=2
print(mutable_list)
