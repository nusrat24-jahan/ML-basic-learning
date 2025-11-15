import matplotlib.pyplot as plt
#hello guys we are writing the code make the pie chart 
#1. labels that is the name of the item
labels=["ac machines",'s ans s','analog','gtd','ml','lst','nsf']
imp=[100,90,110,80,120,130,80]
plt.pie(imp,labels=labels,autopct='%1.1f%%',colors=['pink','red','orange','blue','green','grey','purple'])
plt.title('subject i love most')
plt.show()

# Adding a legend for better clarity
plt.legend(labels, title="Subjects", loc="best", bbox_to_anchor=(1, 0.5))

# Adding a shadow and explode effect for better aesthetics
explode = [0.1 if i == max(imp) else 0 for i in imp]  # Highlight the subject with the highest value
plt.pie(imp, labels=labels, autopct='%1.1f%%', colors=['pink', 'red', 'orange', 'blue', 'green', 'grey', 'purple'],
    shadow=True, explode=explode, startangle=90)

# Display the updated pie chart
plt.title('Subjects I Love Most (Improved)')
plt.show()