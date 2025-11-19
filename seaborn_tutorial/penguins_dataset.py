import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("penguins")  # or "iris", "titanic", etc.
print(df.head())


#sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)

#sns.boxplot(x="species", y="body_mass_g", data=df)
#plt.show()

#sns.violinplot(x="species", y="flipper_length_mm", data=df)
#plt.show()

sns.pairplot(df, hue="species")
plt.show()
