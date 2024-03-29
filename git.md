### Tips
* diff previous version: `git log -p -1 <path>`
* `git config -l --show-origin; git config --get remote.origin.url`
* Config for win/linux: `git config --global core.filemode false; core.autocrlf input`
* Executable bit: `git ls-files --stage`
* Use rebase instead of merge: `git config --global branch.autosetuprebase always`
* by default _git diff_ compares between working and the index file; _git diff_ can also show us the difference between the working directory and the last commit `git diff HEAD`, or between the index and the last commit `git diff --cached`.
* A file is listed as "Changes to be committed", when is cached in the index file (_git add_). A file is marked "changed but not updated", if it isn’t reflected in the index.
* Branches and [merge conflicts](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts): `git branch; git branch -a #list all; git branch --merge`  
  Merge: a process that unifies the work done in two branches.
* Against remote repo: diff origin/master
* rebase, branch, merge
* Modify the most recent commit: `git commit --amend -m "msg"`
* Clean up local for performance: `git gc; git gc --aggressive --auto`
* Retrieve a file of specific version: `git show REV:path/to/file`. Support commit range: commitA...commitD 

### [Core Concepts](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/)
* blob — contents of a file.
* tree — a directory listing (of blobs and trees).
* commit — a snapshot of the working tree.
* branch — a named reference to a commit. .git/refs/heads
* HEAD — a special pointer to denote active branch. Points to a branch, which in turns points to a commit. .git/HEAD
* A repository (in short: repo) is a collection of commits, each of which is an archive of what the project’s **working tree** looked like at a past date, whether on our machine or someone else’s.
* index == the staging area
* When we `checkout` a branch, `git` populates the **index** with all the file contents that were last checked out into our **working directory** and what they looked like when they were originally checked out.
* [git reset](https://www.freecodecamp.org/news/save-the-day-with-git-reset/)

### Callaborating
* Check remote repo: `git remote -v`
* The refs for local branches are stored in: ./.git/refs/heads/, remote: ./.git/refs/remotes/. `git branch; git fetch <remote> <branch>`

### Typical workflow
```
git branch b1
git rebase master

git checkout master
git merge b1

git stash
git stash pop
git stash list
git stash show -p
git stash drop stash@{1}
```

* patch
```
git log --pretty=oneline -3

# create a patch against master
git format-patch master --stdout > fix.patch

# show the patch - not apply
git apply --stat fix.patch

# test the patch
git apply --check fix.patch

# apply
git am --signoff < fix.patch
```

### The Git object database
* Every object in the Git history is stored under a 40-digit hex name, which is the SHA-1 hash of the object’s contents.

```
git cat-file -t 5419
git cat-file commit 5419

git ls-tree 92b8
git cat-file blob 3b18

cat .git/HEAD
```

### Other core concepts
* keep in mind the difference between "working tree contents", "index file" and "committed tree"
* the HEAD link is supposed to always point to the branch you are working on right now.
* .git/index file is the index that describes your current working tree. Examine index file: `git ls-files --stage`
* by default _git commit_ uses the index to create the commit
* Objects are immutable.

### Commands
```


git log --since="2 weeks ago"
git log -2 -p
git show HEAD
git show HEAD~2

git grep "test"

git update-index --add hello example
git diff-files -p
git write-tree
git diff-index --cached -p HEAD # compares a tree
git tag
# Copy repo
git read-tree --reset HEAD
git update-index --refresh
# Copy repo from remote
rsync -rL ../tuto/.git/ .git
git checkout-index -u -a
# Clone repo
git clone ./tuto/.git/ tuto4
git checkout
# Branch
git checkout -b mybranch


# Merge
git merge -m "Merge work in mybranch" mybranch
git show-branch --topo-order --more=1 master mybranch
git show-branch master mybranch
git merge -m "Merge upstream changes." master
# Merge from remote repo
git pull ../tuto
git config remote.tuto-local.url ../tuto
git pull tuto-local
# Undo
git merge --abort

# Publishing
GIT_DIR=tuto-git.git git init
git push <public-host>:/path/to/tuto-git master

# Packaging
git repack
git count-objects

# Health check
git fsck

# Patch
git format-patch origin
git am
# Keeping a patch series up to date using git rebase
git checkout mywork
git rebase origin
git rebase --continue
git rebase --abort
# Reordering or selecting from a patch series
git format-patch origin
git reset --hard origin
git am *.patch

```
### References
* https://www.atlassian.com/git/tutorials/syncing
* https://backlog.com/git-tutorial/
* Tutorial: https://git-scm.com/docs/gittutorial
* User manual: https://git-scm.com/docs/user-manual.html
* git reset: https://dev.to/char_bone/how-and-when-to-use-git-reset-2om6


