TODO: Reflect on what you learned this week and what is still unclear.

../ben_is_cool.txt means the file named ben_is_cool.txt located in the parent directory of the current working directory. For example, if your current working directory is /home/user/docs, the path ../ben_is_cool.txt would refer to /home/user/ben_is_cool.txt.

xxx.read() reads the entire contents of the file

json.dumps() is used to convert a Python object into a JSON string. This process is known as serialization or "dumping" the object to JSON.
xx.write(string/item/object) is used write a string (or bytes) to a file object xx.

json.loads() is a method that is used to parse a JSON string and convert it into a Python dictionary, list, or other appropriate data structure.

requests.get(url) gets the info in the url

\t sequence represents a tab character

modes
w=write mode. This will create the file if it does not exist, or overwrite the file if it does exist.
r=read mode. This allows the function to read the contents of the file without modifying it.

absolute path defines the filepath from the whole machine (from big daddy file to the exact file, layer by layer)
relative path locates the file in relation to the current working directory (ie the file that is written after denyceng@Denyces-MacBook-Air in terminal)

../ means in parent directory of current directory
./ means in current directory
/ means in big daddy/root directory

Assuming the current directory is /home/user:
./document.txt refers to /home/user/document.txt.
../document.txt refers to /home/document.txt.
