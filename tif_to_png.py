from PIL import Image
from PIL import ImageSequence
from pathlib import Path

def tif_to_png(path):
    '''
    Converte arquivo .tif para png splitando as páginas do documento.
    | Parâmetros:
    |-- path: Caminho do arquivo.
    '''
    im = Image.open(path)
    name=str(Path(path).parent)+str(Path(path).stem)
    for i, page in enumerate(ImageSequence.Iterator(im)):
        page.save(name+"_%d.png" % i, quality=300)

tif_to_png("image.tif")


