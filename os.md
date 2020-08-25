## Linux/Unix
### Tips
* ldd /bin/ls
* [ -d tests ] && echo exists
* last working dir: cd -; home dir: cd ~
* only if success: cmd1 && cmd2
* last arg: alt+.
* set up default group for creating file: newgrp grp
* Get file size: `find . -type f -exec du -b {} + | awk '{sum+=$1} END{print sum}'` (The difference between ; and + is that with ; a single command for each file is executed whereas with + as many files as possible are given as parameters at once).
* Find by size: `find . -type f -size +30M -size -40M -exec ls -l {} +`
* Test variable not exists: `if [ -z "$VAR" ]; then; echo not-exists; fi`

### Shell expansion
* Pathname Expansion: echo *; echo [[:upper:]]*
* Arithmetic Expansion: echo $((1+2)); 
* brace expansion: echo {a,b,c}_back; echo {1..5}; echo {z..a}; 
* Command Substituation: file $(ls /usr/bin/* | grep bin/zip)
* Double quotes suppress word-splitting
* Single Quotes suppress all expansions.
* Backslash to escape
* http://linuxcommand.org/lc3_lts0080.php


### awk
* `awk '{print $1,$2}'`; printf
* IFS: internal field separator
* pattern match: '/pattern/ action'
* [awk command series](https://www.tecmint.com/tag/awk-command/)

## Windows
### Win tips
* List groups: `whoami /groups; gpresult /r`
* Ticket reset: `klist purge; klist tgt`
* update GPO: `gpupdate /force`. GPO editor console: rsop.msc
* Map network drive: `net use m: path /persistent:yes
* `runas /user:username explorer
*


## Reference
* [Linux shell scripting tutorial](https://bash.cyberciti.biz/guide/Main_Page)
* [10 useful chaining operators in Linux](https://www.tecmint.com/chaining-operators-in-linux-with-practical-examples/)
* awk: https://www.howtogeek.com/562941/how-to-use-the-awk-command-on-linux/amp/
