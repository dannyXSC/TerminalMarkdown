from datetime import datetime, timedelta

class Session:
    def __init__(self):
        self.start_time = None
        self.files = {}
        self.last_time = {}
        self.current = None

    def load(self, filename):
        self.start_time = datetime.now()
        if filename in self.files:
            pass
            # print(f"Resuming session for {filename}.")
        else:
            self.files[filename] = self.start_time
            # print(f"New session for {filename} started.")

    def stats(self, command):
        current_time = datetime.now()
        if command.strip().endswith("md"):
            #print("session start", self.start_time.strftime('%Y%m%d %H:%M:%S'))

            duration = current_time - self.files[command]
            print(f"./{command} {self.format_duration(duration)}")
        elif command == "all":

            for filename, start_time in self.files.items():
                duration = current_time - start_time
                print(f"./{filename} {self.format_duration(duration)}")
                # Assuming log file search and addition here
        elif command == "current":
            duration = current_time - self.files[self.current]
            print(f"./{self.current} {self.format_duration(duration)}")

        else:
            print("It is Invalid command.")

    def quit(self):
        end_time = datetime.now()
        if self.start_time:
            for filename, start_time in self.files.items():
                duration = end_time - start_time
                with open('log.txt', 'a') as file:  # 'a' 表示以附加模式打开文件
                    file.write(f"./{filename} {self.format_duration(duration)}" + "\n")  # 写入数据并换行
                # print(f"./{filename} {self.format_duration(duration)}")
            self.start_time = None  # Clear session

    @staticmethod
    def format_duration(duration):
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        if hours==0:
            return f"{minutes} 分钟"
        else:
            return f"{hours} 小时 {minutes} 分钟"

# session = Session()

#
# while True:
#     command = input("Enter a command (load [filename], stats [current | all], q to exit): ")
#     if command.startswith("load"):
#         filename = command.split(" ")[1]
#         session.load(filename)
#     elif command.startswith("stats"):
#         command_parts = command.split(" ")
#         if len(command_parts) == 2:
#             session.stats(command_parts[1])
#         else:
#             print("Invalid stats command.")
#     elif command == "q":
#         session.quit()
#         break
#     else:
#         print("Invalid command.")


