"""
SatelliteImage class basics
===========================

This is (right now) a dummy example for showing the functionality of :class:`geoutils.SatelliteImage`.
"""
import matplotlib.pyplot as plt

import geoutils as gu

# %%
# Example raster:
img = gu.Raster(gu.datasets.get_path("landsat_B4_crop"))

# %%
# Info:
print(img)


# %%
# A plot:
img.show(cmap="Greys_r")
plt.show()