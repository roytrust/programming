## Linux/Unix
### Tips
* Check executable: `type cmd`. Real path: `realpath pth`
* Check functions: `typeset -f; typeset -f func`
* ldd /bin/ls
* ps aux; ps ef
* memory: free
* boot time: who -b; last reboot; last -x
* [conditionals](https://www.cyberciti.biz/faq/ksh-if-command-examples/): `[ -d tests ] && echo exists`
* set var on condition: `V=$([ -n "$V1"] && echo "some val" || echo "")`
* last working dir: `cd -`; home dir: `cd ~`
* only if success: `cmd1 && cmd2`; Return on error: `cmd || return $?`
* last arg: `alt+.`
* set up default group for creating file: newgrp grp
* Get file size: `find . -type f -exec du -b {} + | awk '{sum+=$1} END{print sum}'` (The difference between ; and + is that with ; a single command for each file is executed whereas with + as many files as possible are given as parameters at once).
* Find by size: `find . -type f -size +30M -size -40M -exec ls -l {} +`. By time newer n days: `-ctime -n`; +n older
* du sort by size: `du -hs * | sort -h`
* Test variable not exists: `if [ -z "$VAR" ]; then; echo not-exists; fi`
* `sed -n 's%.* GET /product/\([0-9]\{5\}\)/.*%\1%p'`
* Count occurrence: `awk -v OFS=',' '{a[$1]++}END{for(i in a){print i, a[i]}}' `
* Sort: `sort -t, -n -r -k2 -k1`
* Show binary: `xxd -l 10 file`
* Redirect: cmd > file 2>&1
* gmt date in iso format: `date -u -d "now + 5mins" +"%Y-%m-%dT%H:%M"`
* Epoch time: seconds `date +%s`, millisec `date +%s%3N`
* Network: netstat -tulpn | grep LISTEN. lsof -i -P -n | grep LISTEN
* Unzip into a different dir: `STEM=$(basename "${f}" .gz); gunzip -c "${f}" > $THERE/"$STEM"
* Change loop delimiter: `IFS=,; for f in $files; do ech $f; done; unset IFS`
* Add a string after each line in a file: `sed -e 's/$/sting/' -i file`
* Get first column: `cut -f1`
* Unzip tar file and skip existing files: `tar --skip-old-files -xv -f file.tar.gz -C dir/`
* Remove/cut first n chars: `${var:1}`. Exclude by pattern: `${var#p}`
* [How to detect if a script is being sourced](https://stackoverflow.com/questions/2683279/how-to-detect-if-a-script-is-being-sourced): `case ${0##*/} in dash|-dash|bash|-bash|ksh|-ksh|sh|-sh) IS_SOURCED=1;; esac`
* [Test IO disk/storage performance/speed](https://www.cyberciti.biz/faq/howto-linux-unix-test-disk-performance-with-dd-command/): `dd if=/dev/zero of=testfile bs=1M count=1000; dd if=testfile of=/dev/null bs=8k`
* Check system services: `systemctl status sendmail`

### Shell expansion
* Pathname Expansion: echo *; echo [[:upper:]]*
* Arithmetic Expansion: echo $((1+2)); 
* brace expansion: echo {a,b,c}_back; echo {1..5}; echo {z..a}; 
* Command Substituation: file $(ls /usr/bin/* | grep bin/zip)
* Double quotes suppress word-splitting
* Single Quotes suppress all expansions.
* Backslash to escape
* Set default variable: `VAR=${2-text}`. 
* `[[ $# -eq ]] && { echo "Usage: $0 format"; exit 1; }`
* Numberic comparison: `[[ $a -lt $b ]] && echo ok`. alphabetic comparison: `[[ $a < $b ]] && echo ok`
* http://linuxcommand.org/lc3_lts0080.php
* [Shell Parameter Expansion](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)
* 

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
* Map network drive: `net use m: path /persistent:yes`
* `runas /user:username explorer`
* Check user: `net user username /domain 2>&1 | findstr changeable`
* Timing: Measure-Command {script | Out-Default}

## Reference
* [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)
* [Linux shell scripting tutorial](https://bash.cyberciti.biz/guide/Main_Page)
* [10 useful chaining operators in Linux](https://www.tecmint.com/chaining-operators-in-linux-with-practical-examples/)
* awk: https://www.howtogeek.com/562941/how-to-use-the-awk-command-on-linux/amp/
* [curl](https://curl.se/docs/httpscripting.html)
