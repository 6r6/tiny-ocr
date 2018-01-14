# tiny-ocr

***

### 腾讯优图通用OCR
识别率超高、抗干扰强、免费。[接口申请](http://open.youtu.qq.com/)

```
ocr = Youtu('app_id', 'secret_id', 'secret_key')
resp = ocr.get_text('3.png')
```

### 汉王OCR（aliyun）
识别率一般、抗干扰极差、SDK杂乱。[点我购买](https://market.aliyun.com/products/57124001/cmapi011523.html)

汉王官方SDK的写作风格真的...只能用匪夷所思来形容

```
ocr = Hanvon(你的appcode)
print(ocr.get_text('zs', 'png'))
```

***
以上仅为个人观点！
