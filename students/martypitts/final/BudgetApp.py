
'''
#Title: Budget Application
#Dev:   Anonymous
#Dec 1, 2015
#Description
# This program will create a monthly budget based on a college students
# funding for one year. The idea is to provide something useful for students
# with unique funding needs and help them figure out what a monthly resource
# allocation might look like.
#
# Pseudo code
#   1) Querry student on funding resources.
#   2) Sum funding resources into as budget available.
#   2) Querry student for common expected expenses and store in a list.
#   3) Sum the expenses into an expected expenses.
#   4) Divide the resources by expenses and print montly budget for 9 months. Save to pickle file to obfiscate data from view.

1)	Create a simple example of how you would use Python Exception Handling.
    Make sure to comment your code.
2)	Create a simple example of how you would use Python Pickling.
    Make sure to comment your code.
'''

# Data Code
###### Assets  ######
import pickle, shelve

SavingsTotal = 0 #  Total savings from student
FinancialAidTotal = 0 # Expected financial aid from government
ScholarshipTotal = 0 # Expected grants from private resources
ParentTotal = 0 # Total savings from partents support (includes anyone who is willing to contribute)
OtherTotal = 0 # Other resources not covered above (Student job, selling blood, weekend job etc.)
FundingTotal = 0 # College Funding Resources
objFile = None # File to store results
deficit = True

##### Liabilities #######
HousingTotal = 0
FoodTotal = 0
TuitionTotal = 0
BooksTotal = 0
MedicalTotal = 0
ClothingTotal = 0
HygeneTotal = 0
EntertainTotal = 0
UtilitiesTotal = 0
BankingTotal = 0
InsuranceTotal = 0
OtherTotal = 0

monthlyBuget = 0 # calculated budget
FixedCollegeCosts = 0 # sum tuition and books
FixedHousingCosts = 0 # sum for rent and utilities
VariableCosts = 0 # non fixed costs
RemoveFixedCollegeCost = 0 # budget after removing fixed costs
AssetsAfterFixed = 0 #budget after removing fixed costs
ExpensesAfterFixed = 0# expenses after removing fixed costs
variableMonthlyBudget = 0 # budget after removing fixed costs
BudgetTimeMonths = 10

#  -- processing code --
#  Create a Class to do the following:
#   1) Collect assets available for college
#   2) Collect expected college expenses
#   3) Sum the available funds
#   4) Sum the expected expenses
#   5) Generate budget for each month

class CollegeBudgeting(object):

  # Function to querry student for funding resources
  @staticmethod
  def FundingResources():
    '''
    This section sums the expected resources for the current calender year. The
    following assumptions are made.
      1) The year will run sept. through June.
      2) Querry common resources (savings, expected income, financial aid, parents)
    '''

    print("This section sums the expected resources for the coming year.")
    print("Our first objective is to capture the resources you have for school.")
    print("Please enter the following information to start our budget activity.\n")

    # Querry student for savings, financial aid, scholarships, parents, other
    SavingsTotal = print("How much money do you have in your savings & checking accounts?")
    try:
        SavingsTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        SavingsTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    FinancialAidTotal = print("How much money do you expect from FAFSA (grants + loans)?")
    try:
        FinancialAidTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        FinancialAidTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    ScholarshipTotal = print("How much money do you expect from scholarships?")
    try:
        ScholarshipTotal= float(input("\nEnter a number: "))
    except ValueError as e:
        ScholarshipTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    ParentTotal = print("How much money do you expect from partents, uncles, grandparents, etc.?")
    try:
        ParentTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        ParentTotal = 0
        print("That was not a number! or as python would say...")
        print(e)

    OtherTotal = print("How much money do you expect from other resources not currently accouted for?\n"
                       "Get creative here (Sell blood, Get a Job, Sell shirt off back, etc.)\n"
                       "Who needs stuff when you can expand your mind!!\n")
    try:
        OtherTotal= float(input("\nEnter a number: "))
    except ValueError as e:
        OtherTotal = 0
        print("That was not a number! or as python would say...")
        print(e)

    return(SavingsTotal, FinancialAidTotal,ScholarshipTotal, ParentTotal, OtherTotal)
    # end FundingResoiurces

