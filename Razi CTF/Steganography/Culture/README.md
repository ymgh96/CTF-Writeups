An image in PNG format [enc.png](https://github.com/ymgh96/CTF-Writeups/blob/main/Razi%20CTF/Steganography/Culture/enc.png) is given in this challenge.\
If we run zsteg tool, we can acheive the flag.\
```
root@kali:~/razi/Culture# zsteg enc.png 
imagedata           .. text: "+*#QRM'(\""
b1,bgr,lsb,xy       .. text: "RaziCTF{i_s33_ur_4_MaN_0f_LSB_aS_W3LL}====="
b2,b,lsb,xy         .. text: "UZ_yl\t z"
b4,r,lsb,xy         .. text: "ff3\"\"#Ffffwwww"
b4,r,msb,xy         .. text: ["U" repeated 8 times]
b4,g,lsb,xy         .. text: "322\"3\"22TB2\""
b4,g,msb,xy         .. text: "UUUU3333"
b4,b,lsb,xy         .. text: "\"#33#\"33EDDDUUUU"
b4,b,msb,xy         .. text: ["U" repeated 8 times]
```
