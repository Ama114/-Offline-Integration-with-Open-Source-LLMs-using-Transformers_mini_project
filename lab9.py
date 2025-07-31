from transformers import pipeline

# Load model and tokenizer locally
generator = pipeline("text-generation", model="gpt2")

# New prompt for blog titles
prompt = "3 possible titles for a blog post on 'climate change and technology:"

# Generate 3 sequences
output = generator(prompt, max_length=20, num_return_sequences=3)

# Print each generated title
print("Generated Blog Titles:")
for i, result in enumerate(output):
    print(f"{i+1}. {result['generated_text'].strip()}")
