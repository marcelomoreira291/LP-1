
funcionário = {
    "nome" : "José",
    "matrícula" : 1223766,
    "salário" : 989.0,
    "ferias" : True, #faltava uma vírgula
    "horas_extras" : 3
}

rem = funcionário.pop("ferias") # argumento funcionario != funcionário 
print(funcionário) 
print(rem)

del funcionário["nome"] 
print(funcionário) 


