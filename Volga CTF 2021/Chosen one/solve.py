from apng import APNG
import cv2 as cv
import matplotlib.pyplot as plt
from bitstring import BitArray

# read an apng file
ampg_file = APNG.open("../movie.apng")
# get the bytes of an apng file
file_bytes = ampg_file.to_bytes()

# get frames from an apng file
z_frames = ampg_file.frames
for count_frame in range(len(z_frames)):
    z_frames[count_frame][0].save("../frames/frames" + str(count_frame) + ".png")


#computing the lsb of the blue_plane frames
with open("../out", "wb") as f:
    for name in ["../frames/frames437.png", "../frames/frames579.png"]:
        # z_comment read all pizel value in 3 channels
        img = cv.imread(name)
        # z_comment computing the lsb of the blue_plane frames
        blue_plane = img[:, :, 0] & 1  # get LSB from 0'th channel (blue)
        # z_comment show the results images of the lsb data
        plt.imshow(blue_plane); plt.show()  # debug printing so that we know we have the correct files
        # z_comment convert array to flatten binary string
        bits = "".join(blue_plane.flatten().astype(str))  # flatten 1920x1000 pixel array of binary to string
        by = BitArray(bin=bits).tobytes()  # bitstring to bytes
        f.write(by)
