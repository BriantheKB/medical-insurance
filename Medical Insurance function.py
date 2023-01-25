# So I learned alot about functions and this is how i learned to get the indivudual calculate_insurance_cost() with the function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12
  print("The estimated insurance cost for "  + name + " is " + str(estimated_cost) + " dollars.")
  print(estimated_cost)
  return estimated_cost


# Estimate Jef's insurance cost
jef_insurance_cost = calculate_insurance_cost(name = "Jef", age = 41, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 0)


# Estimate Brian's insurance cost 
brian_insurance_cost = calculate_insurance_cost(name = "Brian", age = 42, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)



