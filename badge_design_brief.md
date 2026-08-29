# Workout Widget — Badge Design Brief

## App Context
This is a dark-themed fitness tracking app. The badge screen is where users see their achievements. 
Badges sit on dark cards (~#181824 background), displayed in a 2-column grid.
Each badge card is about **160×180 px** on screen.

## Visual Style Guide
**Theme:** Dark fantasy / Greek mythology / Epic comic art  
**NOT:** Cartoons, bright pastels, playful kids-style, flat minimalist icons  
**YES:** Dramatic lighting, bold outlines, cinematic shading, aged metal, fire, stone, cosmic  
**Color palette:** Deep blacks, gold (#FFD700), crimson, bronze, electric blue, purple-violet  
**Mood:** Power, discipline, battle-hardened, mythological grandeur  

## Technical Specs for Each Badge Icon
- **Format:** Transparent PNG, 200×200 px (square)
- **Style:** Rich illustration, NOT flat icon
- **Background:** Transparent — will appear on dark card background
- **Filename:** Use the ID from the table (e.g. `s1.png`, `w50.png`)

---

## STREAK BADGES
*Earned by consecutive weeks of 5+ workouts*

| ID | Name | Description | Visual Concept |
|----|------|-------------|----------------|
| `s1` | First Blood | 1 week | A dripping gladius sword, first drop of blood on the blade — gritty, intense |
| `s2` | Blade Forged | 2 weeks | A single ornate dagger being hammered on an anvil, sparks flying |
| `s4` | Iron Will | 4 weeks | A battle-scarred Spartan shield with a fist dent in the center |
| `s8` | No Days Off | 8 weeks | A skull wearing a laurel wreath, one eye socket glowing red |
| `s13` | War Eagle | 13 weeks | A massive eagle diving with talons extended, feathers razor-sharp |
| `s26` | Poseidon's Tide | 26 weeks | Poseidon's gold trident rising from a churning dark sea |
| `s52` | Undying | 52 weeks | A crowned skull and crossbones, crown of thorns, chains broken |

---

## MONTHLY BADGES
*Earned by hitting 16+ workouts in a calendar month*

| ID | Name | Description | Visual Concept |
|----|------|-------------|----------------|
| `m1` | Zeus Mode | 16+ workouts in a month | Zeus's hand throwing a crackling lightning bolt downward |
| `m2` | Trident | 2 consecutive full months | A golden trident, tines glowing electric blue |
| `m3` | Locked On | 3 consecutive full months | An arrow nocked on a drawn bow, aimed dead center |
| `m6` | Lion's Reign | 6 consecutive full months | A lion's head roaring, wearing a battle-worn crown |
| `m12` | Eye of the Gods | 12 consecutive full months | An all-seeing eye inside a triangle of fire, Greek key border |
| `mt6` | Volcanic Discipline | Any 6 months with 16+ | An erupting volcano at night, lava rivers glowing orange |

---

## WORKOUT COUNT BADGES

| ID | Name | Description | Visual Concept |
|----|------|-------------|----------------|
| `w1` | First Bout | 1st workout | A pair of worn boxing gloves hanging from a hook |
| `w10` | Raw Steel | 10 workouts | A massive muscular arm flexing, veins visible, skin like bronze |
| `w25` | Hammer Down | 25 workouts | A war hammer mid-swing, trailing motion blur |
| `w50` | Battle Worn | 50 workouts | Crossed swords with deep nicks and battle damage, dried blood |
| `w100` | Iron Body | 100 workouts | A bionic mechanical arm flexing — half flesh, half iron machine |
| `w250` | Dragon Born | 250 workouts | A dragon's head exhaling fire, scales gleaming like obsidian |
| `w500` | King of Iron | 500 workouts | An iron throne with a spiked crown sitting on top, glowing embers beneath |

---

## VOLUME BADGES — SETS

| ID | Name | Description | Visual Concept |
|----|------|-------------|----------------|
| `st100` | Bolted In | 100 sets | A massive hex bolt driven into stone |
| `st500` | Full Throttle | 500 sets | A large spinning gear with fire coming off the teeth |
| `st1k` | Hammer Forged | 1,000 sets | A forge hammer striking glowing red-hot steel, sparks erupting |
| `st5k` | Volcanic Output | 5,000 sets | An erupting volcano seen from above, rivers of lava |

---

## VOLUME BADGES — POUNDS LIFTED

| ID | Name | Description | Visual Concept |
|----|------|-------------|----------------|
| `v1k` | First Load | 1,000 lbs | A thick iron weight plate, worn and chalked |
| `v10k` | Forge Master | 10,000 lbs | Crossed forge hammers over an anvil, embers glowing |
| `v100k` | Stone Crusher | 100,000 lbs | A massive fist shattering a boulder, cracks radiating out |
| `v500k` | Mountain Mover | 500,000 lbs | A lone figure pushing the base of a crumbling mountain |
| `v1m` | Ton Club | 1,000,000 lbs | A rocket launching upward through storm clouds |
| `v2m` | Iron Giant | 2,000,000 lbs | A colossal iron colossus figure standing over a city skyline |
| `v5m` | Force of Nature | 5,000,000 lbs | A lightning bolt splitting the earth in two, glowing fissures |
| `v10m` | **ATLAS** *(special)* | 10,000,000 lbs | **See Atlas section below** |

---

## 🌍 ATLAS BADGE — SPECIAL FULL-WIDTH CARD
*This badge is displayed larger than all others — it spans the full width of the screen.*

**Visual concept:** The Greek Titan Atlas, kneeling on a rocky cliff, straining to hold the glowing Earth above his head. Cosmic dark background with nebula and stars. His bronze body is hyperrealistic, massively muscular, glistening with effort. The Earth illuminates him from above with blue-white light.

**Reference style:** Boris Vallejo fantasy oil painting — hyperrealistic, cinematic, dramatic lighting.

**Suggested image size:** 420×520 px (portrait), JPEG, embedded via the `embed_atlas.html` tool.

**The glow:** When this badge is earned, the card pulses with a dramatic gold-to-orange fire glow.

---

## PR BADGES
*Personal records set across all exercises*

| ID | Name | Description | Visual Concept |
|----|------|-------------|----------------|
| `pr1` | First PR | 1st personal record | A golden trophy, polished, with a laurel wreath |
| `pr5` | 5 PRs | 5 records | A silver medal with a battle-axe engraved on it |
| `pr10` | 10 PRs | 10 records | A gold medal with crossed swords engraved |
| `pr25` | Record Slayer | 25 records | A sword slashing through a stone tablet (breaking a record) |
| `pr50` | PR Titan | 50 records | A massive Titan figure holding a trident aloft |
| `pr100` | Eagle Standard | 100 records | A Roman eagle perched atop a battle standard, wings spread |
| `pr250` | Thunderous | 250 records | A dark storm cloud with a massive lightning bolt descending |
| `pr500` | Death to Limits | 500 records | A skull with broken chains dangling from it, fire behind |

---

## VARIETY BADGES

| ID | Name | Description | Visual Concept |
|----|------|-------------|----------------|
| `ex5` | Arsenal Starts | 5 exercises | A rack of 5 different weapons — dagger, sword, bow, axe, spear |
| `ex10` | Range Expands | 10 exercises | A full quiver of arrows, finely fletched |
| `ex20` | Full Arsenal | 20 exercises | A full armory wall filled with weapons of every type |
| `mg5` | Full Beast | 5 muscle groups | A gorilla in full flex, veins popping, absolutely jacked |
| `mg7` | Complete Dragon | All muscle groups | A full dragon body in a power pose, wings spread wide |

---

## CARDIO BADGES

| ID | Name | Description | Visual Concept |
|----|------|-------------|----------------|
| `c1` | First Stride | 1st cardio session | A running shoe with motion blur lines behind it |
| `c5` | Wind Sprint | 5 sessions | A blurred figure running, wind streaks around them |
| `c10` | Taking Flight | 10 sessions | An eagle silhouette soaring upward on a thermal |
| `c25` | Current Rider | 25 sessions | A surfer riding a massive dark wave |
| `c50` | Lightning Legs | 50 sessions | A pair of muscular legs with lightning bolts at the calves |
| `c100` | Cardio Lion | 100 sessions | A lion mid-sprint, mane streaming back, teeth bared |
| `cd10` | 10K Arrow | 10 km | An arrow in perfect flight, tip glowing gold |
| `cd42` | Marathon Beast | 42.2 km | A runner's silhouette crossing the finish line in front of an erupting volcano |
| `cd100` | Century Ride | 100 km | A rocket-powered bicycle leaving a fire trail |

---

## HIIT BADGES

| ID | Name | Description | Visual Concept |
|----|------|-------------|----------------|
| `h1` | Sparked | 1st HIIT session | A single electric spark on a dark background |
| `h5` | HIIT Starter | 5 sessions | A roaring flame, intense and upward |
| `h10` | HIIT Regular | 10 sessions | An explosion burst with shockwave rings |
| `h25` | Tornado | 25 sessions | A dark tornado funnel descending from storm clouds |
| `h50` | Silverback | 50 sessions | A massive gorilla beating its chest, screaming — alpha energy |
| `h100` | HIIT Dragon | 100 sessions | A dragon exhaling a massive cone of fire, eyes glowing |
| `hs100` | 100 Forged | 100 HIIT sets | Crossed forge hammers over glowing hot metal |
| `hs500` | Warrior | 500 HIIT sets | A full-armored warrior standing in battle stance, sword drawn |
| `hs1k` | Reaper | 1,000 HIIT sets | The Grim Reaper with scythe raised, tattered robes, shadowed face |

---

## Prompt Suggestion for Image Generation AI

> "Create a [200×200 px / square] badge icon for a fitness app. Dark fantasy / Greek mythology aesthetic. 
> Transparent background. The icon depicts: [INSERT VISUAL CONCEPT FROM TABLE].
> Style: bold dramatic illustration, cinematic lighting, deep shadows, rich detail — NOT flat, NOT cartoon.
> Color palette: dark backgrounds, gold, bronze, crimson, electric blue accents.
> The icon will appear on a very dark (#181824) card background."

---

## Delivery Format
- **Format:** Transparent PNG, 200×200 px per badge
- **Filename:** Use the badge ID exactly (e.g. `s1.png`, `v10m.png`)
- **Atlas badge:** 420×520 px JPEG (not PNG), no transparency needed — use `embed_atlas.html` to insert it
