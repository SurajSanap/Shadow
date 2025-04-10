import json

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
    "Candle Shop": "It was always there, wasn’t it?",
    "Project Requiem": "The song has already been played. You just weren’t listening.",
    "The Hollow Man": "Emptiness echoes loudest in those who listen.",
    "Cipher Delta": "Some doors require no keys, only the right whispers."
}


def apply_agent_rules(agent_level: str, query: str, retrieved_chunks: list) -> str:
    greeting = AGENT_PROFILE[agent_level]["greeting"]
    style = AGENT_PROFILE[agent_level]["style"]

    # --- Handle fixed phrase triggers ---
    for phrase, response in FIXED_PHRASE_RESPONSES.items():
        if phrase.lower() in query.lower():
            return f"{greeting}\n🔒 *Matched Phrase Trigger*: `{phrase}`\n\n{response}"

    # --- Match rule from rules file (if any) ---
    matched = None
    for rule in RULES:
        if "query_type" in rule and rule["query_type"].lower() in query.lower():
            matched = rule
            break

    # --- If no rule, fallback to retrieved content ---
    if not matched and retrieved_chunks:
        fallback_text = retrieved_chunks[0]["text"]
        return f"{greeting}\n🧠 *Semantic Retrieval Result*:\n\n{style_wrap(fallback_text, style)}"

    if not matched:
        return f"{greeting}\n❌ Oops!! No matching data found."

    # --- Final response from rulebook ---
    rule_response = matched.get("response", "No content in rule.")
    return f"{greeting}\n📜 *Matched Rule*: `{matched.get('query_type', 'Unknown')}`\n\n{style_wrap(rule_response, style)}"


def style_wrap(text: str, style: str) -> str:
    if style == "cryptic":
        return f"{text}\n\nInterpret as you will."
    elif style == "coded":
        return f"[Encrypted transmission...]\n{text}"
    elif style == "strategic":
        return f"🧠 Strategy Brief:\n{text}"
    elif style == "tactical":
        return f"🎯 Tactical Outline:\n{text}"
    else:
        return f"📘 Instructions:\n{text}"
