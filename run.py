from PIL import Image, ImageDraw

im = Image.new('RGBA', (100, 100), (255,255,255,0))

ctx = ImageDraw.Draw(im)

ctx.point([(1, 2)], (100, 100, 100, 1))

im.show()