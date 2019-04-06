import os
import csv
os.chdir('../input')
pId = []
# Use the csv function to store the csv file with product information (Product ID, Department ID, etc) as a list of list of string
with open('products.csv', newline = '', encoding = 'utf8', errors = 'ignore') as csvfile:
        productId = csv.reader(csvfile)
        for row in productId:
            pId.append(row)
# Use a dictionary to store the product ID with the corresponding department ID from the stored pId list of list of string, product ID is key, department ID is value
# Try and except structure is used here to deal with the case that product ID or/and department ID is/are not integer
# Also the first non-replicate product ID is considered right here, if any replicate product ID appears, an error information will be printed
proDepart = {}
for i in range (1, len(pId)):
    try:
        proId = int(pId[i][0])
    except ValueError:
        print ('Please enter an integer as product ID at row No.', i,', make sure the department ID is in the correct form in this row')
        continue
    try:
        depId = int(pId[i][len(pId[i]) - 1])
    except ValueError:
        print ('Please enter an integer as department ID at row No.', i)
        continue
    if proId not in proDepart:
        proDepart[proId] = int(depId)
    elif proId in proDepart:
        print('Please check the product ID at row No.', i,', replicate product ID')
# Open the order information csv here and use the pId dictionary to get the department information about all the products in the csv
# Try and except used here to show the information about non-integer product ID
# Result dictionary contains department ID as key, and a two-element integer list as value, the first element in the list is the total order number, and the second number is the first order number
# Count is to be used as the row index in this case, number is corresponding to the csv file row number
# If multiple csv data needs to be calculated as a sum, just simply run this part of the code multiple times
result = {}
with open('order_products__prior.csv', newline = '', encoding = 'utf8', errors = 'ignore') as csvfile:
    opp = csv.reader(csvfile)
    header = next(opp)
    count = 2
    for row in opp:
        try:
            key = int(row[1])
        except ValueError:
            print ('Please enter an integer as product ID at row No.', count)
            count += 1
            continue
        # Check the department ID first if it is in the dictionary proDepart
        if key in proDepart:
            depId = proDepart.get(key)
            # Check the department ID if it is already in the result dictionary
            if depId not in result:
                # Check the first order index, check if it is an integer first
                try:
                    firstOrder = int(row[len(row) - 1])
                except ValueError:
                    print ('Please enter 0 or 1 as first Order at row No.', count)
                    count += 1
                    continue
                # Now check if  the first order index is 0 or 1 or not 0 or 1, if neither 0 nor 1, print error
                if firstOrder == 0:
                    result[depId] = [0,0];
                    result[depId][1] = 1;
                elif firstOrder == 1:
                    result[depId] = [0,0];
                    result[depId][1] = 0;
                elif firstOrder is not 0 and firstOrder is not 1:
                    print ('Invalid first order index at row No.', count)
                    count += 1
                    continue
                result[depId][0] = 1;
            # If the department ID is already in the result dictionary
            else:
                result.get(depId)[0] = result.get(depId)[0] + 1
                try:
                    firstOrder = int(row[len(row) - 1])
                except ValueError:
                    print ('Please enter 0 or 1 as first Order at row No.', count)
                    count += 1
                    continue
                if firstOrder == 0:
                    result[depId][1] = result.get(depId)[1] + 1
                elif firstOrder is not 0 and firstOrder is not 1:
                    print ('Invalid first order index at row No.', count)
                    count += 1
                    continue
        else:
            print('The Product ID number', key,'at row No.', count, 'is not in the products file, please double check')
        count += 1
# Repeat the process for the train csv file
with open('order_products__train.csv', newline = '', encoding = 'utf8', errors = 'ignore') as csvfile:
    opp = csv.reader(csvfile)
    header = next(opp)
    count = 2
    for row in opp:
        try:
            key = int(row[1])
        except ValueError:
            print ('Please enter an integer as product ID at row No.', count)
            count += 1
            continue
        # Check the department ID first if it is in the dictionary proDepart
        if key in proDepart:
            depId = proDepart.get(key)
            # Check the department ID if it is already in the result dictionary
            if depId not in result:
                # Check the first order index, check if it is an integer first
                try:
                    firstOrder = int(row[len(row) - 1])
                except ValueError:
                    print ('Please enter 0 or 1 as first Order at row No.', count)
                    count += 1
                    continue
                # Now check if  the first order index is 0 or 1 or not 0 or 1, if neither 0 nor 1, print error
                if firstOrder == 0:
                    result[depId] = [0,0];
                    result[depId][1] = 1;
                elif firstOrder == 1:
                    result[depId] = [0,0];
                    result[depId][1] = 0;
                elif firstOrder is not 0 and firstOrder is not 1:
                    print ('Invalid first order index at row No.', count)
                    count += 1
                    continue
                result[depId][0] = 1;
            # If the department ID is already in the result dictionary
            else:
                result.get(depId)[0] = result.get(depId)[0] + 1
                try:
                    firstOrder = int(row[len(row) - 1])
                except ValueError:
                    print ('Please enter 0 or 1 as first Order at row No.', count)
                    count += 1
                    continue
                if firstOrder == 0:
                    result[depId][1] = result.get(depId)[1] + 1
                elif firstOrder is not 0 and firstOrder is not 1:
                    print ('Invalid first order index at row No.', count)
                    count += 1
                    continue
        else:
            print('The Product ID number', key,'at row No.', count, 'is not in the products file, please double check')
        count += 1
# Create a sorted list of department ID from the result dictionary
# Use the sorted order from the list to write the department ID, total order number, first order number, and the percentage of first order into the new report csv
resultList = sorted(result)
os.chdir('../output')
with open('report.csv', 'w', newline = '') as csvFile:
    fields = ['department_id', 'number_of_orders','number_of_first_orders', 'percentage']
    writer = csv.writer(csvFile)
    writer.writerow(fields)
    for key in resultList:
        key = str(key)
        writer.writerow([key,result.get(int(key))[0], result.get(int(key))[1], "{0:.2f}".format(result.get(int(key))[1]/result.get(int(key))[0])])
