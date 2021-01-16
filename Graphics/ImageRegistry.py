images = {
    # key is image name, value is pygame image
}


def register_images():
    from pygame.image import load
    from Graphics import RendererManager
    import os
    # get the directory of the images relative to this file
    directory = os.path.join(__file__.split("Graphics")[0], "assets", "images")
    files = os.listdir(directory)
    for file_name in files:
        full_path = os.path.join(directory, file_name)
        name_without_extension = file_name.split(".")[0]
        extension = file_name.split(".")[1]
        if extension == 'png':
            images[name_without_extension] = load(full_path).convert_alpha(RendererManager.screen)
        else:
            images[name_without_extension] = load(full_path).convert(RendererManager.screen)


def get_image(name):
    return images[name]