# Function to Sum all the user fund inputs
  @staticmethod
  def SumFundingResources(SavingsTotal, FinancialAidTotal,ScholarshipTotal, ParentTotal, OtherTotal):
      print("Funding resources for the year = ")
      print("     Bank Accounts =", SavingsTotal)
      print("     Government =", FinancialAidTotal)
      print("     Scholarships =", ScholarshipTotal)
      print("     Parents = ", ParentTotal)
      print("     Other =", OtherTotal)
      FundingTotal = SavingsTotal + FinancialAidTotal + ScholarshipTotal + ParentTotal + OtherTotal
      print("Total Budget = ", FundingTotal)
      return(FundingTotal)
  # end SumFundingResources

# Function Querry Liabilities
  def YearlyExpense():
    '''
    This section querrys for the expected expenses for the current calender year. The
    following assumptions are made.
      1) The year will run sept. through June.
      2) Everything not in querried items is dumped to other
    '''
    print()

    print("This section asks the student about expected expenses.")
    print("Please enter the following information so we can generate a budget.")
    # Querry student for repected expenses
    HousingTotal = print("How much will housing cost for the year (assume Sept. through June)?")
    try:
        HousingTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        HousingTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    # Querry student for repected expenses
    FoodTotal = print("How much will food cost for the year (assume Sept. through June)?")
    print("Ask dad about this one. He might start discussing the boat he could have had.")
    print("Think about beans, rice, bulk purchases then freeze, Costco, Sams, Walmart.")
    try:
        FoodTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        FoodTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    TuitionTotal = print("How much will tuition cost for the year (assume Sept. through June)")
    try:
        TuitionTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        TuitionTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    BooksTotal = print("How much will books cost for the year (assume Sept. through June)?")
    print("Think about computers (and repairs), cell phones (And repairs), Tech Support, Tutors, etc. ")
    try:
        BooksTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        BooksTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    MedicalTotal = print("How much will medical cost for the year (assume Sept. through June)?")
    print("Yes you are a greek god / godess and invincible. Here is an item which could have long lasting impact to family if something happens. ")
    try:
        MedicalTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        MedicalTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    ClothingTotal = print("How much will clothing cost for the year (assume Sept. through June)?")
    print("Goodwill, Salvation Army, Costco, Wallmart are cheap.  Hey you are starving student:)")
    try:
        ClothingTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        CollegeBudgeting = 0
        print("That was not a number! or as python would say...")
        print(e)
    HygeneTotal = print("How much will hygene cost for the year (assume Sept. through June?)")
    print("When mom and dad come to visit soap comes in handy, so feel free to pad this line item.")
    try:
        HygeneTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        HygeneTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    EntertainTotal = print("How much will Entertainment cost for the year (assume Sept. through June?)")
    print("You will want to have fun in school. Pizza, movies, clubs, etc.")
    try:
        EntertainTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        EntertainTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    UtilitiesTotal = print("How much will utilities cost for the year (assume Sept. through June?)")
    print("Garbage, Lights, Gas, Cleaning Service")
    try:
        UtilitiesTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        UtilitiesTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    BankingTotal = print("How much will banking cost for the year (assume Sept. through June?)")
    print("Credit Unions are a good option.")
    try:
        BankingTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        BankingTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    InsuranceTotal = print("How much will renters, car insurance cost for the year (assume Sept. through June?)")
    try:
        InsuranceTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        InsuranceTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    OtherTotal = print("What other items will cost money for the year (car, hobbies, study abroad) (assume Sept. through June?)")
    try:
        OtherTotal = float(input("\nEnter a number: "))
    except ValueError as e:
        OtherTotal = 0
        print("That was not a number! or as python would say...")
        print(e)
    return(HousingTotal, FoodTotal,TuitionTotal,BooksTotal,MedicalTotal,ClothingTotal,HygeneTotal,EntertainTotal,UtilitiesTotal,BankingTotal,InsuranceTotal,OtherTotal)
  # end YearlyExpense

