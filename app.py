import streamlit as st
import random

# Prosty system typowania demo (1X2 + Dokładny wynik + Value)

st.title("⚽ Football AI Pro 1.0")
st.subheader("Automatyczne typy meczowe + Dokładny wynik + Value Bet")

# Przykładowe mecze
matches = [
    {"home": "Arsenal", "away": "Chelsea"},
    {"home": "PSG", "away": "Real Madrid"},
    {"home": "Bayern", "away": "Dortmund"},
]

for match in matches:
    st.markdown(f"### {match['home']} vs {match['away']}")

    # Losowe typy demo (tu podpinamy model AI później)
    prediction = random.choice(["1", "X", "2"])
    exact_score = f"{random.randint(0, 3)}:{random.randint(0, 3)}"
    value_bet = random.choice(["✅ Value Bet", "❌ Brak Value"])

    st.write(f"**Typ AI:** {prediction}")
    st.write(f"**Dokładny wynik:** {exact_score}")
    st.write(f"**Value Bet:** {value_bet}")
    st.write("---")

st.info("Wersja demonstracyjna Football AI Pro 1.0 — pełne AI i value do podpięcia.")
