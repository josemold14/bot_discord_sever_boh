import os
from dotenv import load_dotenv

load_dotenv() # <--- Carga las variables del archivo .env

import discord
from discord.ext import commands

# --- CONFIGURAZIONE DEGLI INTENTS ---
# Devono essere ATTIVATI anche sul Portale Sviluppatori di Discord!
intents = discord.Intents.default()
intents.message_content = True  # Necessario per leggere i comandi (come !ciao)
intents.members = True          # Necessario per rilevare l'arrivo di nuovi membri (per il benvenuto)


# --- CONFIGURAZIONE DEL BOT ---
# Definisce il prefisso di comando: usa '!'
bot = commands.Bot(command_prefix='!', intents=intents)

# --- CONFIGURAZIONE DEL CANALE DI BENVENUTO ---
# IMPORTANTE: Sostituisci questo ID con l'ID numerico del tuo canale di benvenuto.
# Vai su Impostazioni Utente -> Avanzate -> Attiva Modalità Sviluppatore.
# Poi clicca destro sul canale e 'Copia ID'.
ID_CANALE_BENVENUTO = 123456789012345678  # <-- SOSTITUISCI QUESTO NUMERO!

# --- EVENTI DEL BOT ---

@bot.event
async def on_ready():
    """Viene eseguito quando il bot è connesso e pronto."""
    print(f'Il bot è loggato come {bot.user}!')
    print(f'Stato del Member Intent: {"ATTIVATO ✅" if bot.intents.members else "DISATTIVATO ❌"}')
    print('-------------------------------------------')

@bot.event
async def on_member_join(member):
    """Viene eseguito quando un nuovo membro si unisce al server."""
    
    print(f"--- EVENTO MEMBRO UNITO: {member.name} ---") # Messaggio di debug nel terminale
    
    # 1. Ottiene il canale di benvenuto tramite l'ID
    channel = bot.get_channel(1449514458983563374)
    
    if channel is not None:
        try:
            # 2. Invia il messaggio di benvenuto
            await channel.send(f'🎉 Benvenuto/a nel server, {member.mention}! Siamo felici di averti con noi, non dimenticarti di leggere le {regole}. Una cosa in piú puoi fare due comandi con me !ciao e !regole si fai quello !regole ti diro le diverse regole')
            print("Messaggio di benvenuto inviato con successo.")
        except discord.Forbidden:
            print("ERRORE PERMESSI: Il bot non può scrivere nel canale di benvenuto.")
        except Exception as e:
            print(f"ERRORE SCONOSCIUTO durante l'invio del messaggio: {e}")
    else:
        print(f"ERRORE: Canale con ID {1449514458983563374} non trovato.")


# --- COMANDI DEL BOT ---

@bot.command()
async def ciao(ctx):
    """Risponde con un saluto quando viene usato il comando !ciao."""
    await ctx.send(f'Ciao, {ctx.author.name}! Sono il tuo bot e sono operativo.')
    
# Asegúrate de que esta línea @bot.command() está pegada al margen izquierdo.
@bot.command()
async def regole(ctx):
    """Mostra le regole specifiche per il canale in cui viene utilizzato."""
    
    # Prende il nome del canale e lo mette in minuscolo per una comparazione sicura
    nome_canal = ctx.channel.name.lower()
    
    # Inizializza la variabile del messaggio
    messaggio_finale = ""

    # --- LOGICA CONDIZIONALE if/elif ---

    if nome_canal == "regole":
        messaggio_finale = (
            "📜 **REGOLAMENTO COMPLETO** 📜\n"
            "Benvenuto/a nel cuore delle nostre regole. **Leggi attentamente ogni punto.** "
            "Non dire parolaccie ne offendere nessuno."
            "Non madare contenuti offesivi."
            "Seguire le regole specificate nei diversi canala"
        )
        
    elif nome_canal == "benvenuto":
        messaggio_finale = (
            "👋 **BENVENUTO & INTRODUZIONE** 👋\n"
            "Ciao! Per favore, presentati qui, ma **non fare domande sul server.** "
            "Usa il canale #generale o #regole per ulteriori informazioni."
            "Non dire parolaccie ne offendere nessuno."
            "Non madare contenuti offesivi."
        )
        
    elif nome_canal == "classe":
        messaggio_finale = (
            "📚 **FOCUS SUGLI STUDI** 📚\n"
            "Questo canale è dedicato esclusivamente ai **compiti e alle domande della tua classe.** "
            "Qualsiasi altro argomento (spam, off-topic, giochi) è vietato."
            "Non dire parolaccie ne offendere nessuno."
            "Non madare contenuti offesivi."
        )
        
    elif nome_canal == "minecraft":
        messaggio_finale = (
            "⛏️ **FOCUS SUL GIOCO** ⛏️\n"
            "Discuti qui solo di **Minecraft (server, mod, costruzioni).** "
            "Non dire parolaccie ne offendere nessuno."
            "Non madare contenuti offesivi."
        )
        
    elif nome_canal == "lingue":
        messaggio_finale = (
            "🗣️ **FOCUS SULLA LINGUA** 🗣️\n"
            "In questo canale si parla **sulle lingue (grammatica,memi ecc...).** "
            "Per favore, mantieni l'attenzione sul miglioramento linguistico e la pratica."
            "Non dire parolaccie ne offendere nessuno."
            "Non madare contenuti offesivi."
        )
        
    elif nome_canal == "general":
        messaggio_finale = (
            "💬 **REGOLE GENERALI** 💬\n"
            "Non dire parolaccie ne offendere nessuno."
            "Non madare contenuti offesivi."
            "Parlare sul tema speccificato sui canali"
        )
    elif nome_canal == "meme":
        menssaggio_finala =(
            "Si parla sui meme quindi poi dire quello che vuoi sui meme"
            "Non dire parolaccie ne offendere nessuno."
            "Non madare contenuti offesivi."
        )
        
    
        
    else:
        # Se non è nessuno dei canali specificati, invia un messaggio di errore
        messaggio_finale = (
            f"🚫 Comando `!regole` non valido qui.\n"
            f"Per favore, usalo in un canale specifico o in #regole."
        )

    # Invia il messaggio finale determinato dalla condizione
    await ctx.send(messaggio_finale)

# --- AVVIO DEL BOT ---

# *** IL PASSO PIÙ CRITICO: IL TUO TOKEN ***
# SOSTITUISCI 'IL_TUO_TOKEN_SEGRETO_QUI' con il token del tuo bot.
bot.run(os.getenv("DISCORD_TOKEN"))