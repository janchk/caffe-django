from djng_app import style


# from djng_app import views


# emulation for parser's namespace arguments
class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# must specify arguments 10 at least


def processing(request):
    images = request.POST['img_to_proceed'].split(',')
    cntimg = images[0]
    simg = images[1]
    args = Namespace(style_img=simg, content_img=cntimg, gpu_id=-1, model='vgg19', init='content',
                     ratio='1e4', num_iters='2', length=200, verbose='store_true', output='')
    processed_output = style.main(args)
    print(processed_output)
    # return processed_output
    return args