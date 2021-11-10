                          ########ACTIVITY 1###########

# A scatter plot is a type of plot or mathematical diagram using Cartesian coordinates to display values
# for typically two variables for a set of data.
# If the points are coded, one additional variable can be displayed.


                        # ###########ACTIVITY 2###########
import matplotlib.pyplot as plt
with open("test.txt") as f:
    data = f.read()
data = data.split('\n')
x = [float(row.split(' ')[0]) for row in data]
y = [float(row.split(' ')[1]) for row in data]
plt.plot(x, y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Sample graph!')
# Display a figure.
plt.show()


                    # #######################    ACTIVITY 3    ###############


# import matplotlib.pyplot as plt
# from pylab import randn
# X = randn(200)
# Y = randn(200)
# plt.scatter(X,Y, color='r')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()                  