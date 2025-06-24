from deepface import DeepFace
import tempfile
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


def detect_expression(image_file):
    from deepface import DeepFace
    from PIL import Image
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image = Image.open(image_file)
        image.save(tmp.name)
        try:
            result = DeepFace.analyze(img_path=tmp.name, actions=['emotion'], enforce_detection=False)
            return result[0]['emotion']  # Dict of emotions and their confidence
        except Exception as e:
            return {"error": str(e)}
