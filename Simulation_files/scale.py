import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def scale_1000(x):
  print(x.shape)
  x = x - np.min(x)
  x = x/(np.max(x))
  x = x*100
  print("x shape: ", x.shape)
  x = np.round(x)
  print(x.shape)
  return x.astype(int)




for n in [2, 3, 4]: # number of bodies
	xarr = np.load('xtracks_{}.npy'.format(n))
	yarr = np.load('ytracks_{}.npy'.format(n))
	plt.plot(xarr[0], yarr[0])
	plt.savefig("prior{}.pdf".format(n))
	plt.close()
	# plt.plot()

	img_rows, img_cols = 110, 110
	imgs = np.zeros((n, img_rows, img_cols))
	for i in range(n):
	  print(xarr[i].shape)
	  print(yarr[i].shape)

	  xvals = scale_1000(xarr[i])
	  yvals = scale_1000(yarr[i])
	  print(xvals.shape)
	  print(yvals.shape)
	  for xval, yval in zip(xvals, yvals):
	  	imgs[i][xval][yval] = 1

	  print(imgs[i].tolist())

	  # new_img = Image.fromarray(img).convert('L')
	  # filename = 'test'+str(n) + "_" + str(i) + '.png'
	  # print("filename: ", filename)
	  # new_img.save(filename)
	  plt.imshow(imgs[i], cmap ='Greys', interpolation='nearest')
	  plt.show()
	  plt.savefig("after{}{}.pdf".format(i,n))
	  plt.close()
	  quit()

