
import streamlit as st
import pandas as pd
import numpy as np
from unidecode import unidecode

st.set_page_config(page_title="nestR", page_icon="🐣")

st.title("🐣 nestR: the Bird Baby Name Generator")
st.caption("Choose how many babies to name, set vibes & plausibility, then let RNG (with your guidance) pick fun bird-based baby names.")

st.markdown(
    "*Disclaimer: This tool is for entertainment only. "
    "All gender vibes and plausibility judgments are AI generated "
    "and not necessarily the opinions of the creator... Have fun!*"
)
# --- Hardcoded DataFrame ---
data = [
["Robin","normal",40,95,"Already common; gender-neutral classic"],
["Wren","normal",35,92,"Trendy soft girl name"],
["Raven","normal",55,94,"Edgy, unisex"],
["Phoenix","mythological",60,90,"Powerful modern gender-neutral pick"],
["Dove","normal",20,80,"Gentle, feminine"],
["Sparrow","normal",45,88,"Indie/hipster vibe"],
["Jay","normal",65,95,"Common male name"],
["Bluejay","normal",60,50,"Quirky compound, borderline usable"],
["Hawk","normal",85,78,"Rugged boy name trend"],
["Falcon","normal",90,70,"Aggressive masculine name"],
["Finch","normal",50,82,"Literary (Atticus Finch) vibe"],
["Lark","normal",30,87,"Light feminine sound"],
["Starling","normal",35,75,"Feminine nature name"],
["Kite","normal",60,55,"Playful but odd for child"],
["Swallow","normal",35,10,"...unfortunate implications"],
["Titmouse","normal",25,2,"Funniest low-plausibility example"],
["Woodpecker","normal",85,0,"Too anatomical; pure comedy"],
["Puffin","normal",50,40,"Cute nickname vibe"],
["Pelican","normal",65,15,"Gangly mental image"],
["Albatross","normal",70,25,"Heavy symbolic baggage"],
["Egret","normal",40,35,"Soft but odd"],
["Heron","normal",55,65,"Cool, sleek sound"],
["Crane","normal",60,58,"Asian symbolism; plausible surname"],
["Swan","normal",25,60,"Graceful but a little too nouny"],
["Goose","normal",70,5,"Comic insult associations"],
["Gander","normal",85,15,"Very masculine farm uncle energy"],
["Pigeon","normal",55,20,"Urban pest reputation"],
["Crow","normal",70,65,"Gothic appeal"],
["Rook","normal",60,55,"Sharp, medieval"],
["Magpie","normal",45,40,"Cute but silly"],
["Oriole","normal",40,55,"Pretty sound, plausible"],
["Cardinal","normal",65,70,"Strong, churchy"],
["Canary","normal",25,45,"Vintage but unlikely"],
["Peacock","normal",50,5,"Self-absorbed vibes"],
["Hen","normal",20,10,"Too barnyard"],
["Rooster","normal",95,0,"Would make roll call hilarious"],
["Chickadee","normal",25,20,"Adorable nickname only"],
["Osprey","normal",75,55,"Powerful outdoorsy"],
["Eagle","normal",90,45,"Patriotic but weird as name"],
["Condor","normal",80,35,"Dramatic, villain-like"],
["Vulture","normal",95,0,"Zero chance, metal band maybe"],
["Parrot","normal",50,10,"Too literal"],
["Macaw","normal",60,25,"Colorful, exotic"],
["Cockatoo","normal",55,2,"Funny word, not a name"],
["Cockatiel","normal",40,2,"Slightly cuter, still no"],
["Toucan","normal",50,15,"Cartoonish"],
["Kiwi","flightless",30,75,"Actually used in NZ nickname form"],
["Emu","flightless",70,10,"Impossible not to laugh"],
["Ostrich","flightless",65,15,"Clumsy mental image"],
["Cassowary","flightless",80,5,"Sounds like a dinosaur"],
["Moa","flightless",50,25,"Cool ancient vibe"],
["Dodo","flightless",40,5,"Adorable but insulting"],
["Penguin","flightless",50,25,"Cute but silly"],
["Pidgey","Pokemon",45,70,"Cute and believable nickname"],
["Pidgeotto","Pokemon",70,25,"Too Italian-sounding for real name"],
["Pidgeot","Pokemon",80,20,"Macho but fake"],
["Spearow","Pokemon",75,30,"Sounds edgy"],
["Fearow","Pokemon",85,15,"Villainous"],
["Murkrow","Pokemon",60,35,"Gothic fantasy usable"],
["Honchkrow","Pokemon",95,10,"Mafia boss energy"],
["Swablu","Pokemon",40,55,"Whimsical girl vibe"],
["Altaria","Pokemon",35,70,"Could pass for fantasy girl name"],
["Talonflame","Pokemon",90,5,"Too metal"],
["Rowlet","Pokemon",50,65,"Cuddly neutral"],
["Dartrix","Pokemon",80,25,"Sounds like edgy gamer tag"],
["Decidueye","Pokemon",85,5,"Absolutely unpronounceable"],
["Noctowl","Pokemon",75,15,"Sleep-aid commercial vibe"],
["Corviknight","Pokemon",90,10,"Badass, implausible"],
["Chatot","Pokemon",50,40,"Silly but musical"],
["Ducklett","Pokemon",45,60,"Sweetly absurd, could be toddler nickname"],
["Swanna","Pokemon",25,70,"Elegant girl name vibe"],
["Rufflet","Pokemon",60,45,"Boyish but odd"],
["Braviary","Pokemon",85,15,"Sounds like fantasy hero title"],
["Articuno","Pokemon",55,30,"Legendary, exotic"],
["Zapdos","Pokemon",80,5,"Comic-book villain"],
["Moltres","Pokemon",75,10,"Fiery but fake"],
["Ho-Oh","Pokemon",50,0,"Unfortunate sound"],
["Lugia","Pokemon",40,65,"Could almost be a girl name"],
["Yveltal","Pokemon",90,10,"Heavy metal stage name"],
["Cramorant","Pokemon",70,10,"Weird uncle energy"],
["Bombirdier","Pokemon",85,0,"Baby name explosion waiting to happen"],
["Flamigo","Pokemon",60,25,"Punny 'flamingo' copy, cute but weird"],
["Oricorio","Pokemon",40,40,"Musical rhythm vibe"],
["Farfetch’d","Pokemon",70,2,"Apostrophe kills it"],
["Togekiss","Pokemon",35,60,"Sounds sugary sweet"],
["Delibird","Pokemon",60,20,"Christmas mascot energy"],
["Hawlucha","Pokemon",85,25,"Sounds like Lucha Libre hero"],
["Skarmory","Pokemon",80,20,"Spiky, edgy"],
["Xatu","Pokemon",65,45,"Tribal-sounding, short"],
["Archeops","Pokemon",90,10,"Fossil warrior vibe"],
["Roc","mythological",80,65,"Strong, short mythic"],
["Simurgh","mythological",60,35,"Persian myth, exotic"],
["Garuda","mythological",90,75,"Legit male name in SE Asia"],
["Thunderbird","mythological",85,20,"Cool but too superhero-like"],
["Bennu","mythological",50,60,"Egyptian myth; mysterious"],
["Firebird","mythological",55,40,"Ballet associations"],
["Huma","mythological",45,55,"Persian lucky bird; sounds usable"],
["Fenghuang","mythological",50,30,"Hard to pronounce for English use"],
["Caladrius","mythological",70,15,"Latin tongue-twister"],
["Alicanto","mythological",65,45,"Chilean myth; melodic"],
["Valkyrie","mythological",40,85,"Already used as girl name"],
["Siren","mythological",30,75,"Common myth-bird hybrid name"],
["Harpy","mythological",25,20,"Negative but fun insult"],
["Griffin","mythological",85,95,"Real boy name already"],
["Hippogriff","mythological",70,5,"Too long and silly"],
["Ziz","mythological",65,25,"Short, strange Hebrew myth bird"],
["Anzu","mythological",60,55,"Japanese use plausible"],
["Karura","mythological",60,60,"Japanese deity name, works regionally"],
["Aello","mythological",35,70,"Greek feminine harpy; nice sound"],
["Celaeno","mythological",40,65,"Elegant Greek feel"],
["Alkonost","mythological",45,35,"Slavic legend, clunky in English"],
["Sirin","mythological",35,60,"Lovely Russian feminine name"],
["Aethon","mythological",80,50,"One of Helios’s fire-birds; plausible"],
["Phoenixia","mythological",30,75,"Feminized fantasy name"],
["Ardea","normal",40,70,"Latin genus, elegant"],
["Tern","normal",50,35,"Short but blunt"],
["Gull","normal",65,20,"Too Seagullish"],
["Gannet","normal",60,25,"Awkward '-et' ending"],
["Kestrel","normal",45,85,"Actually rising as girl name"],
["Merlin","normal",70,95,"Already popular male name"],
["Swift","normal",60,80,"Athletic unisex option"],
["Nightjar","normal",55,30,"Too goth, but cool"],
["Nighthawk","normal",85,40,"Vigilante vibe"],
["Chick","normal",60,0,"Please don’t"],
["Henna","normal",25,90,"Already name, fits"],
["Peahen","normal",35,10,"Strange combo"],
["Lovebird","normal",40,20,"Cute but cringy"],
["Kingfisher","normal",80,35,"Grand, British pub vibe"],
["Bittern","normal",65,15,"Sounds like 'bitter'"],
["Grebe","normal",50,5,"Ugly phonetics"],
["Rail","normal",60,5,"Infrastructure confusion"],
["Quail","normal",55,65,"Short, quirky"],
["Turaco","normal",45,50,"Exotic rhythm"],
["Motmot","normal",50,25,"Childlike repetition"],
["Hoatzin","normal",60,15,"Sci-fi pronunciation"],
["Lyrebird","normal",50,35,"Musical potential"]
]
df = pd.DataFrame(data, columns=["Bird Name","Category","Gender Vibe (0–100♂)","Name Plausibility (0–100)","Notes"])

