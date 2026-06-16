import os
import glob
import json
import time
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

providers = []
if os.environ.get("ANTHROPIC_API_KEY"):
    import anthropic
    anthropic_client = anthropic.Anthropic()
    providers.append("anthropic")
    print("Enabled Anthropic (Haiku)")
    
if os.environ.get("GEMINI_API_KEY"):
    from google import genai
    gemini_client = genai.Client()
    providers.append("gemini")
    print("Enabled Google GenAI (Gemini 2.0)")

if not providers:
    raise ValueError("Please set ANTHROPIC_API_KEY or GEMINI_API_KEY in .env")

def analyze_with_anthropic(prompt):
    response = anthropic_client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1000,
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def analyze_with_gemini(prompt):
    response = gemini_client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text

def main():
    prompt_template = open("analysis_prompt.md").read()
    files = glob.glob("agents-benchmark/*.md")
    
    print(f"Found {len(files)} AGENTS.md files to analyze.")
    results = []
    
    for i, file_path in enumerate(files):
        with open(file_path, "r", encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        if len(content.strip()) < 50:
            print(f"Skipping {file_path} (too short)")
            continue
            
        prompt = prompt_template.replace("{CONTENT_PLACEHOLDER}", content)
        
        # Round-robin between available providers to distribute token load
        provider = providers[i % len(providers)]
        print(f"[{i+1}/{len(files)}] Analyzing {os.path.basename(file_path)} using {provider}...")
        
        try:
            if provider == "anthropic":
                result_text = analyze_with_anthropic(prompt)
            else:
                result_text = analyze_with_gemini(prompt)
                
            # Clean up backticks if the model ignored formatting instructions
            result_text = result_text.strip()
            if result_text.startswith("```json"):
                result_text = result_text[7:]
            elif result_text.startswith("```"):
                result_text = result_text[3:]
            if result_text.endswith("```"):
                result_text = result_text[:-3]
                
            data = json.loads(result_text.strip())
            data["source_file"] = os.path.basename(file_path)
            results.append(data)
        except json.JSONDecodeError:
            print(f"Failed to parse JSON for {file_path}")
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            
        # Basic rate limiting
        time.sleep(1)
        
    # Save the aggregated structured dataset
    output_file = "analysis_results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
        
    print(f"\nAnalysis complete! Extracted structured insights saved to {output_file}")
    
if __name__ == "__main__":
    main()