# Function to Sum all the student yearly expenses
  @staticmethod
  def SumExpenses(HousingTotal, FoodTotal,TuitionTotal,BooksTotal,MedicalTotal,ClothingTotal,HygeneTotal,EntertainTotal,UtilitiesTotal,BankingTotal,InsuranceTotal,OtherTotal):
      print("Total Expenses for the year = ")
      print("      Housing =",  HousingTotal)
      print("      Food =",  FoodTotal)
      print("      Tuition =",  TuitionTotal)
      print("      Books =",  BooksTotal)
      print("      Medical =",  MedicalTotal)
      print("      Clothing =",  ClothingTotal)
      print("      Hygene =",  HygeneTotal)
      print("      Entertainment =",  EntertainTotal)
      print("      Utilities =",  UtilitiesTotal)
      print("      Banking =",  BankingTotal)
      print("      Insurance =",  InsuranceTotal)
      print("      Other =",  OtherTotal)
      TotalExpenses = HousingTotal + FoodTotal + TuitionTotal + BooksTotal + MedicalTotal + ClothingTotal + HygeneTotal + EntertainTotal + UtilitiesTotal + BankingTotal + InsuranceTotal + OtherTotal
      print(" Total Expenses =", TotalExpenses)
      return(TotalExpenses)
  # end SumExpenses

# Now Dump Out the monthly budget
  @staticmethod
  def DumpMonthlyBudget(FundingTotal, TotalExpenses, BudgetTimeMonths):
      deficit = True
      monthlyBuget = TotalExpenses / BudgetTimeMonths
      monthlyIncome = FundingTotal / BudgetTimeMonths
      monthlyBugetMargin = (FundingTotal - TotalExpenses) / BudgetTimeMonths
      print("Total expenses per month  =", monthlyBuget)
      print("Total budget available per months =", monthlyIncome)
      if monthlyBugetMargin < 0:
         defict = True
         print()
         print("########## Results and suggestions: ###################")
         print("So you need an additional", abs(monthlyBugetMargin), "per month. Do not worry! Check out the following links.")
         print("    Get a scholarship.")
         print("         http://www.thewashboard.org/login.aspx")
         print("         http://www.state.gov/m/dghr/flo/c21963.htm")
         print("         http://www.wsac.wa.gov/")
         print("    Get a part time Job. Here is a place to start.")
         print("         http://www.manpower.com/?utm_source=google&utm_medium=local&utm_campaign=google-local")
         print("         https://fortress.wa.gov/esd/worksource/Employment.aspx?CurrentPage=Employment")
         print("    Hate having a boss. Start a small business.")
         print("         https://www.entreleadership.com/")
         print("         https://www.sba.gov/offices/headquarters/wbo")
         print("         http://www.crowdsource.com/how-it-works/")
         print("    Start a croud sourcing campaign.")
         print("         https://www.gofundme.com/")
         print("         https://www.indiegogo.com/")
      elif monthlyBugetMargin < 200:
         deficit = False
         print()
         print("########## Results and suggestions: ###################")
         print("Congratulations you created a buget which balances! Your monthly surplus is", monthlyBugetMargin,".")
         print("Think about additional income sources in case of unexpected events.")
         print("    Start a savings investment account. Here are videos on the most powerful force in the world (Albert Einstein")
         print("    https://www.youtube.com/watch?v=RqHfESOrwMU")
         print("    https://personal.vanguard.com/us/openaccount?CompLocation=GlobalHeader&Component=OpenAccount")
         print("    https://investor.vanguard.com/mutual-funds/index-funds?WT.srch=1")
      else:
         deficit = False
         print()
         print("########## Results and suggestions: ###################")
         print("Congratulations you made a budget with a healthy projected surplus. Your surplus is", monthlyBugetMargin, "per month.")
         print("You have planned for this event. Good job, now verify your numbers and make sure they make sense. Do a 'what if'? analysis.")
         print()
         print("Start thinking about how to grow a nest egg. Watch out for sharks! Here are a couple ideas.")
         print("    https://www.youtube.com/watch?v=S98O2gFBEPo")
         print("    https://www.tdameritrade.com/home.page")
      return(monthlyBuget,monthlyBugetMargin,monthlyIncome,deficit)
  # end DumpMonthlyBudget

