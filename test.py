from PIL import Image

foo = Image.open("screenshot.png")
print(foo.size) #(1920, 1080) - > 1366 , 768
foo = foo.resize((1366 , 768),Image.ANTIALIAS)
foo.save("images/screenshot_down.png",quality=95)