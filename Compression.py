import numpy as np
from PIL import Image

def loadData(filePath):
    f = open(filePath, 'rb')
    data = []
    img = Image.open(f)  
    m, n = img.size   # get the size(m, n) of the picture
    for i in range(m):  
        for j in range(n):
            x,y,z = img.getpixel((i,j))
            data.append([x, y, z]) # get a list of the pixels in the picture
    f.close()
    return data, m, n # return the pixel list and the size of the picture

def kmeans_clustering(pixellist, k):   # pixellist: a list of pixels; k: the number of clusters
    pixelarr=np.array(pixellist).astype(np.int32)
    num_pix, num_cha = pixelarr.shape   # num_pix: the number of pixels; num_cha: the number of channels
    cluster_pix = np.empty(num_pix, dtype=np.int32) # generate a num_pix long array, used to denote which cluster each pixel belongs to
    cores = pixelarr[np.random.choice(np.arange(num_pix), k, replace=False)] # randomly pick k pixels as the initial cores

    # If k==2, watermark removal feature is activated, which eliminates the randomness of the choice of initial points.
    while k==2 and cores[0][0]==cores[1][0] and cores[0][1]==cores[1][1] and cores[0][2]==cores[1][2]:
        cores = pixelarr[np.random.choice(np.arange(num_pix), k, replace=False)]
    #####
   
    reshaped_pixelarr = np.repeat(pixelarr, k, axis=0).reshape(num_pix, k, num_cha)
    
    while True:
        dif = reshaped_pixelarr - cores # calculate the difference between the pixel and the core
        dif2 = np.square(dif)
        distance = np.sqrt(np.sum(dif2, axis=2)) # calculate the distance of each pixel to each core
        closest_core = np.argmin(distance, axis=1) # derive the closest core to each pixel
        
        if (closest_core == cluster_pix).all(): # if the clusters don't change, then end the loop
            break
        
        cluster_pix = closest_core # assign each pixel to the closest core to form new clusters
        for i in range(k):
            pixelitems = pixelarr[cluster_pix==i]
            cores[i] = np.mean(pixelitems, axis=0) # calculate the new core for new clusters

    return cluster_pix, cores

def Compress(path,name,k):
    imgData, row, col = loadData(filePath= path)
    cluster_pix,cores = kmeans_clustering(imgData, k)
    pic_new = Image.new('RGB', (row, col))
    # generate a new picture using the mean of the clusters
    for i in range(row):
        for j in range(col):
            pic_new.putpixel((i, j), tuple(np.around(cores[cluster_pix[i*col+j]]).astype(np.int32)))
    # save the picture in JPG format
    pic_new.save(name,"JPEG")





