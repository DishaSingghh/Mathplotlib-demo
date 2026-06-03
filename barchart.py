import matplotlib as mpl;
import matplotlib.pyplot as plt;
import numpy as np;
categories=np.array(["Grains","Vegetables","Fruits","Dairy","Meat"]);
values=np.array([20,15,30,10,25]);
#bar chart
# plt.bar(categories, values, color=['red', 'green', 'blue', 'orange', 'purple']);
# plt.xlabel("Food Categories");
# plt.ylabel("Values");
# plt.title("Bar Chart");
#pie chart 
plt.pie(values, labels=categories, autopct='%1.1f%%', explode=(0, 0, 0, 0, 0.1), colors=['red', 'green', 'blue', 'orange', 'purple']);
plt.show();