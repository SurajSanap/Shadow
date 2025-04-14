import json
import re
from typing import Dict, List, Optional

# Load response framework rules
with open("chunks/response_framework_chunks.json", "r") as f:
    RULES = json.load(f)

AGENT_PROFILE = {
    "1": {"greeting": "Salute, Shadow Cadet.", "style": "instructive"},
    "2": {"greeting": "Bonjour, Sentinel.", "style": "tactical"},
    "3": {"greeting": "Eyes open, Phantom.", "style": "strategic"},
    "4": {"greeting": "In the wind, Commander.", "style": "coded"},
    "5": {"greeting": "The unseen hand moves, Whisper.", "style": "cryptic"},
}

FIXED_PHRASE_RESPONSES = {
    "Omega Echo": "The shadow moves, but the light never follows.",
    "The bridge is burning": "What was built must sometimes fall. What rises next is the real question.",
    "Candle Shop": "It was always there, wasn't it?",
    "Project Requiem": "The song has already been played. You just weren't listening.",
    "The Hollow Man": "Emptiness echoes loudest in those who listen.",
    "Cipher Delta": "Some doors require no keys, only the right whispers."
}

def apply_agent_rules(agent_level: str, query: str, retrieved_chunks: list) -> str:
    greeting = AGENT_PROFILE[agent_level]["greeting"]
    style = AGENT_PROFILE[agent_level]["style"]
    
    if not retrieved_chunks:
        return f"{greeting}\n❌ No data found for your query."
    
    best_chunk = max(retrieved_chunks, key=lambda x: len(x["text"]))
    full_text = best_chunk["text"]
    
    # --- Level 1 (Basic Cadet) ---
    if agent_level == "1":
        simplified = "\n".join([
            line for line in full_text.split("\n") 
            if not any(kw in line.lower() for kw in ["classified", "compromise", "protocol"])
        ])[:300]
        return f"{greeting}\n📘 TRAINING EXCERPT:\n\n{simplified}..."

    # --- Level 5 (Ultra Clearance) ---
    elif agent_level == "5":
        key_points = [
            f"• {line.strip()}" 
            for line in full_text.split("\n") 
            if any(kw in line.lower() for kw in ["protocol", "execute", "classified"])
        ][:3]
        obscured = "\n".join(f"§ {phrase} §" for phrase in full_text.split(". ")[:3])
        return (
            f"{greeting}\n🌑 ULTRA-CLEARANCE BRIEFING:\n\n"
            f"{obscured}\n\n"
            f"«The rest is written between the lines»\n\n"
            f"🔮 KEY PROTOCOLS:\n" + "\n".join(key_points)
        )

    # --- Levels 2-4 ---
    else:
        if style == "coded":
            wrapped = f"[ENCRYPTED]\n{full_text}\n[END ENCRYPTED]"
        elif style == "strategic":
            wrapped = f"🧠 STRATEGIC BRIEF:\n{full_text}\n\nKEY TAKEAWAY:\n{full_text.split('.')[0]}"
        else:
            wrapped = full_text
            
        return f"{greeting}\n🧠 INTELLIGENCE REPORT:\n\n{wrapped}"

def _generate_analysis(self, text: str) -> str:
    """Generate strategic analysis for ultra-clearance agents"""
    key_points = [
        line for line in text.split("\n") 
        if any(kw in line.lower() for kw in ["protocol", "execute", "classified"])
    ]
    return ("• " + "\n• ".join(key_points[:3]) + 
            "\n\n[Additional analysis available at Terminal-5]")

def style_wrap(text: str, style: str) -> str:
    """Enhanced style differentiation"""
    if style == "cryptic":  # Level 5
        phrases = text.split(". ")
        obscured = "\n".join(f"§ {phrase} §" for phrase in phrases[:3])
        return f"{obscured}\n\n«The rest is written between the lines»"
    
    elif style == "instructive":  # Level 1
        return f"📘 INSTRUCTIONS:\n{text[:300]}{'...' if len(text) > 300 else ''}"
    
    elif style == "strategic":  # Level 3
        return f"🧠 STRATEGIC BRIEF:\n{text}\n\nKEY TAKEAWAYS:\n{text.split('.')[0]}"
    
    return text  # Default