# Write Pickle File using this function which stores data for assets, liabilities, and calculated statistics
  @staticmethod
  def SaveBudgetPickleFile(dumpAssets,dumpExpenses, dumpStatistics):
    try:
      objFile = open("Budget.dat", "wb+")
      print("Here is the current budget file:")
      pickle.dump(dumpAssets,objFile)
      pickle.dump(dumpExpenses,objFile)
      pickle.dump(dumpStatistics,objFile)
      objFile.close()
    except Exception as e:
      print("There was a unexpected error!")
      print("pythons error info: ")
      print(e.__str__())
    finally:
      if objFile != None:
        objFile.close()
    # End try except

  # Read Pickle File  this function which retrives data for assets, liabilities, and calculated statistics
  @staticmethod
  def ReadBudgetPickleFile():
    try:
      objFile = open("Budget.dat", "rb")
      print("Here is the previous budget file:")
      readAssetsPickle = pickle.load(objFile)
      readExpensesPickle = pickle.load(objFile)
      readStatistics = pickle.load(objFile)
      objFile.close()
      return(readAssetsPickle, readExpensesPickle, readStatistics)
    except Exception as e:
      print("There was a unexpected error!")
      print("pythons error info: ")
      print(e.__str__())
    finally:
      if objFile != None:
        objFile.close()
    # End try except
# End Class

# Presentation Code
print("*************************** Welcome **************************************")
print("You have started the college budget tool.")
print("The idea is to define what assets you have ")
print("for school, the liabilities, and monthly expenses.")
print("***************************************************************************")

SavingsTotal, FinancialAidTotal,ScholarshipTotal, ParentTotal, OtherTotal= CollegeBudgeting.FundingResources()
FundingTotal = CollegeBudgeting.SumFundingResources(SavingsTotal, FinancialAidTotal,ScholarshipTotal, ParentTotal, OtherTotal)
HousingTotal, FoodTotal,TuitionTotal,BooksTotal,MedicalTotal,ClothingTotal,HygeneTotal,EntertainTotal,UtilitiesTotal,BankingTotal,InsuranceTotal,OtherTotal = CollegeBudgeting.YearlyExpense()
TotalExpenses = CollegeBudgeting.SumExpenses(HousingTotal, FoodTotal,TuitionTotal,BooksTotal,MedicalTotal,ClothingTotal,HygeneTotal,EntertainTotal,UtilitiesTotal,BankingTotal,InsuranceTotal,OtherTotal)

# Print out statistics and budget
print()
print("########## Budget Summary Below: ###################")
print("The total expected funding =", FundingTotal)
print("The total expected expenses =", TotalExpenses)
[monthlyBuget,monthlyBudgetMargin,monthlyIncome,deficit] = CollegeBudgeting.DumpMonthlyBudget(float(FundingTotal), float(TotalExpenses),BudgetTimeMonths)
print("Deficit =", deficit)
FixedCollegeCosts = TuitionTotal + BooksTotal
print()
print("########## Budget Analysis Below: ###################")
print("Note: Fixed costs are expenses which are non negotiable.")
print("Fixed College Costs (Tuition and Books) =", FixedCollegeCosts)
FixedHousingCosts = HousingTotal + UtilitiesTotal
print("Fixed Housing Costs (Housing and Utilities) =", FixedHousingCosts)
print()
VariableCosts = abs(TotalExpenses - (FixedCollegeCosts + FixedHousingCosts))
print("Note: Variable costs are expense where you might have some control. For example buy light beer vs. IPA. Life is a big trade study.")
print("Variable Costs (Food, Medical, Clothing, Hygene, Entertainment, Banking, Insurance, Other Category) =", VariableCosts)
print()
print("################################## Remove the fixed costs for tuition and books. ######################################")
print("Living expenses equal Total Expenses minus tuition and books.")
# Assets - Liabilities without housing
RemoveFixedCollegeCost =  (FundingTotal - (TotalExpenses - FixedCollegeCosts)) / BudgetTimeMonths
# print("FundingTotal =", FundingTotal, "TotalExpense=", TotalExpenses, "FixedCollegeCosts =",FixedCollegeCosts, "RemoveFixedCollegeCost=", RemoveFixedCollegeCost)
LifExpenses = monthlyIncome - RemoveFixedCollegeCost
if deficit == True:
  print("Monthly college defict for life expense after removing expected tuition and books =", RemoveFixedCollegeCost)
