# P8-Taxes-Revisited
CS301-8
Program Skills
Using lists of lists
Reusing and improving previously written code
Summary
So, remember Program 3 (Death and Taxes), and how annoying it was to write all of those nested if statements and numbers? This week we're going to revisit that program and make it better.

Program Requirements
For this assignment, you will write five (5) functions with the following names and behaviors:

get_tax_table() - return a list of lists containing tax information. See below for details.
tax(filing_status, income, tax_table) - calculate taxes according to the tax brackets provided in the tax_table. Unlike your P3 function, you may NOT hard-code any tax information in this function; all data must come from tax_table.
is_valid(filing_status, income) - check if the input filing_status and income are valid.
percent_of_income(tax_amount, income) - calculate estimated tax rate as a percent of income.
main(filing_status, income) - uses the three functions above and displays results.
Functions which may be identical to your P3 functions are italicized. Functions which are either new or modified from P3 are bolded. If you do reuse your P3 functions, though, make sure you take any feedback from that assignment into account - this is your chance to improve!

1. Tax table
This function should create and return (not print) a list of lists containing tax information for 2016. You may design the layout of this table yourself, but it must contain this information:

Tax rate	Single filers	Married filing jointly or qualifying widow(er)	Married filing separately	Head of household
10%	Up to $9,275	Up to $18,550	Up to $9,275	Up to $13,250
15%	$9,276 - $37,650	$18,551 - $75,300	$9,276 - $37,650	$13,251 - $50,400
25%	$37,651 - $91,150	$75,301 - $151,900	$37,651 - $75,950	$50,401 - $130,150
28%	$91,151 - $190,150	$151,901 - $231,450	$75,951 - $115,725	$130,151 - $210,800
33%	$190,151 - $413,350	$231,451 - $413,350	$115,726 - $206,675	$210,801 - $413,350
35%	$413,351 - $415,050	$413,351 - $466,950	$206,676 - $233,475	$413,351 - $441,000
39.6%	$415,051 or more	$466,951 or more	$233,476 or more	$441,001 or more
2. Tax calculation
As in program 3, this function returns the amount of tax as an integer that someone with the given filing status and income must pay.

HOWEVER, there are two additional requirements for this function that were not present last time:

This function must not contain any hard-coded numbers. You MUST get the values from your tax_table list-of-lists. If we provide a different tax_table (say, we modify it to contain 2015 values), your function should give different results.
This function must contain no more than 30 lines. (This does not include lines used for whitespace or comments.) Use loops, use variables, but I am challenging you to implement this using something other than a bazillion nested if statements. (Note: my implementation used 17 lines, not including whitespace or comments.)
The exact implementation here will, of course, depend on how your tax_table is set up, but here's the algorithm I implemented in 17 lines:

Figure out which index in your tax_table corresponds to the filing_status, and save this.
Track three things: the amount of income already taxed, the amount of tax calculated so far, and the current tax bracket.
While the income is higher than the cutoff for the current tax bracket:
Calculate how much income you're taxing - cutoff minus amount of income already taxed. Add this to your income taxed so far.
Calculate the tax on that income and add it to the tax calculated so far.
Increase the tax bracket.
Make sure that when you find a tax bracket where the cutoff is higher than the income, that you do your final leftovers calculation for that rate and add it to your calculations so far.
Return the total tax calculated.
When testing this function, remember that it will take an additional argument over P3:

>>> tax('single', 24000, get_tax_table())
=> 3136
>>> tax('married filing jointly', 50000, get_tax_table())
=> 6572
3. Argument validation
May be directly reused from Program 3. See that writeup for details.

4. Percent of income
May be directly reused from Program 3. See that writeup for details.

5. Main function
May be directly reused from Program 3. See that writeup for details.

Sample Output
Literally everything about how this program LOOKS should be exactly the same as P3 (i.e. you should NOT have this program run automatically from the command line):

>>> main('single', 24000)
Tax: $3136
Tax as % of income: 13.066666666666665%
>>> main('married filing jointly', 50000)
Tax: $6572
Tax as % of income: 13.144%
>>> main('married filing separately', 120000)
Tax: $27306
Tax as % of income: 22.755%
>>>
The lines that begin with >>> are your console inputs, calling the take_my_money() function. I've made the text that you'll type bold and blue so you can see it clearly.

NOTICE: The dollar sign ($) and the dollar amount have NO SPACE between them; same with the percentages and the percent sign (%). Try using concatenation to achieve this.

If you run your program with invalid inputs, it should look like this:

>>> main('hello', 100)
Invalid input.
Filing status must be 'single', 'married filing jointly', 'widow(er)', 'married filing separately', or 'head of household'.
Income must be greater than or equal to zero.
>>> main('single', -5)
Invalid input.
Filing status must be 'single', 'married filing jointly', 'widow(er)', 'married filing separately', or 'head of household'.
Income must be greater than or equal to zero.
>>> main('hello', 'hello')
Invalid input.
Filing status must be 'single', 'married filing jointly', 'widow(er)', 'married filing separately', or 'head of household'.
Income must be greater than or equal to zero.
>>>
Commenting Your Code
As with last week's program, every function you write is required to include a docstring, and you must also write comments in your code.

Handing In Your Program
Students completing this program in pairs should join a P8 Group. If you are having trouble joining (not creating!) a P8 Group, please contact Hobbes with your partner's name.

When you're done, upload all functions in a file called taxes_hw2.py.
