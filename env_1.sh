#! /bin/bash

# 替换Windows风格的换行符为Unix风格
sed -i 's/\r$//' env.sh

git lfs install 
# clone代码库
git clone http://oauth2:tbJXojN-wU1fJ9WbBNsZ@www.modelscope.cn/studios/niceLemon/sci-paper-improve-assistant.git
git clone https://github.com/modelscope/modelscope-agent.git

cd modelscope-agent
pip install -r requirements.txt
mv requirement.txt requirement-ma.txt
cp -r apps/agentfabric/* .
pip install -r requirements.txt


# 设置环境变量 ~/.bashrc
echo "--------------|||||||||||||||--------------------------------------------------|||||||||||||||--------------------"
cd ..
cp -r modelscope-agent/* sci-paper-improve-assistant 
cd sci-paper-improve-assistant

python app.py