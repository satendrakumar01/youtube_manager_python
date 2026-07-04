import sqlite3


con=sqlite3.connect('youtube_videos.db')

cursor=con.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL, 
               time TEXT NOT NULL
               )
               
               ''')




def add_video():
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    con.commit()
    print("Video added successfully!")

def show_videos():
    cursor.execute('SELECT * FROM videos')
    videos = cursor.fetchall()
    for video in videos:
        print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")

def update_video():
     
     cursor.execute('SELECT * FROM videos')
     videos = cursor.fetchall()
    #  print(videos)
     for video in videos:
        print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")

     video_id = input("Enter video ID to update: ")
     new_name = input("Enter new video name: ")
     new_time = input("Enter new video time: ")
     cursor.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (new_name, new_time, video_id))
     con.commit()
     print("*"*100)
     print("Video updated successfully!")
     print("Updated video list:")
     show_videos()

def delete_video():
    video_id = input("Enter video ID to delete: ")
    cursor.execute('DELETE FROM videos WHERE id = ?', (video_id,))
    con.commit()
    print("Video deleted successfully!")
            



def main():
    while True:
        print("\nYouTube Video Management System")
        print("1. Add video")
        print("2. Show videos")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':

            add_video()
        
        elif choice == '2':
            show_videos()
        
        elif choice == '3':
            update_video()
        
        elif choice == '4':
            delete_video()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice! Please try again.")
        con.close()


if __name__ == "__main__":
    main()