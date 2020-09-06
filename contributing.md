# How to start developing

To develop this automation, you'll need to first clone the repository on to your computer. For new Git users, see the [Using Git](#using-git) section below. <br><br>

## Working with GitHub Issues

1. If you find a problem with `jekyll-gather-data-types` look to see if there is an open issue addressing the problem, if not [create a new issue](https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue).

1. If you want to help fix this issue, declare your intention of working on the issue by commenting on the issue.

1. [Fork the repository](#Fork-the-repository) and begin development on your own [feature branch](Work-on-an-issue-using-git).

1. Update the issue with images depicting the result of your changes. Then create a pull request to merge your code from your fork to the main repository.

## Using Git

This section discusses some tips and best practices for working with Git.

### Making changes, committing and pushing

1. Generally changes start on your local clone of your fork of this repository, in your own branch.

1. Commit your changes with a comment related to the issue it addresses to your local repository.

1. Push that commit(s) to your online GitHub fork.

1. From the `jekyll-gather-data-types` repository, create a Pull Request which asks `jekyll-gather-data-types` to pull changes from your fork into the `develop` branch of the repository.

#### Fork the repository

In https://github.com/100Automations/jekyll-gather-data-types, look for the fork icon in the top right. Click it and create a fork of the repository.

For git beginners, a fork is a copy of the repository that will be placed on your GitHub account url.

It should create a copy here: https://github.com/your_GitHub_user_name/jekyll-gather-data-types, where `your_GitHub_user_name` is replaced with exactly that.

Note that this copy is on a remote server on the GitHub website and not on your computer yet.

If you click the icon again, it will not create a new fork but instead give you the URL associated with your fork.

#### Clone your online repository to your local computer

For git beginners, this process will create a third copy of the repository on your local desktop.

First create a new folder on your desktop that will contain `100automation` projects.

In your shell, navigate there then run the following commands:

```bash
git clone https://github.com/your_GitHub_user_name/jekyll-gather-data-types.git
```

You should now have a new folder in your `100automation` folder called `jekyll-gather-data-types`.

Verify which URL your `origin` remote is pointing to:

```bash
git remote show origin
```

If you accidentally cloned the `100automation/jekyll-gather-data-types.git` then you can correct that with the following two commands: 

1) Change your local copy to upload to your fork with the following:

```bash
git remote set-url origin https://github.com/your_user_name/jekyll-gather-data-types.git
```

2) Add another remote called `upstream` that points to the `100automation` version of the repository. This will allow you to incorporate changes later:

```bash
git remote add upstream https://github.com/100automation/jekyll-gather-data-types.git
```

#### Work on an issue using git

Create a new branch for each issue you work on. Doing all your work on feature branches leaves your repository's main branch (named `master`) unmodified and greatly simplifies keeping your fork in sync with the main project.

a) Check current branch

The `git branch` command will let you know what branch you are in, and what branch names are already in use.

```bash
git branch
```

You will see a list of all of your branches. There will be a star (`*`) next to the branch that you are currently in. By default you should start on the `master` branch.

b) Pull the develop branch from the repo and switch to it
```bash
git pull origin develop
```
then switch to the develop branch
```bash
git checkout develop
```

c) Create a new branch where you will work on your issue

The `git checkout` command will create and change to a new branch where you will do the work on your issue.  In git, the checkout command lets you navigate between different branches.  Using the `-b` flag you can create a new branch and immediately switch into it. 

To create a new issue branch, and switch into it: 

```bash
git checkout -b fix-logo-width-311
```

The text after the `-b`, in the example `fix-logo-width-311`, will be the name of your new branch. Choose a branch name that relates to the issue you're working on. (No spaces!)

The format should look like the scheme above where the words are a brief description of the issue that will make sense at a glance to someone unfamiliar with the issue. 

No law of physics will break if you don't adhere to this scheme, but laws of git will break if you add spaces.

When you've finished working on your issue, follow the steps below to prepare your changes to push to your repository. 

d) Prepare your changes to push to your repository

Once you are done with the work on your issue you will push it to your repository.  Before you can push your work to your repository, you will stage and commit your changes.  These two commands are similar to the save command that you have used to in other programs. 

-Use the `git add` command to stage your changes.  
This command prepares your changes before you commit them. You can stage files one at a time using the filename, or you can use the `.` to stage all of the files that you have added or made changes to. 

Run the command: 
```bash
git add .
```

-Use the `git status` command to see what files are staged. 

This command will list the files that have been staged.  These are the files that will be committed (saved) when you run the next command, `git commit`. 
```bash
git status
```

-Use the `git commit` command

This command saves your work, and prepares it to push to your repository.  Use the `-m` flag to quickly add a message to your commit. Your message should be a short description of the issue you are working.  It will be extremely helpful if other people can understand your message, so try to reisst the temptation to be overly cryptic.

