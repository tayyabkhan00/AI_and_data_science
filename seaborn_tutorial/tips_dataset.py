import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load an example dataset
print(sns.get_dataset_names())
df=sns.load_dataset('tips')
print(df.head())


# Create a scatter plot
#sns.countplot(x="day", data=df)


# Create a heatmap to visualize correlations
#sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

#sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm")

#sns.set_style("whitegrid")
#sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
#plt.title("Total Bill vs Tip")
#plt.show()


#sns.histplot(df["total_bill"], kde=True)
#plt.show()

#sns.boxplot(x=df["tip"])
#plt.show()

#sns.histplot(df["size"], kde=True)#kde is for smooth curve
#plt.show()

#sns.countplot(x="day",hue="sex", data=df)
#plt.show()

#table = pd.crosstab(df["sex"], df["smoker"])
#sns.heatmap(table, annot=True, cmap="coolwarm")
#plt.show()

#sns.lineplot(x="total_bill", y="tip", data=df)
#plt.show()

