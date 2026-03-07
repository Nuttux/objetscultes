from PIL import Image
import shutil, os

SRC = "/Users/theotortorici/ai-dev/objetscultes/exports/images"
DST_FIG = "/Users/theotortorici/ai-dev/objetscultes/site/images/figurines"
DST_CTX = "/Users/theotortorici/ai-dev/objetscultes/site/images/context"

def composite(color_num, mask_num, name, dst=DST_FIG):
    color = Image.open(f"{SRC}/img-{color_num:03d}.png").convert("RGBA")
    mask = Image.open(f"{SRC}/img-{mask_num:03d}.png").convert("L")
    color.putalpha(mask)
    color.save(f"{dst}/{name}.png")
    print(f"  {name}.png ({color.size[0]}x{color.size[1]})")

# Page 1 - Exhibition hall figurines
print("=== FIGURINES ===")
composite(6, 7, "shakoki-dogu")           # Central goggle-eyed figurine (on pedestal)
composite(12, 13, "mimizuku-dogu")         # Triangle-head with spiral arms
composite(18, 19, "swirl-dogu")            # Small figurine with swirl patterns
composite(24, 25, "seated-warrior")        # Seated figurine with hat
composite(30, 31, "heart-face-dogu")       # Heart-shaped face figurine
composite(36, 37, "thinking-dogu")         # Thinking/sitting figurine
composite(42, 43, "boar-vessel")           # Wild boar figurine (horizontal)
composite(48, 49, "flame-vessel")          # Flame-style Jomon pottery
composite(53, 54, "small-seated-dogu")     # Small meditating figurine
composite(56, 57, "wild-hair-dogu")        # Figurine with wild hair and big eyes
composite(61, 62, "jomon-venus")           # Venus figurine (red, curvy)
composite(67, 68, "tall-striped-dogu")     # Tall thin figurine with striped dress
composite(73, 74, "boar-large")            # Large boar figurine
composite(79, 80, "tattooed-dogu")         # Large standing tattooed figurine (red)

# Page 3/4 unique figurines
composite(179, 180, "dark-venus")          # Dark small venus figurine
composite(184, 185, "mushroom-dogu")       # Small mushroom-head figurine
composite(189, 190, "elegant-dogu")        # Tall elegant figurine (side view)
composite(199, 200, "ornate-dogu")         # Ornate goggle figurine (gray)
composite(204, 205, "owl-dogu")            # Owl-like figurine

# Page 2 - Context/library images
print("\n=== CONTEXT ===")
composite(97, 98, "jomon-pot", DST_CTX)            # Decorated pot with figure
composite(102, 103, "magatama-necklace", DST_CTX)   # Magatama bead necklace
composite(107, 108, "red-beans", DST_CTX)            # Red azuki beans
composite(109, 110, "oak-leaves", DST_CTX)           # Oak leaves and acorns
composite(111, 112, "chestnut-husk", DST_CTX)        # Chestnut in husk
composite(113, 114, "yam-root", DST_CTX)             # Yam/root vegetable
composite(115, 116, "chestnut-leaves", DST_CTX)      # Chestnut leaves
composite(117, 118, "chestnut-nut", DST_CTX)         # Chestnut nut
composite(119, 120, "gourd", DST_CTX)                # Gourd/calabash
composite(124, 125, "thatched-houses", DST_CTX)      # Jomon thatched houses
composite(129, 130, "red-shell", DST_CTX)            # Red ochre shell
composite(134, 135, "shiba-inu", DST_CTX)            # Shiba Inu dogs

print("\nDone!")
