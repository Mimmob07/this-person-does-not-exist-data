# from hair_color_detector import HairColorDetector

# hcd = HairColorDetector()
# detected_color = hcd.get_color("assets/img_1.jpeg", save_result=False)
# print(f"Detected color: {detected_color}")

from deepface import DeepFace

file = open("data.csv", "w")
file.write("Filename,Race,Emotion,Gender,Age\n")

for i in range(1,1001):
    filename = f"assets/img_{i}.jpeg"

    try:
        objs = DeepFace.analyze(img_path = filename, actions = ['age', 'gender', 'race', 'emotion'])[0]
        file.write(f"{filename},{objs['dominant_race']},{objs['dominant_emotion']},{objs['dominant_gender']},{objs['age']}\n")
        print(f"Processed image {i}")
    except Exception as e:
        print(f"Face not found: {e}")
        file.write(f"{filename},,,,\n")
