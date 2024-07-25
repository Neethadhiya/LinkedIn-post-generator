import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts.prompt import PromptTemplate

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["api_key"]
gpt3_model = ChatOpenAI(model_name="gpt-3.5-turbo-0125")

st.title("LinkedIn Post Generator - V 🐦")
st.subheader("🚀 Generate LinkedIn post on any topic")

# Initialize session state variables if not already set
if 'topic' not in st.session_state:
    st.session_state.topic = ""

if 'response_content' not in st.session_state:
    st.session_state.response_content = ""

# Input field for topic
st.session_state.topic = st.text_input("Enter the topic", value=st.session_state.topic, key='topic_input')

# Define the prompt template
example_prompt = PromptTemplate(
    input_variables=["topic"], 
    template="""Generate a LinkedIn post based on the following topic. The post should be engaging, 
    informative, and suitable for LinkedIn. It must contain at least 200 words and should not include
     any adult content, harmful topics, or sensitive subjects such as violence or illegal activities
      . Include relevant hashtags and ensure it aligns with professional standards.

Topic: {topic}

The post should be engaging, informative, and suitable for LinkedIn. Include relevant hashtags and make sure it aligns with professional standards.

Example 1:
🤖 {topic} 🤖

As AI technologies advance at an unprecedented pace, ensuring ethical practices and responsible development has never been more crucial. 🌐💡

AI has the power to transform industries, enhance decision-making, and drive innovation. However, with these advancements come significant responsibilities. Here’s what we need to focus on:

Bias and Fairness: Addressing and mitigating bias in AI algorithms to ensure equitable outcomes for all users.
Transparency: Building AI systems that are transparent and explainable, so users understand how decisions are made.
Privacy: Safeguarding user data and ensuring that AI applications respect and protect individual privacy rights.
Accountability: Establishing clear accountability for AI systems and their impacts, promoting ethical practices and trust.
As we integrate AI into our businesses and daily lives, let’s prioritize responsible development and ethical considerations to ensure that these technologies benefit society as a whole. How is your organization addressing AI ethics and responsibility? Let’s share best practices and drive positive change together! 🌍🔍

#AIethics #ResponsibleAI #TechForGood #ArtificialIntelligence #EthicalAI #DataPrivacy #AITransparency

Example 2:
✍️ {topic} ✍️

Artificial Intelligence is revolutionizing the world of creative writing, offering new tools and possibilities for writers. Here’s how AI is shaping the future of storytelling:

Idea Generation: AI tools can assist writers in brainstorming and generating ideas, providing inspiration and helping overcome writer's block with creative prompts and suggestions.
Enhanced Writing Assistance: AI-driven writing assistants offer real-time feedback on grammar, style, and tone, helping writers refine their drafts and improve their craft.
Personalized Content: AI can analyze audience preferences and trends to help tailor stories and content to specific audiences, enhancing engagement and relevance.
Creative Collaboration: AI is enabling new forms of collaboration, where writers and AI systems work together to co-create content, blending human creativity with machine efficiency.
Content Generation: From generating articles and reports to creating entire narratives, AI is capable of producing high-quality text, assisting writers with drafting and expanding their work.
The integration of AI in creative writing is opening doors to innovative storytelling methods and expanding the creative possibilities for writers. How are you exploring the intersection of AI and creativity? Let’s discuss the exciting developments and opportunities in this dynamic field! 🚀📚

#CreativeWriting #AI #Storytelling #WritingTools #TechInWriting #AIWriting #ContentCreation #Innovation

Example 3:
🌐 {topic} 🌐

The metaverse is rapidly evolving, offering exciting new possibilities for virtual interaction, business, and entertainment. 🚀✨

Here are some of the most intriguing developments in the metaverse space:

Enhanced Virtual Experiences: Advancements in VR and AR are creating more immersive and realistic virtual environments, making interactions in the metaverse more engaging than ever.
Digital Economies: The growth of virtual economies is enabling new business models, including virtual real estate, NFTs, and digital goods, offering opportunities for innovation and investment.
Interoperability: Efforts are underway to create a more interconnected metaverse, allowing users to seamlessly move between different virtual spaces and platforms.
Social and Collaborative Tools: New tools are enhancing how we connect and collaborate in virtual spaces, from virtual meetings to social events and collaborative projects.
The metaverse represents a frontier full of potential, transforming how we work, play, and interact. What developments in the metaverse are you most excited about? Let’s discuss how these innovations are shaping the future! 🌟🔮

#Metaverse #VirtualReality #AugmentedReality #DigitalEconomy #Innovation #FutureOfWork #TechTrends


"""
)

if st.button("Generate"):
    # Format the prompt with the user input
    prompt = example_prompt.format(topic=st.session_state.topic)

    # Get the response from the model
    response = gpt3_model.invoke(prompt)
    print(response)
    # Update session state with the response content
    st.session_state.response_content = response.content.strip()

if st.button("Clear"):
    st.session_state.topic = ""
    st.session_state.response_content = ""

if st.session_state.response_content:
    st.write(st.session_state.response_content)
