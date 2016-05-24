# This section imports modules installed from third-party packages
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import rcParams, image
import numpy as np

# This section would import modules created by the user


# # Let's import the data we want to use from the file 'alpleo9.p' using the pickle function
# file_to_read = open('alpleo9.p', 'rb') # This opens the file for Python to read
# alpleo9 = pickle.load(file_to_read) # This unpacks the included data into a Python dictionary named 'alpleo9'
#
# # This dictionary contains several keys, two of which interest us here: radius and data. Let's extract the arrays paired with these keys for easier use
# data = alpleo9['data']
# radius = alpleo9['radius']
# optical_depth = alpleo9['optical_depth']
#
# # Now let's take a look at our data by plotting it, using matplotlib, which we have imported as plt.
# plt.plot(radius,data)
# plt.show()
#
# # Let's investigate that dip around 140,000 km by extracting that region from the overall data
# data_region = data[(radius > 138000) & (radius < 142000)]
# radius_region = radius[(radius > 138000) & (radius < 142000)]
# plt.plot(radius_region,data_region)
# plt.show()
#
# # Let's zoom in even further and examine that sharp dip:
# data_region = data[(radius > 139500) & (radius < 140500)]
# radius_region = radius[(radius > 139500) & (radius < 140500)]
# plt.plot(radius_region,data_region)
# plt.show()
#
# # Let's overplot the optical depth in this region
# od_region = optical_depth[(radius > 139500) & (radius < 140500)]
# plt.plot(radius_region,data_region/10000)
# plt.plot(radius_region,od_region)
# plt.show()
#
# # Let's find the minimum value of data in this region:
# min_value = np.min(data_region)
# print(min_value)
#
# # Time to make the plot prettier!
# rcParams.update({'font.size': 16}) # Set plot font size to 16
# rcParams.update({'figure.figsize': (20, 10)}) # Set the plot size in (x,y) inches
# plt.plot(radius_region,data_region/10000)
# plt.plot(radius_region,od_region)
# plt.xlim((139500,140500))
# plt.ylim((0,1.5))
# plt.title("A strange feature in Saturn's rings",size=24) # Give it a title!
# plt.xlabel('Distance from Saturn (km)',size=20) # Label the x axis
# plt.ylabel('Counts x10000 / optical depth',size=20) # Label the y axis
# plt.text(139950,2500,'min='+str(min_value),size=18) # Label the minimum point
# plt.legend(['Counts','Optical depth'])
# plt.show()

my_image = image.imread('N1530370686.png')
plt.imshow(my_image,vmin=0.1,vmax=0.2)
plt.show()