else:
  print("Monthly college surplus for life expense after removing expected tuition and books =", RemoveFixedCollegeCost)

print()
print("###################### Remove the fixed costs for tuition and books and housing(rent) and utilities. ##################")
AssetsAfterFixed = FundingTotal - FixedCollegeCosts - FixedHousingCosts
ExpensesAfterFixed = TotalExpenses - FixedCollegeCosts - FixedHousingCosts
print("Budget after removing expected fixed college and housing costs =", AssetsAfterFixed)
print("Expenses after removing expected fixed college and housing costs = ", ExpensesAfterFixed)

# print()
# print("######################### This is your calculated budget for each month after fixed costs. #############################")
# [monthlyBuget,monthlyBudgetMargin,monthlyIncome,deficit] = CollegeBudgeting.DumpMonthlyBudget(float(AssetsAfterFixed), float(ExpensesAfterFixed),BudgetTimeMonths)

dumpAssets = (SavingsTotal, FinancialAidTotal,ScholarshipTotal, ParentTotal, OtherTotal)
dumpExpenses = (HousingTotal, FoodTotal,TuitionTotal,BooksTotal,MedicalTotal,ClothingTotal,HygeneTotal,EntertainTotal,UtilitiesTotal,BankingTotal,InsuranceTotal,OtherTotal)
dumpStatistics = (monthlyBuget, FixedCollegeCosts, FixedHousingCosts, VariableCosts, RemoveFixedCollegeCost, AssetsAfterFixed, ExpensesAfterFixed, variableMonthlyBudget)

# ask user if they would like to save a data file
strUserInputItem1 = input("Would you like to save information to Budget.dat? Enter: Choice or (Yes/No)")
if strUserInputItem1.lower() == "yes":
  CollegeBudgeting.SaveBudgetPickleFile(dumpAssets,dumpExpenses, dumpStatistics)
elif strUserInputItem1.lower() == "no":
  strUserInputItem2 = input("Would you like to read information from prior budget Budget.dat? Enter: Choice or (Yes/No)")
  if strUserInputItem2.lower() == "yes":
    dumpAssets,dumpExpenses, dumpStatistics = CollegeBudgeting.ReadBudgetPickleFile()
    # Saved Assets
    print("Saved assets from file are = ", "Savings=",dumpAssets[0], "Financial Aid=",dumpAssets[1],"Scholarship=", dumpAssets[2],"Parents=",dumpAssets[3],"Other=",dumpAssets[4])
    print("Saved expenses from file are =", dumpExpenses)
    print("Saved Statistics from file are = ")
    # Saved calculated statistics
    print("   Monthly Budget=",dumpStatistics[0])
    print("   Fixed College Costs=", dumpStatistics[1])
    print("   Fixed Housing =",dumpStatistics[2])
    print("   Variable Costs=",dumpStatistics[3])
    print("   Removed Fixed Cost =",dumpStatistics[4])
    print("   Assets - Fixed Cost=",dumpStatistics[5])
    print("   Expenses After Fixed=",dumpStatistics[6])
    print("   Variable Monthly Budget", dumpStatistics[7])
    # Saved Expenses
    print("Housing Total=",dumpExpenses[0])
    print("FoodTotal=", dumpExpenses[1])
    print("TuitionTotal=",dumpExpenses[2])
    print("BooksTotal=",dumpExpenses[3])
    print("MedicalTotal=",dumpExpenses[4])
    print("ClothingTotal=",dumpExpenses[5])
    print("HygeneTotal=",dumpExpenses[6])
    print("EntertainTotal=",dumpExpenses[7])
    print("UtilitiesTotal=",dumpExpenses[8])
    print("BankingTotal=",dumpExpenses[9])
    print("InsuranceTotal=",dumpExpenses[10])
    print("OtherTotal=",dumpExpenses[11])
  # end if
# end if

