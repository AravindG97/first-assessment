import os
from datetime import datetime
print(dir(os))
print(os.getcwd())
# os.chdir("psth")
print(os.listdir())
# os.makedir()"""only one if given 2 itll throw error"""
# os.makedirs()"""can create subdirectory like  folder1/sub-folder1-sub2"""
# os.rmdir()
# os.rmdirs()
# os.rename("hangman.py","hang.py")
print(os.listdir())
a=os.stat("hang.py").st_mtime
print(datetime.fromtimestamp(a))
# os.walk()"""generator reuturns a list of tuples with 3 elements"""
# for dirpath, dirname ,filenames in os.walk(os.getcwd()):
#     print(dirname)
#     print(dirpath)
#     print(filenames)
print(os.environ)
b="aa.txt"
path=os.path.join(os.environ,"bb.txt")
print(path)
# print(os.path.exists("path"))
# os.path.isfile()
# os.path.isdir()
os.path.splitext("path")"""split @ extension gives file name w/o extension"""
# os.system("file name to be opened")
import zipfile







# ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
# C:\Users\N.Vishvanand\PycharmProjects\practise
# ['.idea', 'hangman.py', 'hangman_final.py', 'oss.py', 't2.py', 't3.py', 'trial.py', 'venv', '__pycache__']
# ['.idea', 'hang.py', 'hangman_final.py', 'oss.py', 't2.py', 't3.py', 'trial.py', 'venv', '__pycache__']
