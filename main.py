#function with the inputs
import pandas

def main(args):
  if 'country' in args:
     country = args.get('country')
     if country != 'United States' or 'Brazil' or 'LATAM' or 'India' or 'Turkey' or 'Australia' or 'Scandinavia' or 'ASEAN' or 'Japan' or 'Italy' or 'South Africa' or 'France' or 'United Kingdom' or 'South Korea' or 'Middle East' or 'Germany' or 'Canada' or 'United States':
       country = 'United States';
  else:
    country = 'United States';
  if 'industry' in args:
    industry = args.get('industry')
    if industry != 'Health' or 'Hospitality' or 'Media' or 'Retail' or 'Research' or 'Communications' or 'Consumer' or 'Transportation' or 'Education' or 'Entertainment' or 'Industrial' or 'Services' or 'Energy' or 'Technology' or 'Pharmaceuticals' or 'Financial' or 'Public':
      industry = 'Global average'
  else:
    industry = 'Global average'   
  if 'employees' in args:
    employees = int(args.get('employees'))
    if employees < 500: 
      employees = 'Less than 500 employees'
    elif employees >= 500 and employees <= 1000: 
      employees = '500 to 1000 employees'
    elif employees >= 1001 and employees <= 5000: 
      employees = '1001 to 5000 employees'
    elif employees >= 5001 and employees <= 10000: 
      employees = '5001 to 10000 employees'
    elif employees >= 10001 and employees <= 25000: 
      employees = '10001 to 25000 employees'
    elif employees >= 2500: 
      employees = 'More than 25000 employees'
    else:
      employees = 'Average'
  else:
      employees = 'Average'
  
  df3 = pandas.read_csv('ATC.csv')
  df6 = pandas.read_csv('TC.csv')
  df7 = pandas.read_csv('TCH.csv')

  F2021 = df3.loc[df3.Country == country, 'FY2021'].item()
  F2021I = df6.loc[df6.Industry == industry, '%Total'].item()
  HeadcountShare = df7.loc[df7.Conditions == employees, 'MarketShare'].item()
  F2021Ind = F2021I * F2021 * 0.01; 
  
  COB = round(F2021Ind * HeadcountShare * 0.01 * 1000000); 

  
  return {"COB": COB}

dict = {}
print(main(dict))