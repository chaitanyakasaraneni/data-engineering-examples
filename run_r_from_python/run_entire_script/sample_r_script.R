install.packages("ggplot2",repos = "http://cran.us.r-project.org")
library(ggplot2)
library(datasets)

# Load the iris dataset
data(iris)

# Create a scatter plot of Sepal.Length vs Sepal.Width
ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point() +
  ggtitle("Sepal Length vs. Sepal Width")

# Create a scatter plot of Petal.Length vs Petal.Width
ggplot(iris, aes(x = Petal.Length, y = Petal.Width, color = Species)) +
  geom_point() +
  ggtitle("Petal Length vs. Petal Width")

# Create a histogram of Sepal.Width
ggplot(iris, aes(x = Sepal.Width, fill = Species)) +
  geom_histogram() +
  ggtitle("Distribution of Sepal Width")

# Create a boxplot of Petal.Length by Species
ggplot(iris, aes(x = Species, y = Petal.Length)) +
  geom_boxplot() +
  ggtitle("Boxplot of Petal Length by Species")
