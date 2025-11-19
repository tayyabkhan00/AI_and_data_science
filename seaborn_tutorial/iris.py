import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")  # or "penguins", "titanic", etc.
(df.head(2))

#sns.boxplot(x="species", y="petal_length", data=df)
#plt.show()

#sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
#plt.title("Correlation Between Flower Measurements")

sns.pairplot(df, hue="species")
#plt.show()


# sns.violinplot(x="species", y="petal_length", data=df)
# plt.title("Distribution of Petal Length by Species")
plt.show()