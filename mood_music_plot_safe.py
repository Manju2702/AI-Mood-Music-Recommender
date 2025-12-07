import os
import sys
import matplotlib.pyplot as plt
mood_keywords = {
    "happy": ["happy", "joy", "excited", "great", "love"],
    "sad": ["sad", "down", "unhappy", "cry"],
    "angry": ["angry", "mad", "furious"],
    "stressed": ["tired", "pressure", "overwhelmed", "stress"],
    "calm": ["calm", "peaceful", "relaxed", "okay"]
}
music_recs = {
    "happy": "Pop / Dance",
    "sad": "Soft Piano / Acoustic",
    "angry": "Rock / Energetic",
    "stressed": "Lo-Fi / Ambient",
    "calm": "Meditation / Chill"
}
mood_history = []
def tokenize(text):
    for ch in ".,!?;:\n\t":
        text = text.replace(ch, " ")
    return text.lower().split()
def predict_mood(text):
    tokens = tokenize(text)
    scores = {mood: 0 for mood in mood_keywords}

    for mood, words in mood_keywords.items():
        for w in words:
            if w in tokens:
                scores[mood] += 1

    best_mood = max(scores, key=scores.get)
    return best_mood, scores[best_mood]
def plot_and_save(mood_list, filename="mood_frequency.png"):

    if not mood_list:
        print("No mood data to plot.")
        return False

    moods = sorted(list(set(mood_list)))
    counts = [mood_list.count(m) for m in moods]

    plt.figure(figsize=(7, 4))
    bars = plt.bar(moods, counts, color="skyblue")
    plt.xlabel("Mood")
    plt.ylabel("Count")
    plt.title("Mood Frequency Chart")

    for bar, cnt in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width()/2, cnt + 0.05, str(cnt),
                 ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(filename)
    print(f"\nGraph saved as: {os.path.abspath(filename)}")

    try:
        plt.show()
    except:
        print("Graph display failed, but image is saved.")

    return True
print("AI Mood-to-Music Recommender")
print("Enter your mood sentence each time.")
print("Type 'exit' to finish and show the graph.\n")

while True:
    text = input("How do you feel today? >>> ")

    if text.strip().lower() == "exit":
        break

    if not text.strip():
        print("Please type something.")
        continue

    mood, score = predict_mood(text)
    music = music_recs[mood]
    mood_history.append(mood)

    print("\n--- RESULT ---")
    print("Detected Mood :", mood.title())
    print("Match Score   :", score)
    print("Music Suggest :", music)
    print("---------------------------\n")

print("\nPreparing your mood graph...")
plot_and_save(mood_history)
print("\nDone! If graph didn't open, open mood_frequency.png manually.")

