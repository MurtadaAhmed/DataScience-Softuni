# from transformers import TrOCRProcessor, VisionEncoderDecoderModel
# from PIL import Image
import requests
#
# # load image from the IAM database (actually this model is meant to be used on printed text)
# url = 'https://localfonts.eu/wp-content/uploads/2017/12/Bulgaria-Moderna-01.jpg'
# image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
#
# processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
# model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed')
# pixel_values = processor(images=image, return_tensors="pt").pixel_values
#
# generated_ids = model.generate(pixel_values)
# generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
#
# print(generated_text)




# from transformers import TrOCRProcessor, VisionEncoderDecoderModel
# from PIL import Image
#
# # Load processor and model
# processor = TrOCRProcessor.from_pretrained("microsoft/trocr-large-printed")
# model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-large-printed")
#
# # Load an image
# # url = 'https://localfonts.eu/wp-content/uploads/2017/12/Bulgaria-Moderna-01.jpg'
# # image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
# image = Image.open("image.PNG")
#
# # Preprocess image and run the model
# pixel_values = processor(images=image, return_tensors="pt").pixel_values
# generated_ids = model.generate(pixel_values)
#
# # Decode the predicted text
# generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
# print(generated_text)

# from transformers import pipeline
#
# # Initialize the pipeline with the model
# pipe = pipeline("image-to-text", model="raxtemur/trocr-base-ru")
#
# # Perform OCR on an image
# text = pipe("bulgarski.PNG")[0]['generated_text']
#
# print("Extracted Text:", text)



import easyocr

# Initialize reader with Bulgarian language
reader = easyocr.Reader(['bg'])

# Perform OCR on the image
result = reader.readtext('image.PNG')

# Extract text
for (bbox, text, prob) in result:
    print(f"Detected text: {text} with confidence {prob:.4f}")

