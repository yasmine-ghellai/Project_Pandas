import matplotlib.pyplot as plt
import pandas as pd

Données = {"Postes":["DevOps",
                     "data_scientist",
                     "data_scientist","software devloper",
                     "data_scientist","DevOps","software devloper",
                     "software devloper","data_scientist",
                     "data_scientist"],
                     "Salary":[3400,4000,5000,5400,4900,5200,5000,5000,5000,4500],
                     "Nationality":["FR","USA","JP","RU","JP","JP","FR","FR","USA","USA"],
                     "Experience_level":["JR","SR","Mid","JR","Mid","Mid","JR","JR","JR","Mid"]}
tableau = pd.DataFrame(Données)
tableau["Salary__Devise"]= tableau["Salary"].astype(str)
tableau.loc[tableau["Nationality"]=="FR" , "Salary_Devise"]=tableau["Salary__Devise"] + "€"
tableau.loc[tableau["Nationality"] == "JP","Salary_Devise"]=tableau["Salary__Devise"] + "¥"
tableau.loc[tableau["Nationality"]=="RU", "Salary_Devise" ] = "₽" + tableau["Salary__Devise"] 
tableau.loc[tableau["Nationality"] == "USA","Salary_Devise"]= "$" + tableau["Salary__Devise"] 
print(tableau)
moyenne = tableau["Salary"].mean()
median = tableau["Salary"].median()
print("la mediane :", median)
print("la moyenne :", moyenne)
print(tableau.groupby("Postes")["Salary"].mean())
print(tableau["Salary"].value_counts())
print(tableau["Salary"].describe())
print(tableau[(tableau["Nationality"]=="FR") &(tableau["Salary"] > 4000)])
tableau["Salary"].hist(bins=5, edgecolor="blue")
plt.axvline(x=moyenne, color="red" , linestyle="dashed" , label="mean")
plt.axvline(x=median , color="green" , linestyle="solid" , label="mediane" )
plt.title("Bilan des salariés")
plt.xlabel("salaire")
plt.ylabel("employés")
plt.legend()
plt.savefig("first_hist.png")
plt.show()
