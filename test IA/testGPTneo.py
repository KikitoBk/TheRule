import torch
from transformers import GPTNeoForCausalLM, AutoTokenizer

# Vérifier si un GPU est disponible et l'utiliser si possible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Utilisation de l'appareil: {device}")

# Charger le modèle GPT-Neo 2.7B et le tokenizer associé
model_name = "EleutherAI/gpt-neo-2.7B"
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Déplacer le modèle vers le device (GPU ou CPU)
model.to(device)

# Définir un prompt pour générer du texte
prompt = "In a distant future, humanity has colonized the stars and established a new civilization."

# Tokeniser le prompt et le déplacer vers le device
inputs = tokenizer(prompt, return_tensors="pt").to(device)

# Générer du texte à partir du modèle
with torch.no_grad():
    outputs = model.generate(inputs.input_ids, max_length=100, do_sample=True, top_k=50)

# Décoder et afficher le texte généré
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
