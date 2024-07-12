w, h, b = map(int, input().split())
print(f'{w*h*b/8/1024/1024:0.2f}', 'MB')