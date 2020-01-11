python C:/scripts/create.py %1
cd E:/Repos/%1
E:
echo %1 >> README.md
git init 
git remote add origin https://github.com/manakmishra/%1.git
git add README.md
git commit -m "Initial Commit"
git push -u origin master
