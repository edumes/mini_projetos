from captcha.image import ImageCaptcha

imagem = ImageCaptcha(width=280, height=90)
captcha_text = 'edumes.py'
data = imagem.generate(captcha_text)
imagem.write(captcha_text, 'captcha.png')