# Normalize category for matching (remove accents, title-case primary labels)
def normalize_category(cat: str) -> str:
    c = unidecode(str(cat)).strip().lower()
    mapping = {
        "normal": "Normal",
        "flightless": "Flightless",
        "pokemon": "Pokemon",
        "pokmon": "Pokemon",
        "mythological": "Mythological"
    }
    return mapping.get(c, cat)

df["NormCategory"] = df["Category"].apply(normalize_category)

# Utility bucketing
def gender_bucket(score):
    if score <= 40:
        return "F"
    if score >= 60:
        return "M"
    return "Neutral"

def plaus_bucket(score):
    if score < 33:
        return "Low"
    if score <= 66:
        return "Medium"
    return "High"

def plaus_label(score):
    if score < 33:
        return "Implausible"
    if score <= 66:
        return "In-between"
    return "Plausible"

# Sidebar controls
st.sidebar.header("Controls")

num_babies = st.sidebar.slider("How many babies?", min_value=1, max_value=6, value=3, step=1)

rand_degree = st.sidebar.slider("Degree of randomness (higher = wilder)", min_value=0, max_value=100, value=30, step=1)

randomize_all = st.sidebar.button("🎲 Randomize all settings")

st.sidebar.divider()
st.sidebar.caption("Tip: 'Random' ignores that filter but still lets other choices bias the pick. Higher randomness flattens the biases.")

