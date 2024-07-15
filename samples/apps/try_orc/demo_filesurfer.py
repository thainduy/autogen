from autogen import config_list_from_json
from autogen.agentchat.contrib.file_surfer.file_surfer import FileSurferAgent
from autogen import UserProxyAgent


llm_config = {"config_list": config_list_from_json("OAI_CONFIG_LIST")}

filesurfer = FileSurferAgent(name="File Surfer", llm_config=llm_config)

user = UserProxyAgent(
    name="User",
    human_input_mode="ALWAYS",
    is_termination_msg=lambda msg: "TERMINATE" in msg.get("content", ""),
)

task = input("Enter a task: ")
user.initiate_chat(filesurfer, message=task)