
from autogen.agentchat.assistant_agent import AssistantAgent
from autogen.agentchat.user_proxy_agent import UserProxyAgent
from autogen.oai.openai_utils import config_list_from_json
from autogen.agentchat.groupchat import GroupChat, GroupChatManager

def load_llm_config():
    config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
    return {"config_list": config_list}


if __name__ == "__main__":
    llm_config = load_llm_config()

    # define agents
    ceo_agent = AssistantAgent(name="ceo", system_message="", llm_config=llm_config)
    cto_agent = AssistantAgent(name="cto", system_message="", llm_config=llm_config)
    cpo_agent = AssistantAgent(name="cpo", system_message="", llm_config=llm_config)

    # TODO define programmer, designer, and tester


    user_proxy = UserProxyAgent(
        name="User_proxy",
        system_message="A human admin.",
        code_execution_config={"last_n_messages": 3, "work_dir": "coding"},
        human_input_mode="NEVER",
    )

    # execute Design stage
    groupchat = GroupChat(agents=[user_proxy, ceo_agent, cto_agent, cpo_agent], messages=[], max_round=10)
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)
    user_proxy.initiate_chat(manager, message="download data from https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv and plot a visualization that tells us about the relationship between weight and horsepower. Save the plot to a file. Print the fields in a dataset before visualizing it.")


    # execute Coding stage

    # execute Testing stage

    # execute Documenting stage
                         
