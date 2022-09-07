import qrcode
import qrcode.image.svg


factory = qrcode.image.svg.SvgPathFillImage
svg_img = qrcode.make("Helllo world", image_factory=factory)
svg_img.save("myqr.svg")











