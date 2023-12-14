git lfs install
git clone http://oauth2:tbJXojN-wU1fJ9WbBNsZ@www.modelscope.cn/studios/modelscope/AgentFabric.git
git clone https://github.com/modelscope/modelscope-agent.git

cd modelscope-agent
pip install -r requirements.txt


cp -r apps\agentfabric\* .
pip install -r requirements.txt


# 设置环境变量 ~/.bashrc
