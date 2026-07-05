from unittest import result
from bson import ObjectId
from pymongo import MongoClient
# from python_project import delete_video, update_video

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.nv6dykp.mongodb.net/ytmanager", tlsAllowInvalidCertificates=True) #not a good idea to put your password in the code, but for testing purposes, it is fine.db = client["ytmanager"]


db=client["ytmanager"]
videos_collection = db["videos"]

print(videos_collection)


def view_videos():
    videos = videos_collection.find()
    for video in videos:
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")


def add_video(name, time):
    video = {"name": name, "time": time}
    videos_collection.insert_one(video)
    print("Video added successfully!")

def update_video(video_id, name, time):
    videos_collection.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": {"name": name, "time": time}}
    )
    print("Video updated successfully!")

def delete_video(video_id):
    videos_collection.delete_one({"_id": ObjectId(video_id)})
    print("Video deleted successfully!")



def main():
    while True:
        print("Welcome to the YouTube Video Manager!")
        print("1. View videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video ID to update: ")
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
















