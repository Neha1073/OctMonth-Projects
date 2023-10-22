import openai

# Collect the user's API key
api_key = input("Please enter your OpenAI API key: ")

# Initialize the OpenAI API client
openai.api_key = api_key

# Collect the topic for the article
topic = input("Enter the topic for the article: ")

# Define a prompt for the GPT-3 model
prompt = f"Write an article about {topic}."

# Set the model and configuration
model = "text-davinci-002"  # You can choose other models based on your needs
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=300,  # Adjust as needed
)

# Extract and print the generated article
article = response.choices[0].text
print("Generated Article:")
print(article)
