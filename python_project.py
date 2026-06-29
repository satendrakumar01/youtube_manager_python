import json


def load_videos():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        # print("*"*100)
        print(f"{index}. Name: {video['name']}, Time: {video['time']}") 
    print("\n") # print(videos)
    print("*"*100)

def add_video(videos):
    name=input("Enter the video name:")
    time=input("Enter the video time:")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: ")) - 1
    if 0 <= index < len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid video number.")
    

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: ")) - 1
    if 0 <= index < len(videos):
        videos.pop(index)
        save_data_helper(videos)
    else:
        print("Invalid video number.")



def main():
    videos = load_videos()

    while True:
        print("\n Youtube Manager | choose an option:")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")      
        print("5. Exit the application")
        print("--------------------------------------------------")
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting the application. Goodbye!")
                save_data_helper(videos)
                break
            case _:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()