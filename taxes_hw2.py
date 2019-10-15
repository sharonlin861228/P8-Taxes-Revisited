def get_tax_table():
  ''' the table contains the information of tax'''
  return [[['single'], [0, 9275, 37650, 91150, 190150, 413350, 415050]], [['married filing jointly', 'widow(er)'], [0, 18550, 75300, 151900, 231450, 413350, 466950]], [['married filing separately'], [0, 9275, 37650, 75950, 115725, 206675, 233475]], [['head of household'], [0, 13250, 50400, 130150, 210800, 413350, 441000]], [0, 0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]]


def tax(filing_status, income, tax_table):
  """This function is to count the tax with the status and income that user provides, and the tax table. """
  tax_rate = tax_table[-1]
  table = tax_table[:-1]

  index = 0
  while True: # select the status to collect the tax range
    if filing_status in table[index][0]:
      tax_range = table[index][1]
      break
    index += 1

  # use the income to calculate the tax with tax information
  result = 0
  index = 1
  while index < len(tax_range):
    if income < tax_range[index]:
      result += (income-tax_range[index-1]) * tax_rate[index]
      break
    else:
      result += (tax_range[index]-tax_range[index-1]) * tax_rate[index]
    index += 1

  if income > tax_range[-1]:
    result += (income-tax_range[-1]) * tax_rate[-1]

  return int(result)

def is_valid(filing_status, income):
  """ This function is to test if the user type the right thing, such as status and income."""
  if filing_status in ( 'single', 'married filing jointly', 'widow(er)', 'married filing separately', 'head of household') and isinstance(income, int) and income > 0 :
    return True
  else:
    return False

def percent_of_income(tax_amount, income):
  """The function is for counting the percent of tax in income"""
  result = (float(tax_amount*100))/(float(income))
  return result


  """This function is the combinaion of all the functions above. If the first function is valid, the main function will progress successfully. However, if the user type something invalid, the main function will print and tell the user he or she types something invalid. The function also print the tax and calculate the percentage of the tax in income."""

def main(filing_status, income):
  if is_valid(filing_status, income) == True:
    tax1 = tax(filing_status, income, get_tax_table())
    print "Tax:$", tax1

    print "Tax as % of income:", str(percent_of_income(tax1, income)) + "%"
  else:
    print "Invalid input."
    print "Filing status must be 'single', 'married filing jointly', 'widow(er)', 'married filing separately', or 'head of household'."
    print "Income must be greater than or equal to zero."
