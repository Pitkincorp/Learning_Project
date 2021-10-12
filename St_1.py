with open('dataset_24465_4.txt') as f:
    text = f.readlines()
    text.reverse()
with open('newtext.txt', 'w') as n:
    for i in text:
        n.write(i)