# Options
gender_opts = ['M','F','Neutral','Random']
plaus_bucket_opts = ['High','Low','Medium','Random']
category_opts = ['Normal','Flightless','Mythological','Pokemon','Random']
plaus_label_opts = ['Plausible', 'Implausible', 'In-between', 'Random']

# Per-baby configuration
configs = []
for i in range(num_babies):
    with st.expander(f"Baby #{i+1} settings", expanded=(i==0)):
        if randomize_all:
            g = np.random.choice(gender_opts)
            pb = np.random.choice(plaus_bucket_opts)
            cat = np.random.choice(category_opts)
            pl = np.random.choice(plaus_label_opts)
        else:
            g = st.selectbox("Gender (ChatGPT perceived)", gender_opts, index=3, key=f"g_{i}")
            pb = st.selectbox("Plausibility (High/Low/Medium)", plaus_bucket_opts, index=3, key=f"pb_{i}")
            cat = st.selectbox("Category", category_opts, index=4, key=f"cat_{i}")
            pl = st.selectbox("Plausibility (Plausible/Implausible/In-between)", plaus_label_opts, index=3, key=f"pl_{i}")
        configs.append({
            "gender": g,
            "plaus_bucket": pb,
            "category": cat,
            "plaus_label": pl
        })

def weighted_pick(available_df, cfg, temperature):
    # Compute weights
    weights = np.ones(len(available_df), dtype=float)

    # Category bias
    if cfg["category"] != "Random":
        match = (available_df["NormCategory"] == cfg["category"])
        weights *= np.where(match, 3.0, 0.3)

    # Gender vibe bias
    if cfg["gender"] != "Random":
        target = cfg["gender"]
        gb = available_df["Gender Vibe (0–100♂)"].apply(gender_bucket)
        match = (gb == target)
        weights *= np.where(match, 2.0, 0.5)

    # Plausibility bucket bias (High/Medium/Low)
    if cfg["plaus_bucket"] != "Random":
        pb = available_df["Name Plausibility (0–100)"].apply(plaus_bucket)
        match = (pb == cfg["plaus_bucket"])
        weights *= np.where(match, 2.0, 0.5)

    # Plausibility label bias (Plausible/Implausible/In-between)
    if cfg["plaus_label"] != "Random":
        pl = available_df["Name Plausibility (0–100)"].apply(plaus_label)
        match = (pl == cfg["plaus_label"])
        weights *= np.where(match, 2.0, 0.5)

    # Avoid zero weights
    if np.all(weights == 0) or np.any(~np.isfinite(weights)):
        weights = np.ones(len(available_df), dtype=float)

    # Temperature scaling: higher temperature -> flatter distribution
    # Map UI 0..100 to temperature 0.5..2.0
    T = 0.5 + (temperature/100.0)*1.5
    # Convert to probabilities via softmax with temperature
    logits = np.log(weights + 1e-12)
    probs = np.exp(logits / T)
    probs = probs / probs.sum()

    idx = np.random.choice(available_df.index.values, p=probs)
    return int(idx)

