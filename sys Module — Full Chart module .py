sys Module — Full Chart


| #  | Syntax                     | क्या करता है?                                    | आसान याद           |
| -- | -------------------------- | ------------------------------------------------ | ------------------ |
| 1  | `sys.argv`                 | Command-line arguments की list                   | **Arguments**      |
| 2  | `sys.argv[0]`              | Script का name/path                              | **Program**        |
| 3  | `sys.argv[1]`              | पहला argument                                    | **1st argument**   |
| 4  | `sys.argv[2]`              | दूसरा argument                                   | **2nd argument**   |
| 5  | `sys.exit()`               | Program terminate करता है                        | **Stop**           |
| 6  | `sys.stdin`                | Standard input                                   | **Input लेना**     |
| 7  | `sys.stdin.readline()`     | एक line input पढ़ना                              | **Input line**     |
| 8  | `sys.stdout`               | Standard/normal output                           | **Output देना**    |
| 9  | `sys.stdout.write()`       | Output manually लिखना                            | **Output control** |
| 10 | `sys.stderr`               | Error/diagnostic output                          | **Error**          |
| 11 | `sys.stderr.write()`       | Error message लिखना                              | **Error output**   |
| 12 | `sys.version`              | Python version + build details                   | **Python version** |
| 13 | `sys.platform`             | Current platform बताता है                        | **OS/Platform**    |
| 14 | `sys.path`                 | Module/package search locations                  | **Module कहाँ?**   |
| 15 | `sys.modules`              | Loaded/imported modules की dictionary            | **Module loaded?** |
| 16 | `sys.executable`           | Current Python interpreter का path               | **Python कहाँ?**   |
| 17 | `sys.getsizeof(obj)`       | Object का size bytes में                         | **Memory size**    |
| 18 | `sys.maxsize`              | `Py_ssize_t` की platform-dependent maximum value | **Maximum value**  |
| 19 | `sys.getrecursionlimit()`  | Current recursion limit बताता है                 | **Limit देखो**     |
| 20 | `sys.setrecursionlimit(n)` | Recursion limit बदलता है                         | **Limit बदलो**     |




  सबसे Important Differences



  sys.stdin
→ Input लेना

sys.stdout
→ Normal output देना

sys.stderr
→ Error output देन
  
  
  
  sys.path
→ Module कहाँ search होगा? 🔍

sys.modules
→ कौन-सा module loaded है? 📦

sys.executable
→ कौन-सा Python चल रहा है? 🐍
  
  
  
sys.getrecursionlimit()
→ Limit देखना 👀

sys.setrecursionlimit()
→ Limit बदलना ✏️ा
