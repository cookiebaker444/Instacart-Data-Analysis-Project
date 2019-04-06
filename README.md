To run my Python file, just download the repository and run the python codes. The code with name "Final Code" is the one for my test cases with dirty data, and the other code with name "Final Code provided data" is the code for the provided Instacart data.

My logic for doing the analysis job is to use a dictionary to record product ID (key) and the corresponding department ID (value) first, and to use this dictionary to be able to recognize the department ID of the products that appears in the order information csv file, because the csv file does not contain the department ID information in it. When analyzing the data from the order information csv file, another dicionary is used to store the deparmtnet ID (key) and a two-element integer list (value). The first element of the list is the total amount of order in this department, and the second element is the amount of the first order in this department. The last step is to write everything into a csv file plus the percentage of first order in the total order.

In the Python files, there are more detail comments in the code.

**Very Important! When try to use the file from the resource called "order_products__train.csv", please make sure to download the file into the file input in the master branch, to be able to run the code with it. The download link is https://www.instacart.com/datasets/grocery-shopping-2017. **
