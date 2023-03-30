import os
import json
import textgrid

def textgrid_to_json(textgrid_file):
    tg = textgrid.TextGrid.fromFile(textgrid_file)
    phone_tier = tg.getFirst("phones")
    word_tier = tg.getFirst("words")

    phones = [{"start": interval.minTime, "end": interval.maxTime, "phone": interval.mark} for interval in phone_tier]
    words = [{"start": interval.minTime, "end": interval.maxTime, "word": interval.mark} for interval in word_tier]

    return {"phones": phones, "words": words}

input_directory = "aligned/"
output_directory = "public/alignments/"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    if filename.endswith(".TextGrid"):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename.replace(".TextGrid", ".json"))

        json_data = textgrid_to_json(input_path)

        with open(output_path, "w") as outfile:
            json.dump(json_data, outfile)
