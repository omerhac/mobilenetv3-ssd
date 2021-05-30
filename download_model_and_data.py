from urllib import request
import os
if __name__ == '__main__':
    # download model
    models_dir = 'models'
    if not os.path.exists(models_dir):
        os.mkdir(models_dir)

    print(f'Downloading model into {models_dir} .....')
    request.urlretrieve('https://github.com/lufficc/SSD/releases/download/1.2/mobilenet_v3_ssd320_voc0712.pth',
                        filename=f'{models_dir}/mobilenetv3_ssd.model')
    print('Finished downloading!')

    # download dataset
    datasets_dir = 'datasets'
    if not os.path.exists(datasets_dir):
        os.mkdir(datasets_dir)
    print(f'Downloading coco dataset into {datasets_dir} ..... (It might take some time)')
    request.urlretrieve('http://images.cocodataset.org/zips/val2017.zip',
                        filename=f'{datasets_dir}/val2017.zip')
    print('Finished downloading!')