# Action button
if st.button("✨ Pick Names"):
    results = []
    used_indices = set()

    for i, cfg in enumerate(configs):
        # Exclude already-chosen names
        available_df = df.drop(index=list(used_indices)) if used_indices else df
        if available_df.empty:
            st.error("Ran out of unique names to choose from.")
            break

        idx = weighted_pick(available_df, cfg, rand_degree)
        name = available_df.loc[idx, "Bird Name"]
        notes = available_df.loc[idx, "Notes"]
        category = available_df.loc[idx, "NormCategory"]

        # Track original index to avoid duplicates
        original_idx = df.index[df["Bird Name"] == name][0]
        used_indices.add(original_idx)

        results.append({
            "Baby": f"Baby #{i+1}",
            "Name": name,
            "Category": category,
            "Commentary": notes
        })

    if results:
        st.subheader("Your Picks")
        for res in results:
            with st.container(border=True):
                st.markdown(f"**{res['Baby']}** — **{res['Name']}**  \n*Category:* {res['Category']}  \n*Commentary:* {res['Commentary']}")

    with st.expander("See full source table (scores hidden in UI request, but available if you need them):"):
        st.dataframe(df[["Bird Name","NormCategory","Notes"]].rename(columns={"NormCategory":"Category"}))

else:
    st.info("Set your preferences, then click **Pick Names**.")

st.sidebar.divider()
st.sidebar.subheader("About")
st.sidebar.write("This app uses a weighted random picker over a hardcoded 150-name bird table (real species, flightless, Pokémon, mythological). Your choices bias the RNG; the 'Degree of randomness' slider flattens or sharpens the bias.")
