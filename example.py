import os

def clear_finished():
    folder = 'finished'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            print(file_path)
            os.unlink(file_path)

if __name__ == "__main__":
    import sys
    from pymysqlbatchimport.run import App
    App.run()
    clear_finished()