To commit your changes with a message, run:
```bash
git commit -m “insert message here”
```

Congratulations!  You are now ready to push your work to your repository. 

#### Check upstream before you push

Before you push your local commits to your repository, check to see if there have been updates made in the main Jekyll - Gather Data Types repository. `git fetch` will check remote repositories for changes without altering your local repository.

```bash
git fetch upstream
```

##### No changes in the upstream repository

If you do not see any output, there have not been any changes in the
main Jekyll - Gather Data Types repository since the last time you
checked. So it is safe to push your local commits to your fork.

If you just type `git push` you will be prompted to create a new branch in your GitHub repository. The more complete command below will create a new branch on your copy of the website repository, and then push your local branch there. The name at the end of this command should be the same as the name of the local branch that you created earlier, as in the example below:  

```bash
git push --set-upstream origin fix-logo-width-311
```

##### Step 7b conflicting changes in the upstream repository

When you check the upstream repository, you may see output like this:

```bash
Fetching upstream
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 11 (delta 5), reused 7 (delta 4), pack-reused 0
Unpacking objects: 100% (11/11), 8.25 KiB | 402.00 KiB/s, done.
From https://github.com/100automation/jekyll-gather-data-types
 + 770d667...14f9f46 Bonnie     -> 100automation/Bonnie  (forced update)
 * [new branch]      bonnie     -> 100automation/bonnie
   5773ebe..0c86ecd  develop   -> 100automation/develop
```

You can safely ignore changes in other issue branches, such as
`bonnie` above. But if you see changes in develop, as in
`5773ebe..0c86ecd  develop   -> 100automation/develop`, you should
incorporate those changes into your repository before merging or
rebasing your issue branch. Use the [instructions below](#incorporating-changes-from-upstream)
to bring your fork up to date with the main repository.


### Incorporating changes from upstream

Your fork of this repository on GitHub, and your local clone of that fork, will
get out of sync with this (upstream) repository from time to time.  (That's what has happend when you see something like "This branch is 1 commit behind 100automation:develop" on the github website version of your jekyll-gather-data-types repository.)

One way to keep your fork up to date with this repository is to follow
these instruction: [Syncing your fork to the original repository via the browser](https://github.com/KirstieJane/STEMMRoleModels/wiki/Syncing-your-fork-to-the-original-repository-via-the-browser)

You can also update your fork via the local clone of your fork, using
these instructions. Assuming you have a local clone with remotes
`upstream` (this repo) and `origin` (your GitHub fork of this repo):

First, you will need to create a local branch which tracks upstream/develop.  You will only need to do this once; you do not need to do this every time you want to incorporate upstream changes. 

Run the following two commands: 

```bash
git fetch upstream
git checkout -b upstream-develop --track upstream/develop
```

If you have already created the branch upstream-develop, the following commands will incorporate upstream changes: 

```bash
git checkout upstream-develop # Move to the branch you want to merge with. 
git pull  # This updates your tracking branch to match the develop branch in this repository
git checkout develop  # Move back to your develop branch
git merge upstream-develop  # Merge to bring your develop current. 
```
If you do all your work on topic branches (as suggested above) and keep gh-develop free of local modifications, this merge should apply cleanly.

Then push the merge changes to your GitHub fork:  

```bash
git push
```
If you go to your online github repository this should remove the message "This branch is x commit behind 100automation:develop".

#### Incorporating changes into your feature branch

To incorporate these updates from the main GitHub repository into your
feature branch, you can 'rebase' your branch onto your updated develop
branch. NOTE you should only rebase if you have never pushed your
topic branch to GitHub (or shared it with another collaborator).

```bash
git checkout fix-logo-width-311
git rebase develop
```

If you receive warnings about conflicts, abort the rebase with `git
rebase --abort` and instead merge develop into your branch.

```bash
git checkout fix-logo-width-311
git merge develop
```

#### Step 8 Complete the pull request

```bash
git push --set-upstream origin fix-logo-width-311
```

Now create a new pull request to ask for your updates to be
incorporated. Go to
https://github.com/100automation/jekyll-gather-data-types/pulls and click on "New pull
request". Please rename your pull request something descriptive i.e. "Adding help flag to command line interface".
Also, since your changes are not in the 100automation/jekyll-gather-data-types
repostory, you need to click the "compare across forks" link in the
first paragraph to make you repository and your new branch
available. Review the changes that will be included in the pull
request and, if it fixes a specific issue, include `Fixes #140` in the
pull request message so the issue will be closed automatically once
your pull request is accepted and merged.

Once you have finished working on the issue you have chosen, commit
the changes to your local branch (e.g. `fix-logo-width-311`).
