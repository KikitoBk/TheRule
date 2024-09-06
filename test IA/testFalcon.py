import torch
from transformers import BloomForCausalLM, AutoTokenizer

print("Torch version:", torch.__version__)

# Vérifier l'appareil disponible (GPU ou CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device utilisé:", device)

# Charger le modèle et le tokenizer
model_name = "bigscience/bloom-560m"  # Utilisez un modèle plus petit pour tester
print("Chargement du modèle et du tokenizer...")
model = BloomForCausalLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("Modèle et tokenizer chargés")

# Tokeniser le texte
prompt = "Utilisateur: Bonjour, quel est la capital de la France? \n Réponse:"
inputs = tokenizer(prompt, return_tensors="pt").to(device)
print("Texte tokenisé")

# Générer du texte
try:
    print("Génération du texte...")
    outputs = model.generate(inputs.input_ids, max_length=50)
    print("Texte généré")
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Texte généré:", text)
except Exception as e:
    print(f"Une erreur est survenue: {e}")
