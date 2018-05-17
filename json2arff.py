import json

with open('feature_name_data.json', 'r') as sd:
    dat = json.load(sd)
with open('feature_name_labeltxt.json', 'r') as sl:
    lab = json.load(sl)
dosya = open("feature_name_feature.arff","w")
dosya.write("@RELATION facialexpressionrecognition\n")
oznitelik = int(dat["image_feature_0"]["cols"])
for i in range(oznitelik):
    dosya.write("@ATTRIBUTE feature"+str(i)+" real\n")
dosya.write("@ATTRIBUTE duygu {Angry,Disgusted,Fear,Happy,Sad,Surprised}\n@data\n")
for i in range(len(dat)):
    dosya.write(",".join(map(str, dat["image_feature_"+str(i)]["data"])))
    dosya.write("," + str(lab["image_label_" + str(i)]))
    dosya.write("\n")
dosya.close()