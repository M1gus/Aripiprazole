structures = c("aripiprazole","rotenone","piericidin", "ubiquinone")
deltaG = c(-10.7, -10.8,-9.1, -11.3)
df = data.frame(structures = structures, deltaG = deltaG)

# Formula: Ki = exp (deltaG/ (R*T)
# for binding: deltaG(binding) = -R*T*ln Kb 
# Reference: http://autodock.scripps.edu/faqs-help/faq/how-autodock-4-converts-binding-energy-kcal-mol-into-ki
# deltaG = X kcal/mol
temp=298.15#K
R = 0.001986#kcal/mol-K

df$Kb = exp(-df$deltaG/ (R*temp))
df
