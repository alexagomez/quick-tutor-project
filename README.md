# Quick Tutor


# terminal instructions
## to push to YOUR branch (DO NOT PUSH TO MASTER pls)
    1. git checkout your_branch_name
       1. if you don't have branch yet: 'git checkout -b your_branch_name'
    2. git add .
    3. git commit -m "sentence about changes you made"
    4. git pull origin master
       1. Fix all merge conflicts on your local after doing this
    5. git push origin your_branch_name


## how to run on local
    1. python migrate.py migrate
       1. To init database changes (don't always need to do this)
    2. python migrate.py runserver
    3. go to localhost:8000 in browser