import discord
import asyncio

TOKEN = "your bot token id here"
CHANNEL_ID = 420420420420420 #your channel id here
COOLDOWN = 1  # seconds

KEYWORDS = {
    "acacia boat", "acacia button", "acacia door", "acacia fence", "acacia fence gate",
    "acacia leaves", "acacia log", "acacia planks", "acacia sign", "acacia stairs",
    "acacia trapdoor", "acacia wood", "activator rail", "allium", "andesite",
    "anvil", "arrow", "barrier", "beacon", "bed", "bedrock",
    "bee", "beehive", "beetroot", "beetroot seeds", "bell", "birch boat",
    "birch button", "birch door", "birch fence", "birch fence gate", "birch leaves",
    "birch log", "birch planks", "birch sign", "birch stairs", "birch trapdoor",
    "birch wood", "black concrete", "black dye", "black wool", "blast furnace",
    "bone", "bone block", "bone meal", "book", "bookshelf", "bow", "bread",
    "brewing stand", "brick", "brick block", "bucket", "cactus", "cake",
    "campfire", "carpet", "carrot", "cauldron", "chain", "chest",
    "chest minecart", "chicken", "chiseled quartz block", "chiseled stone bricks",
    "clay", "coal", "coal block", "coal ore", "compass", "comparator",
    "concrete", "concrete powder", "cooked beef", "cooked chicken", 
    "cooked mutton", "cooked porkchop", "cooked rabbit", "cooked fish", 
    "cooked potato", "cookie", "cornflower", "creeper", "crimson fungi",
    "crimson nylium", "crimson roots", "diamond", "diamond block", 
    "diamond ore", "dirt", "dispenser", "dragon egg", "dried kelp", 
    "dried kelp block", "dropper", "emerald", "emerald block", 
    "emerald ore", "end portal", "end rod", "ender chest", "ender eye", 
    "enderman", "experience", "experience bottle", "farmland", "fence", 
    "fence gate", "fire", "firework", "fishing rod", "furnace", 
    "glass", "glowstone", "glowstone dust", "gold", "gold block", 
    "gold ore", "golden apple", "golden carrot", "golden helmet", 
    "golden sword", "granite", "grass", "grass block", "gravel", 
    "grey concrete", "hay bale", "honey", "honey block", "honeycomb", 
    "iron", "iron block", "iron door", "iron helmet", "iron ingot", 
    "iron pickaxe", "iron shovel", "iron sword", "jungle boat", 
    "jungle button", "jungle door", "jungle fence", "jungle fence gate",
    "jungle leaves", "jungle log", "jungle planks", "jungle sign", 
    "jungle stairs", "jungle trapdoor", "jungle wood", "lapis lazuli", 
    "lapis lazuli block", "lapis lazuli ore", "lead", "lever", 
    "light blue concrete", "light gray concrete", "light gray wool", 
    "lily pad", "lava", "lava bucket", "magma", "magma block", 
    "melon", "melon seeds", "milk bucket", "minecart", "minecart with chest", 
    "minecart with furnace", "minecart with hopper", "mooshroom", "mushroom", 
    "name tag", "nether brick", "nether brick fence", "nether gold ore", 
    "netherite", "netherite ingot", "netherite pickaxe", "netherite sword", 
    "netherrack", "oak boat", "oak button", "oak door", "oak fence", 
    "oak fence gate", "oak leaves", "oak log", "oak planks", "oak sign", 
    "oak stairs", "oak trapdoor", "oak wood", "obsidian", "ocelot", 
    "ender pearl", "ocean monument", "peony", "piston", "piston head", 
    "poisonous potato", "portal", "potato", "potted acacia", "potted allium", 
    "potted azalea", "potted bamboo", "potted birch", "potted cactus", 
    "potted cornflower", "potted dark oak", "potted fern", 
    "potted jungle", "potted lily of the valley", "potted mangrove", 
    "potted mushroom", "potted oak", "potted palm", "potted pink tulip", 
    "potted poppy", "potted red tulip", "potted sunflower", 
    "potted tulip", "pufferfish", "pumpkin", "pumpkin pie", "quartz", 
    "quartz block", "quartz pillar", "rabbit", "rabbit stew", 
    "red concrete", "red dye", "red wool", "redstone", "redstone block", 
    "redstone lamp", "redstone ore", "redstone torch", "salmon", 
    "sand", "sandstone", "scaffolding", "skeleton", "skeleton horse", 
    "slime", "soul sand", "sponge", "sugar cane", "tall grass", 
    "tnt", "torch", "trapdoor", "trident", "tropical fish", "turtle", 
    "vine", "water", "water bucket", "wheat", "wood", "wooden axe", 
    "wooden door", "wooden pickaxe", "wooden sword", "wool", "zombie", 
    "zombie pigman", "zombie villager", "bat", "blaze", "blaze rod", 
    "blaze powder", "phantom", "witch", "drowned", "warden", "vindicator", 
    "vex", "evoker", "pillager", "ravager", "axolotl", "cat", 
    "wolf", "parrot", "llama", "goat", "fox", "panda", "strider",
    "mangrove boat", "mangrove button", "mangrove door", "mangrove fence",
    "mangrove fence gate", "mangrove leaves", "mangrove log", "mangrove planks",
    "mangrove roots", "mangrove sign", "mangrove stairs", "mangrove trapdoor",
    "mangrove wood", "copper", "copper block", "cut copper", "exposed copper", 
    "waxed copper", "waxed exposed copper", "lightning rod", "spyglass",
    "sculk", "sculk sensor", "sculk shrieker", "sculk catalyst", "candle",
    "sculk vein", "bamboo", "bamboo sapling", "bamboo raft", "cherry log",
    "cherry planks", "cherry sapling", "cherry button", "cherry door", 
    "cherry fence", "cherry fence gate", "cherry sign", "cherry stairs",
    "cherry trapdoor", "cherry wood", "fishing", "fishing net", "fishing rod", 
    "spear", "taming", "fishing bait", "cooked fish", "fishing lure", 
    "fishing tackle", "fishing supplies", "fish trap", "prawn trap", 
    "crab trap", "lobster trap", "scuba", "fishing gear", "fishing reel", 
    "fishing pole", "fishing line", "fishing boat", "fishing expedition",
    "fishing report", "tackle box", "fishing location", "fishing technique",
    "fishing hole", "fishing rules", "fishing experience", "fishing tournament"
}


intents = discord.Intents.all()
intents.messages = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready and logged in as {0.user}".format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"Message Received: '{message.content}'")
    content = message.content.lower()
    if any(keyword in content for keyword in KEYWORDS):
        await asyncio.sleep(COOLDOWN)
        links = [f"https://minecraft.fandom.com/wiki/{keyword.replace(' ', '_')}" for keyword in KEYWORDS if keyword in content]
        if links:
            combined_links = "\n".join(links)
            print(f"Links to send: {combined_links}")
            while len(combined_links) > 2000:
                split_index = combined_links.rfind("\n", 0, 1990)
                if split_index == -1:
                    split_index = 1990
                await message.channel.send(combined_links[:split_index] + "...\n(Links trimmed due to size limits.)")
                combined_links = combined_links[split_index:]
            await message.channel.send(combined_links)
bot.run(TOKEN)
