from bertopic import BERTopic
import os
import shutil

embedding_model1 = "thenlper/gte-small"
loaded_model = BERTopic.load("my_model_dir", embedding_model=embedding_model1)

UNSORTED_FOLDER = "unsorted"
SORTED_FOLDER = "sorted"

os.makedirs(SORTED_FOLDER, exist_ok=True)

for filename in os.listdir(UNSORTED_FOLDER):
    if filename.endswith(".txt"): 
        file_path = os.path.join(UNSORTED_FOLDER, filename)
        
       
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
       
        topic, _ = loaded_model.transform([content])
        topic_name = loaded_model.get_topic(topic[0])[0][0] if topic[0] != -1 else "Unknown"

        topic_name = topic_name.replace("/", "_") 

        
      
        topic_folder = os.path.join(SORTED_FOLDER, topic_name)
        os.makedirs(topic_folder, exist_ok=True)
        
       
        shutil.move(file_path, os.path.join(topic_folder, filename))
        print(f"Moved {filename} to {topic_folder}/")

print("Sorting completed!")