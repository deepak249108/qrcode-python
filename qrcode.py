import qrcode
import image

deepak=qrcode.QRCode()

data="https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x&ab_channel=TechieCoder"
deepak.add_data(data)
deepak.make(fit=True)
img=deepak.make_image()
img.save("test.png")
