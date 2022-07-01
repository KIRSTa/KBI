import hashlib

def comparison_to_hashes(original_file,test_file):
    
    h1=hashlib.sha256(open(original_file,'rb').read()).hexdigest()
    h2=hashlib.sha256(open(test_file,'rb').read()).hexdigest()

    if h1==h2:
        return True
    else:
        return False

# print(comparison_to_hashes('orig.txt','test.txt'))

orig_list=[r'D:\Documents\Desktop\orig.txt',
           r'D:\Documents\Desktop\test.txt',
           r'D:\Documents\Desktop\Хобби курсантов 334 учебной группы.docx',
           r'C:\Program Files\Binance\Binance.exe']

test_list=[r'D:\Documents\Desktop\orig.txt',
           r'D:\Documents\Desktop\test.txt',
           r'D:\Documents\Desktop\Эталонные ответы.docx',
           r'C:\Program Files\Binance\ffmpeg.dll']

for orig_f,test_f in zip (orig_list,test_list):
    print(comparison_to_hashes(orig_f,test_f))
    print(hashlib.sha256(open(orig_f,'rb').read()).hexdigest())
    print(hashlib.sha256(open(test_f,'rb').read()).hexdigest())
    print('===================================================')
